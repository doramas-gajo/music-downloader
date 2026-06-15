"""
Music Downloader

Downloader module.
"""

# Standard library imports
import os
import sys

# Third-party imports
import yt_dlp


def download(url: str, output_dir: str, quiet: bool = False) -> bool:
    """Downloads a song as MP3."""

    os.makedirs(output_dir, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'ffmpeg_location': os.path.dirname(os.path.abspath(__file__)),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': quiet,
        'no_warnings': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return True
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python downloader.py <URL>")
    else:
        url = sys.argv[1]
        output_dir = "downloads"
        print("Starting download...")
        download(url, output_dir)
        print("Download completed.")
