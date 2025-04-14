# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 640)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 10, 381, 106))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_url = QLineEdit(self.widget)
        self.lineEdit_url.setObjectName(u"lineEdit_url")

        self.gridLayout.addWidget(self.lineEdit_url, 0, 1, 1, 1)

        self.btn_fetch = QPushButton(self.widget)
        self.btn_fetch.setObjectName(u"btn_fetch")

        self.gridLayout.addWidget(self.btn_fetch, 1, 1, 1, 1)

        self.combo_format = QComboBox(self.widget)
        self.combo_format.setObjectName(u"combo_format")

        self.gridLayout.addWidget(self.combo_format, 3, 1, 1, 1)

        self.btn_download = QPushButton(self.widget)
        self.btn_download.setObjectName(u"btn_download")

        self.gridLayout.addWidget(self.btn_download, 4, 1, 1, 1)

        self.label_url = QLabel(self.widget)
        self.label_url.setObjectName(u"label_url")

        self.gridLayout.addWidget(self.label_url, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 480, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Video Downloader", None))
        self.btn_fetch.setText(QCoreApplication.translate("MainWindow", u"Recup infos", None))
        self.btn_download.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.label_url.setText(QCoreApplication.translate("MainWindow", u"URL:", None))
    # retranslateUi

