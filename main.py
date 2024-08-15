import yt_dlp
import os


def download_youtube_video(url, output_path='.'):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',  # Download the best audio format
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),  # File name template
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',  # Convert video to audio
                'preferredcodec': 'mp3',  # Set preferred audio format
                'preferredquality': '192',  # Set audio quality
            }],
        }

        # Create a YT-DLP object
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading from {url}...")
            ydl.download([url])
            print("Download complete.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")

    save_in_current_dir = input("Save in the current directory? [Y/n]: ").strip().lower()

    if save_in_current_dir == 'n':
        output_directory = input("Enter the directory path where you want to save the file: ").strip()
        # Ensure the directory exists
        if not os.path.isdir(output_directory):
            print(f"Directory {output_directory} does not exist. Exiting.")
            exit(1)
    else:
        output_directory = '.'

    download_youtube_video(video_url, output_directory)
