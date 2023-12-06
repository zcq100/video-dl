import os
import sys
import yt_dlp
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from video_dl.main_ui import Ui_VideoDl


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

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


class MainUi(QMainWindow, Ui_VideoDl):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 设置应用的图标
        # self.setWindowIcon(QIcon(":/icon/recource/download.icon"))
        self.pushButtonDownload.clicked.connect(self.download)
        if sys.platform == "win32":
            download_dir = os.path.join(os.environ.get("USERPROFILE"), "Downloads")
        else:
            download_dir = os.path.join(os.environ.get("HOME"), "Downloads")

        self.label_SaveDir.setText(download_dir)
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

        download_folder = self.label_SaveDir.text()
        archieve_path = os.path.join(download_folder, "archive.txt")

        ydl_opts = {
            "logger": MyLogger(self.textEditLog),
            "paths": {"home": download_folder},
            "writethumbnail": self.checkBox_savethumbnail.isChecked(),
            "download_archive": archieve_path,
            "overwrites": True,
            "verbose": self.checkBox_debug.isChecked()
            # 'progress_hooks': [my_hook],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(url)

    # 选择保存的目录
    def choose_folder(self):
        download_dir = self.label_SaveDir.text()
        dir = QFileDialog.getExistingDirectory(
            self, "选择保存的目录", download_dir, QFileDialog.ShowDirsOnly
        )
        if dir:
            self.label_SaveDir.setText(dir)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainUi()
    window.show()
    sys.exit(app.exec())
