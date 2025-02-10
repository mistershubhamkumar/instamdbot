import youtube_dl
import requests

def download_song(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        return info_dict["id"] + ".mp3"

def download_video(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'downloads/%(id)s.%(ext)s',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        return info_dict["id"] + ".mp4"

def download_sticker(query):
    # Assuming a sticker search API is used
    url = f"https://api.tenor.com/v1/search?q={query}&key=API_KEY&limit=1"
    response = requests.get(url)
    sticker_url = response.json()['results'][0]['media'][0]['gif']['url']
    return sticker_url

def run(bot, message, args):
    if args.startswith("song "):
        song_url = args[5:]
        return download_song(song_url)
    elif args.startswith("video "):
        video_url = args[6:]
        return download_video(video_url)
    elif args.startswith("sticker "):
        sticker_query = args[8:]
        return download_sticker(sticker_query)
    else:
        return "❌ Invalid command. Use '.song <URL>', '.video <URL>', or '.sticker <query>'"
