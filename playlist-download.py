import os
import yt_dlp

# Playlist URL
PLAYLIST_URL = "https://www.youtube.com/playlist?list=PL-tKrPVkKKE0kM18Sg5fqaZW1V2nidAeU" # jadi LPIC-1
# PLAYLIST_URL = "https://www.youtube.com/playlist?list=PL-tKrPVkKKE196tQGGunNbHVlBvqORiaV" # jadi LPIC-2
# PLAYLIST_URL = "https://www.youtube.com/playlist?list=PLx5i827-FDqPiLPjGxlUv3gjq7uCEVVfl" # in the mix playlist

# Output directory
OUTPUT_DIR = "LPIC-1" # jadi
# OUTPUT_DIR = "LPIC-2" # jadi
# OUTPUT_DIR = "in-the-mix-playlist"

# start of the video numbering (1-based index)
starter_video_number = 24

def download_playlist():
    global starter_video_number

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    ydl_opts = {
        # Adds index + title (e.g., 001 - Video Title.mp4)
        'outtmpl': os.path.join(OUTPUT_DIR, '%(playlist_index)03d - %(title)s.%(ext)s'),

        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',

        # IMPORTANT: allow playlist downloading
        'noplaylist': False,

        # Start from nth video (1-based index)
        'playliststart': starter_video_number,

        # Optional: ignore errors and continue
        'ignoreerrors': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([PLAYLIST_URL])
    
    starter_video_number += 1  # Increment for the next video in the playlist

if __name__ == "__main__":
    download_playlist()