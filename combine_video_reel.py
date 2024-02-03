import sys
from moviepy.editor import VideoFileClip, concatenate_videoclips

def stack_videos(video1_path, video2_path, output_path):
    # Load the videos
    clip1 = VideoFileClip(video1_path)
    clip2 = VideoFileClip(video2_path)

    # Resize the videos to the desired sizes
    clip1_resized = clip1.resize(newsize=(1080, 1080))
    clip2_resized = clip2.resize(newsize=(1080, 840))

    # Stack the clips vertically
    final_clip = concatenate_videoclips([clip1_resized, clip2_resized], method="compose")

    # Set the audio of the first clip to the final clip
    final_clip = final_clip.set_audio(clip1.audio)

    # Write the output video file
    final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <video1_path> <video2_path> <output_path>")
        sys.exit(1)

    video1_path, video2_path, output_path = sys.argv[1], sys.argv[2], sys.argv[3]
    stack_videos(video1_path, video2_path, output_path)
