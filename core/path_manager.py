import os
import sys
from pathlib import Path

if getattr(sys, "frozen", False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.abspath(".")

FFMPEG_PATH = os.path.join(BASE_DIR, "ffmpeg", "bin", "ffmpeg.exe")
OUTPUT_PATH = str(Path.home() / "Downloads")


class PathManager:
    @staticmethod
    def ensure_directory(path: str):
        os.makedirs(path, exist_ok=True)

    @staticmethod
    def get_ffmpeg_path():
        return FFMPEG_PATH

    @staticmethod
    def get_output_path():
        return OUTPUT_PATH
