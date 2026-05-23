import yt_dlp

def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',

        'outtmpl': '%(title)s.%(ext)s',

        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'flac',
            },
            {
                'key': 'EmbedThumbnail',
            },
            {
                'key': 'FFmpegMetadata',
            }
        ],

        'writethumbnail': True,

        'postprocessor_args': [
            '-ar', '48000'
        ],

        'quiet': False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    youtube_url = "https://www.youtube.com/watch?v=foRjsU8OXS8" 
    download_audio(youtube_url.strip())