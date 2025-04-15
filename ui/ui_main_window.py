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
from PySide6.QtWidgets import (QApplication, QComboBox, QGraphicsView, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(363, 339)
        MainWindow.setMinimumSize(QSize(363, 339))
        MainWindow.setMaximumSize(QSize(363, 339))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(11, 1, 343, 283))
        self.gridLayout_4 = QGridLayout(self.widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_url = QLabel(self.widget)
        self.label_url.setObjectName(u"label_url")

        self.gridLayout_2.addWidget(self.label_url, 0, 0, 1, 1)

        self.lineEdit_url = QLineEdit(self.widget)
        self.lineEdit_url.setObjectName(u"lineEdit_url")

        self.gridLayout_2.addWidget(self.lineEdit_url, 0, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.btn_fetch = QPushButton(self.widget)
        self.btn_fetch.setObjectName(u"btn_fetch")

        self.gridLayout_4.addWidget(self.btn_fetch, 0, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btn_download = QPushButton(self.widget)
        self.btn_download.setObjectName(u"btn_download")

        self.gridLayout_3.addWidget(self.btn_download, 1, 1, 1, 1)

        self.combo_format = QComboBox(self.widget)
        self.combo_format.setObjectName(u"combo_format")

        self.gridLayout_3.addWidget(self.combo_format, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.graphicsView = QGraphicsView(self.widget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 2)

        self.progressBar_download = QProgressBar(self.widget)
        self.progressBar_download.setObjectName(u"progressBar_download")
        self.progressBar_download.setEnabled(True)
        self.progressBar_download.setValue(0)
        self.progressBar_download.setTextVisible(True)
        self.progressBar_download.setOrientation(Qt.Horizontal)
        self.progressBar_download.setInvertedAppearance(False)

        self.gridLayout_3.addWidget(self.progressBar_download, 2, 0, 1, 2)


        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 363, 21))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Video Downloader", None))
        self.label_url.setText(QCoreApplication.translate("MainWindow", u"URL:", None))
        self.btn_fetch.setText(QCoreApplication.translate("MainWindow", u"Recup infos", None))
        self.btn_download.setText(QCoreApplication.translate("MainWindow", u"Download", None))
    # retranslateUi

