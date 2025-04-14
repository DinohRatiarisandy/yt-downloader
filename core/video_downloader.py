import os

from yt_dlp import YoutubeDL

from core.path_manager import PathManager


class VideoDownloader:
    def __init__(self, url: str, format_id: str):
        self.url = url
        self.format_id = format_id
        self.options = {
            "format": f"{self.format_id}+bestaudio/best",
            "merge_output_format": "mp4",
            "outtmpl": os.path.join(PathManager.get_output_path(), "%(title)s.%(ext)s"),
            "ffmpeg_location": PathManager.get_ffmpeg_path(),
        }

    def download(self):
        PathManager.ensure_directory(PathManager.get_output_path())

        with YoutubeDL(self.options) as ydl:
            ydl.download([self.url])
