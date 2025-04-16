import json
import os
import sys
from pathlib import Path

import requests
from PySide6.QtCore import QByteArray, QThread
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from core.video_downloader import VideoDownloader
from core.video_info import VideoInfo
from core.workers import DownloadWorker, FetchWorker
from ui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.fetch_thread = None
        self.download_thread = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.video_url = ""
        self.formats = []

        self.ui.btn_download.clicked.connect(self.download_video)
        self.ui.lineEdit_url.textChanged.connect(self.on_update_button_state)
        self.ui.combo_format.currentIndexChanged.connect(self.on_update_button_state)

        self.ui.progressBar_download.setVisible(False)
        self.ui.btn_download.setVisible(False)
        self.ui.combo_format.setVisible(False)

    def fetch_info(self):
        url = self.ui.lineEdit_url.text().strip()
        if not url:
            QMessageBox.warning(self, "Erreur", "Veuillez entrer une URL.")
            return

        self.fetch_thread = QThread()
        self.fetch_worker = FetchWorker(url)
        self.fetch_worker.moveToThread(self.fetch_thread)

        self.fetch_thread.started.connect(self.fetch_worker.run)
        self.fetch_worker.finished.connect(self.on_fetch_finished)
        self.fetch_worker.error.connect(self.on_fetch_error)
        self.fetch_worker.finished.connect(self.fetch_thread.quit)
        self.fetch_worker.finished.connect(self.fetch_worker.deleteLater)
        self.fetch_thread.finished.connect(self.fetch_thread.deleteLater)

        self.fetch_thread.start()

    def on_fetch_finished(self, info, formats):
        self.formats = formats
        self.video_url = self.ui.lineEdit_url.text().strip()

        self.ui.combo_format.clear()
        for f in formats:
            fmt_id = f["format_id"]
            label = f"{fmt_id} | {f['ext']} | {f.get('height', '?')}p | {f['size']}"
            self.ui.combo_format.addItem(label, fmt_id)

        # show the video title
        self.ui.label_video_title.setText(f"{info['title']}")

        # show the download button and the combo_format
        self.ui.combo_format.setVisible(True)
        self.ui.btn_download.setVisible(True)

        # show the video thumbnail
        thumbnail_url = info.get("thumbnail", "")
        if thumbnail_url:
            try:
                response = requests.get(thumbnail_url)
                img_data = response.content
                pixmap = QPixmap()
                pixmap.loadFromData(QByteArray(img_data))
                self.ui.label_thumbnail.setPixmap(pixmap.scaled(320, 180))
            except Exception:
                self.ui.label_thumbnail.clear()
        else:
            self.ui.label_thumbnail.clear()

    def on_fetch_error(self, error):
        QMessageBox.critical(self, "Erreur", error)

    def download_video(self):
        fmt_id = self.ui.combo_format.currentData()
        if not self.video_url or not fmt_id:
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un format.")
            return

        self.ui.progressBar_download.setValue(0)
        self.ui.progressBar_download.setVisible(True)
        self.ui.btn_download.setEnabled(False)

        self.download_thread = QThread()
        self.download_worker = DownloadWorker(self.video_url, fmt_id)
        self.download_worker.progress.connect(self.ui.progressBar_download.setValue)
        self.download_worker.moveToThread(self.download_thread)

        self.download_thread.started.connect(self.download_worker.run)
        self.download_worker.finished.connect(self.on_download_finished)
        self.download_worker.error.connect(self.on_download_error)
        self.download_worker.finished.connect(self.download_thread.quit)
        self.download_worker.finished.connect(self.download_worker.deleteLater)
        self.download_thread.finished.connect(self.download_thread.deleteLater)

        self.download_thread.start()

    def on_download_finished(self):
        self.ui.btn_download.setEnabled(True)
        self.ui.progressBar_download.setValue(100)
        QMessageBox.information(self, "Succès", "Téléchargement terminé.")

    def on_download_error(self, error):
        self.ui.btn_download.setEnabled(True)
        self.ui.progressBar_download.setValue(0)
        QMessageBox.critical(self, "Erreur", error)

    def on_update_button_state(self):
        url = self.ui.lineEdit_url.text().strip()
        url_not_empty = bool(url)
        format_selected = self.ui.combo_format.currentIndex() != -1

        if url_not_empty and url != self.video_url:
            self.fetch_info()

        self.ui.btn_download.setEnabled(url_not_empty and format_selected)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
