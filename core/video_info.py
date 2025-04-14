from yt_dlp import YoutubeDL

from core.path_manager import PathManager


class VideoInfo:
    def __init__(self, url: str):
        self.url = url
        self.options = {
            "quiet": True,
            "skip_download": True,
            "ffmpeg_location": PathManager.get_ffmpeg_path(),
        }

    def get_video_infos(self):
        with YoutubeDL(self.options) as ydl:
            info = ydl.extract_info(self.url, download=False)
            return info

    def extract_formats(self, info: dict):
        formats = []
        for f in info["formats"]:
            if f.get("vcodec", "none") != "none" and f.get("height", 0) >= 360:
                size = f.get("filesize", 0)
                size_str = f"{round(size / 1024 / 1024, 2)} MB" if size else "?"
                formats.append(
                    {
                        "format_id": f["format_id"],
                        "ext": f["ext"],
                        "height": f.get("height", "?"),
                        "fps": f.get("fps", ""),
                        "size": size_str,
                    }
                )

        return formats
