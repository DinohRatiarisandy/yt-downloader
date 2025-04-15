from PySide6.QtCore import QObject, Signal

from core.video_downloader import VideoDownloader
from core.video_info import VideoInfo


class FetchWorker(QObject):
    finished = Signal(dict, list)
    error = Signal(str)

    def __init__(self, url: str):
        super().__init__()
        self.url = url

    def run(self):
        try:
            vi = VideoInfo(self.url)
            info = vi.get_video_infos()
            formats = vi.extract_formats(info)
            self.finished.emit(info, formats)
        except Exception as e:
            self.error.emit(str(e))


class DownloadWorker(QObject):
    finished = Signal()
    error = Signal(str)
    progress = Signal(int)

    def __init__(self, url: str, format_id: str):
        super().__init__()
        self.url = url
        self.format_id = format_id

    def run(self):
        try:
            vd = VideoDownloader(
                self.url, self.format_id, progress_hook=self.progress_hook
            )
            vd.download()
            self.finished.emit()
        except Exception as e:
            self.error.emit(str(e))

    def progress_hook(self, d):
        if d["status"] == "downloading":
            total_bytes = d.get("total_bytes") or d.get("total_bytes_estimate")
            downloaded_bytes = d.get("downloaded_bytes", 0)

            if total_bytes:
                percent = int(downloaded_bytes / total_bytes * 100)
                self.progress.emit(percent)
