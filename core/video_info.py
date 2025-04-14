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
            print(f"Title: {info["title"]}")

            for format in info["formats"]:
                if (
                    format.get("vcodec", "none") != "none"
                    and format.get("height", 0) >= 360
                ):
                    fmt_id = format["format_id"]
                    ext = format["ext"]
                    height = format.get("height", "?")
                    fps = format.get("fps", "")
                    size = format.get("filesize", 0)
                    size_str = f"{round(size / 1024 / 1024, 2)} MB" if size else "?"
                    print(
                        f"- id={fmt_id:>4} | {ext} | {height}p | fps: {fps} | size: {size_str}"
                    )
