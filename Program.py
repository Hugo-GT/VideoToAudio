from moviepy import VideoFileClip
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def extract_audio(video_path):
    # Generate the output path by replacing the video extension with .mp3
    base_name = os.path.splitext(video_path)[0]  # Get the file name without extension
    output_audio_path = base_name + ".mp3"

    try:
        video = VideoFileClip(video_path)
        video.audio.write_audiofile(output_audio_path)
        print(f"Audio extracted successfully to {output_audio_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Initialize tkinter and hide the root window
    Tk().withdraw()
    print("Please select the video file...")
    
    # Open file dialog to select the video file
    video_file = askopenfilename(
        title="Select Video File",
        filetypes=[("Video Files", "*.mp4;*.mkv;*.avi;*.mov;*.flv;*.wmv;*.webm"), ("All Files", "*.*")]
    )

    if video_file:
        extract_audio(video_file)
    else:
        print("No file was selected.")
