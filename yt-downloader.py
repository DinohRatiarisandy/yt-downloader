import os
import sys
from pathlib import Path

from yt_dlp import YoutubeDL

if getattr(sys, "frozen", False):
    # PyInstaller executable
    BASE_DIR = sys._MEIPASS
else:
    # Normal Python script
    BASE_DIR = os.path.abspath(".")

FFMPEG_PATH = os.path.join(BASE_DIR, "ffmpeg", "bin", "ffmpeg.exe")

options = {"quiet": True, "skip_download": True, "ffmpeg_location": FFMPEG_PATH}


def get_video_infos(url: str):
    with YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=False)

        print(f"🎬 Title: {info['title']}")

        for f in info["formats"]:
            if f.get("vcodec", "none") != "none" and f.get("height", 0) >= 360:
                fmt_id = f["format_id"]
                ext = f["ext"]
                height = f.get("height", "?")
                fps = f.get("fps", "")
                size = f.get("filesize", 0)
                size_str = f"{round(size / 1024 / 1024, 2)} MB" if size else "?"
                print(
                    f"- id={fmt_id:>4} | {ext} | {height}p | fps: {fps} | size: {size_str}"
                )


def download_video(
    url: str,
    format_id: str,
):
    output_path = str(Path.home() / "Downloads")

    os.makedirs(output_path, exist_ok=True)

    options = {
        "format": f"{format_id}+bestaudio/best",  # video format + best audio
        "merge_output_format": "mp4",  # output as mp4 after merging
        "outtmpl": os.path.join(output_path, "%(title)s.%(ext)s"),
        "ffmpeg_location": FFMPEG_PATH,
    }

    with YoutubeDL(options) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    url = input("URL: ").strip()
    get_video_infos(url)

    video_id = input("Video id: ").strip()

    download_video(url, video_id)
