from core.video_downloader import VideoDownloader
from core.video_info import VideoInfo

if __name__ == "__main__":
    url = input("URL: ").strip()
    vi = VideoInfo(url)
    vi.get_video_infos()

    fmt = input("Video id: ").strip()
    vd = VideoDownloader(url, fmt)
    vd.download()
