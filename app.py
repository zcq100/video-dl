import os
import pickle
import sys
import yt_dlp
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QTextCursor
from video_dl.main_ui import Ui_VideoDl

_HOMEDIR = ""
if sys.platform == "win32":
    _HOMEDIR = os.environ.get("APPDATA")
else:
    _HOMEDIR = os.environ.get("HOME")
    _HOMEDIR = os.path.join(_HOMEDIR, ".config")
_HOMEDIR = os.path.join(_HOMEDIR, "video-dl")
os.makedirs(_HOMEDIR, exist_ok=True)
_CONFIG = os.path.join(_HOMEDIR, "config.pkl")


class MyLogger:
    def __init__(self, textEdit) -> None:
        self.textEdit = textEdit

    def debug(self, msg):
        # For compatibility with youtube-dl, both debug and info are passed into debug
        # You can distinguish them by the prefix '[debug] '
        # if msg.startswith("[debug] "):
        #     pass
        # else:
        self.info(msg)

    def info(self, msg):
        self.textEdit.append(msg)
        self.textEdit.moveCursor(QTextCursor.End)

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


class DownloadThread(QThread):
    # 通过类成员对象定义信号对象
    signal = Signal(int)

    def __init__(self, url, download_folder, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.url = url
        self.download_folder = download_folder

    def progress_hook(self, d):
        if d["status"] == "finished":
            self.parent.textEditLog.append("下载完成，正在转码...")
        if d["status"] == "downloading":
            p = d["_percent_str"].replace("%", "")  # 获取下载进度，去掉 '%'，并转换为整数
            db = int(d["downloaded_bytes"])
            tb = int(d["total_bytes"])
            self.signal.emit(int(db / tb * 100))  # 发送信号
        # if d["status"] == "finished":
        #     self.parent.textEditLog.append("下载完成")

    def run(self):
        logger = MyLogger(self.parent.textEditLog)
        ydl_opts = {
            "logger": logger,
            "paths": {"home": self.download_folder},
            "writethumbnail": self.parent.checkBox_savethumbnail.isChecked(),
            "overwrites": self.parent.checkBox_forceoverwrite.isChecked(),
            "no_color": True,
            "verbose": self.parent.checkBox_debug.isChecked(),
            "progress_hooks": [self.progress_hook],
        }

        # 是否保存archive文件
        if self.parent.checkBox_savearchive.isChecked():
            archieve_path = os.path.join(self.download_folder, "archive.txt")
            ydl_opts["download_archive"] = archieve_path

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(self.url)

        logger.info("任务完成")
        # 启用下载按钮
        self.parent.download_finished()


class MainUi(QMainWindow, Ui_VideoDl):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.load_gui_config()

        # 设置应用的图标
        # self.setWindowIcon(QIcon(":/icon/recource/download.icon"))
        if sys.platform == "win32":
            download_dir = os.path.join(os.environ.get("USERPROFILE"), "Downloads")
        else:
            download_dir = os.path.join(os.environ.get("HOME"), "Downloads")

        self.label_SaveDir.setText(download_dir)
        self.pushButtonDownload.clicked.connect(self.download)
        self.toolButtonChageSaveDir.clicked.connect(self.choose_folder)
        self.pushButtonClearLog.clicked.connect(self.textEditLog.clear)
        self.pushButtonOpenDownloadDir.clicked.connect(self.open_download_dir)

    def open_download_dir(self):
        download_dir = self.label_SaveDir.text()
        os.startfile(download_dir)

    def download(self):
        self.textEditLog.clear()
        url = self.lineEditUrl.text()
        if url.strip() == "":
            self.textEditLog.append("没有输入下载链接.")
            return

        self.pushButtonDownload.setEnabled(False)

        download_folder = self.label_SaveDir.text()
        self.download_thread = DownloadThread(url, download_folder, self)
        self.download_thread.signal.connect(self.update_progress)
        self.download_thread.start()

    # 选择保存的目录
    def choose_folder(self):
        download_dir = self.label_SaveDir.text()
        dir = QFileDialog.getExistingDirectory(
            self, "选择保存的目录", download_dir, QFileDialog.ShowDirsOnly
        )
        if dir:
            self.label_SaveDir.setText(dir)

    def update_progress(self, p):
        self.progressBar_download.setValue(p)

    def download_finished(self):
        self.pushButtonDownload.setEnabled(True)

    def closeEvent(self, event):
        self.save_gui_config()
        super().closeEvent(event)

    def save_gui_config(self):
        opts = {
            "url": self.lineEditUrl.text(),
            "download_dir": self.label_SaveDir.text(),
            "savethumbnail": self.checkBox_savethumbnail.isChecked(),
            "forceoverwrite": self.checkBox_forceoverwrite.isChecked(),
            "debug": self.checkBox_debug.isChecked(),
            "savearchive": self.checkBox_savearchive.isChecked(),
        }
        pickle.dump(opts, open(_CONFIG, "wb"))

    def load_gui_config(self):
        if os.path.exists(_CONFIG):
            try:
                opts = pickle.load(open(_CONFIG, "rb"))
                self.lineEditUrl.setText(opts["url"])
                self.label_SaveDir.setText(opts["download_dir"])
                self.checkBox_savethumbnail.setChecked(opts["savethumbnail"])
                self.checkBox_forceoverwrite.setChecked(opts["forceoverwrite"])
                self.checkBox_debug.setChecked(opts["debug"])
                self.checkBox_savearchive.setChecked(opts["savearchive"])
            except:
                pass
        else:
            self.save_gui_config()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainUi()
    window.show()
    sys.exit(app.exec())
