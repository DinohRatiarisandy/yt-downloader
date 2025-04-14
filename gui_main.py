import os
import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from core.video_downloader import VideoDownloader
from core.video_info import VideoInfo
from ui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.video_url = ""
        self.formats = []

        self.ui.btn_fetch.clicked.connect(self.fetch_info)
        self.ui.btn_download.clicked.connect(self.download_video)

    def fetch_info(self):
        url = self.ui.lineEdit_url.text().strip()
        if not url:
            QMessageBox.warning(self, "Erreur", "Veuillez entrer une URL.")
            return

        try:
            vi = VideoInfo(url)
            info = vi.get_video_infos()
            self.formats = vi.extract_formats(info)
            self.video_url = url

            self.ui.combo_format.clear()
            for f in self.formats:
                fmt_id = f["format_id"]
                label = f"{fmt_id} | {f['ext']} | {f.get('height', '?')}p | {f['size']}"
                self.ui.combo_format.addItem(label, fmt_id)
            QMessageBox.information(self, "Infos", f"Titre: {info['title']}")
        except Exception as e:
            QMessageBox.critical(self, "Erreur", str(e))

    def download_video(self):
        fmt_id = self.ui.combo_format.currentData()
        if not self.video_url or not fmt_id:
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un format.")
            return

        try:
            vd = VideoDownloader(self.video_url, fmt_id)
            vd.download()
            QMessageBox.information(self, "Succès", "Téléchargement terminé.")
        except Exception as e:
            QMessageBox.critical(self, "Erreur", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
