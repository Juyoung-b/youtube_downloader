import sys
import os
from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress

def download_video(url, output_path='.', audio_only=False, download_captions=False):
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        print(f"Title: {yt.title}")
        print(f"Length: {yt.length} seconds")

        if audio_only:
            stream = yt.streams.get_audio_only()
            print("Downloading audio file...")
            file_path = stream.download(output_path=output_path, filename_prefix="audio_")
            print(f"Audio download completed: {file_path}")
        else:
            stream = yt.streams.get_highest_resolution()
            print("Downloading video file...")
            file_path = stream.download(output_path=output_path)
            print(f"Video download completed: {file_path}")

        if download_captions:
            caption = yt.captions.get_by_language_code('en')
            if caption:
                caption_file = os.path.join(output_path, f"{yt.title}_captions.txt")
                with open(caption_file, 'w', encoding='utf-8') as f:
                    f.write(caption.generate_srt_captions())
                print(f"Captions downloaded: {caption_file}")
            else:
                print("No English captions available for this video.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def download_playlist(url, output_path='.', audio_only=False, download_captions=False):
    try:
        pl = Playlist(url)
        print(f"Playlist Title: {pl.title}")
        print(f"Number of videos: {len(pl.video_urls)}")

        for video_url in pl.video_urls:
            download_video(video_url, output_path, audio_only, download_captions)

    except Exception as e:
        print(f"An error occurred while processing the playlist: {str(e)}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <YouTube URL> [output path] [--audio-only] [--download-captions] [--playlist]")
        return

    url = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else '.'
    audio_only = '--audio-only' in sys.argv
    download_captions = '--download-captions' in sys.argv
    is_playlist = '--playlist' in sys.argv

    if is_playlist:
        download_playlist(url, output_path, audio_only, download_captions)
    else:
        download_video(url, output_path, audio_only, download_captions)

if __name__ == "__main__":
    main()
