# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QToolButton, QVBoxLayout, QWidget)
import resource_rc

class Ui_VideoDl(object):
    def setupUi(self, VideoDl):
        if not VideoDl.objectName():
            VideoDl.setObjectName(u"VideoDl")
        VideoDl.resize(622, 656)
        icon = QIcon()
        icon.addFile(u":/icon/recource/download.png", QSize(), QIcon.Normal, QIcon.Off)
        VideoDl.setWindowIcon(icon)
        VideoDl.setStyleSheet(u"QFrame{\n"
"border: 0px;\n"
"}")
        self.centralwidget = QWidget(VideoDl)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(80, 80))
        self.label_5.setPixmap(QPixmap(u":/icon/resource/download.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 50))
        self.label.setStyleSheet(u"font: 20pt \"Microsoft YaHei UI\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.frame_5)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 40))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.lineEditUrl = QLineEdit(self.centralwidget)
        self.lineEditUrl.setObjectName(u"lineEditUrl")
        self.lineEditUrl.setStyleSheet(u"height: 35px;\n"
"font: 12pt \"Lucida Console\";\n"
"border-radius:5px;\n"
"padding: 3px 10px;\n"
"")

        self.verticalLayout.addWidget(self.lineEditUrl)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButtonDownload = QPushButton(self.frame_2)
        self.pushButtonDownload.setObjectName(u"pushButtonDownload")
        self.pushButtonDownload.setMinimumSize(QSize(120, 0))
        self.pushButtonDownload.setMaximumSize(QSize(120, 16777215))
        self.pushButtonDownload.setStyleSheet(u"height: 25px;\n"
"\n"
"/*\n"
"\n"
"QPushButton{\n"
"font: 16pt \"\u9ed1\u4f53\";\n"
"height: 30px;\n"
"border: 2px solid #ccc;\n"
"border-radius: 5px;\n"
"background-color: rgb(0, 127, 0);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 0);\n"
"}\n"
"QPushButton:press{\n"
"	background-color: rgb(0, 113, 0);\n"
"}\n"
"\n"
"\n"
"*/")

        self.horizontalLayout.addWidget(self.pushButtonDownload)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_3)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toolButtonChageSaveDir = QToolButton(self.frame_3)
        self.toolButtonChageSaveDir.setObjectName(u"toolButtonChageSaveDir")

        self.horizontalLayout_2.addWidget(self.toolButtonChageSaveDir)

        self.label_SaveDir = QLabel(self.frame_3)
        self.label_SaveDir.setObjectName(u"label_SaveDir")

        self.horizontalLayout_2.addWidget(self.label_SaveDir)


        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.frame_3)

        self.checkBox_forceoverwrite = QCheckBox(self.frame)
        self.checkBox_forceoverwrite.setObjectName(u"checkBox_forceoverwrite")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.checkBox_forceoverwrite)

        self.checkBox_savethumbnail = QCheckBox(self.frame)
        self.checkBox_savethumbnail.setObjectName(u"checkBox_savethumbnail")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.checkBox_savethumbnail)

        self.checkBox_savearcheive = QCheckBox(self.frame)
        self.checkBox_savearcheive.setObjectName(u"checkBox_savearcheive")
        self.checkBox_savearcheive.setChecked(True)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.checkBox_savearcheive)

        self.checkBox_debug = QCheckBox(self.frame)
        self.checkBox_debug.setObjectName(u"checkBox_debug")
        self.checkBox_debug.setChecked(False)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.checkBox_debug)


        self.verticalLayout.addWidget(self.frame)

        self.textEditLog = QTextEdit(self.centralwidget)
        self.textEditLog.setObjectName(u"textEditLog")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditLog.sizePolicy().hasHeightForWidth())
        self.textEditLog.setSizePolicy(sizePolicy)
        self.textEditLog.setStyleSheet(u"font: 10pt \"Lucida Console\";\n"
"border-radius: 5px;")
        self.textEditLog.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEditLog)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButtonClearLog = QPushButton(self.frame_4)
        self.pushButtonClearLog.setObjectName(u"pushButtonClearLog")
        self.pushButtonClearLog.setMinimumSize(QSize(100, 0))
        self.pushButtonClearLog.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButtonClearLog)

        self.pushButtonOpenDownloadDir = QPushButton(self.frame_4)
        self.pushButtonOpenDownloadDir.setObjectName(u"pushButtonOpenDownloadDir")
        self.pushButtonOpenDownloadDir.setMinimumSize(QSize(100, 0))
        self.pushButtonOpenDownloadDir.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButtonOpenDownloadDir)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_4)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        VideoDl.setCentralWidget(self.centralwidget)

        self.retranslateUi(VideoDl)

        QMetaObject.connectSlotsByName(VideoDl)
    # setupUi

    def retranslateUi(self, VideoDl):
        VideoDl.setWindowTitle(QCoreApplication.translate("VideoDl", u"Video Download", None))
        self.label_5.setText("")
        self.label.setText(QCoreApplication.translate("VideoDl", u"\u89c6\u9891\u4e0b\u8f7d", None))
        self.label_2.setText(QCoreApplication.translate("VideoDl", u"\u652f\u6301 Youtube\uff0cBilibili \u89c6\u9891\u3002\u590d\u5236\u89c6\u9891\u6216\u4e13\u8f91\u7684\u94fe\u63a5\uff0c\u5373\u53ef\u4e0b\u8f7d\u3002", None))
        self.lineEditUrl.setPlaceholderText(QCoreApplication.translate("VideoDl", u"https://", None))
        self.pushButtonDownload.setText(QCoreApplication.translate("VideoDl", u"\u4e0b\u8f7d", None))
        self.label_3.setText(QCoreApplication.translate("VideoDl", u"\u5b58\u653e\u76ee\u5f55", None))
        self.toolButtonChageSaveDir.setText(QCoreApplication.translate("VideoDl", u"\u9009\u62e9...", None))
        self.label_SaveDir.setText(QCoreApplication.translate("VideoDl", u"C:\\Users\\User\\Downloads", None))
        self.checkBox_forceoverwrite.setText(QCoreApplication.translate("VideoDl", u"\u8986\u76d6\u5b58\u5728\u89c6\u9891", None))
        self.checkBox_savethumbnail.setText(QCoreApplication.translate("VideoDl", u"\u4fdd\u5b58\u7f29\u7565\u56fe", None))
#if QT_CONFIG(statustip)
        self.checkBox_savearcheive.setStatusTip(QCoreApplication.translate("VideoDl", u"\u4fdd\u5b58\u5f52\u6863\u6587\u4ef6\uff0c\u5728\u6279\u91cf\u4e0b\u8f7d\u7684\u65f6\u5019\uff0c\u53ef\u4ee5\u907f\u514d\u91cd\u590d\u4e0b\u8f7d\u3002", None))
#endif // QT_CONFIG(statustip)
        self.checkBox_savearcheive.setText(QCoreApplication.translate("VideoDl", u"\u4fdd\u5b58Archive\u8bb0\u5f55", None))
        self.checkBox_debug.setText(QCoreApplication.translate("VideoDl", u"Debug", None))
        self.pushButtonClearLog.setText(QCoreApplication.translate("VideoDl", u"\u6e05\u9664", None))
        self.pushButtonOpenDownloadDir.setText(QCoreApplication.translate("VideoDl", u"\u6253\u5f00\u76ee\u5f55", None))
        self.label_4.setText(QCoreApplication.translate("VideoDl", u"zcq100 v2023.1 (yt-dlp)", None))
    # retranslateUi

