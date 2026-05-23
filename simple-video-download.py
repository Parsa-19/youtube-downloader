import yt_dlp

counter = 0

def download_video(url):
    global counter
    counter += 1
    output_path = f'({str(counter)})_%(title)s.%(ext)s'
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # highest quality
        'outtmpl': output_path,
        'merge_output_format': 'mp4',          # final format
        'noplaylist': True,                   # only single video
        'quiet': False                        # show progress
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Downloaded: {url}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")



if __name__ == "__main__":

    target_url ="https://www.youtube.com/watch?v=I12FURDMCO0&list=PLx5i827-FDqPiLPjGxlUv3gjq7uCEVVfl&index=34&t=9s"
    download_video(target_url)