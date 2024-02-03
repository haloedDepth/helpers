# combine_video.py

## Overview

`combine_video.py` is a Python script designed to combine two videos side by side into a single video file. This script utilizes the MoviePy library, a powerful tool for video editing in Python. The script takes two input video files, resizes them to specified dimensions, and then combines them into one video, placing them side by side. The audio from the first video is retained in the final output.

## Requirements

-   Python 3.x
-   MoviePy library

To install MoviePy, run `pip install moviepy`.

## Usage

To use the script, you need to provide paths to two input video files and an output file path as command-line arguments. The syntax is as follows:


`python combine_video.py <video1_path> <video2_path> <output_path>` 

## Functionality

1.  **Loading Videos**: The script loads two video files provided by the user.
    
2.  **Resizing Videos**: The first video is resized to 1080x1080 pixels, and the second video is resized to 840x1080 pixels.
    
3.  **Combining Videos**: The two resized videos are combined side by side in a single frame.
    
4.  **Audio Handling**: The audio from the first video is used in the final video.
    
5.  **Output**: The script outputs a single video file that contains the two input videos playing side by side. The output video is encoded with 'libx264' video codec and 'aac' audio codec.
    

## Example


`python combine_video.py video1.mp4 video2.mp4 output.mp4` 

This command will take `video1.mp4` and `video2.mp4`, resize them, and combine them side by side into a new file called `output.mp4`.

# combine_video_reel.py

## Overview

`combine_video_reel.py` is a Python script for combining two videos into a single vertical (portrait mode) video file. This script is particularly useful for creating content formatted for platforms that favor vertical video formats, like Instagram Reels or TikTok. It uses the MoviePy library to handle video processing. The script stacks a 1080x1080 pixel video on top of a 1080x840 pixel video, resulting in a final video of 1080x1920 pixels, ideal for vertical formats.

## Requirements

-   Python 3.x
-   MoviePy library

To install MoviePy, use `pip install moviepy`.

## Usage

Run the script with three command-line arguments: the paths to the first and second input video files, and the path for the output video file. The syntax is:



`python combine_video_reel.py <video1_path> <video2_path> <output_path>` 

## Functionality

1.  **Loading Videos**: Loads two video files based on user-provided paths.
    
2.  **Resizing Videos**: Resizes the first video to 1080x1080 pixels and the second video to 1080x840 pixels.
    
3.  **Combining Videos**: Stacks the first video above the second video, aligning them vertically.
    
4.  **Audio Handling**: Uses the audio from the first video in the final output.
    
5.  **Output**: Produces a single 1080x1920 pixel video file, perfect for vertical video platforms. The output video uses 'libx264' video codec and 'aac' audio codec.
    

## Example



`python combine_video_reel.py video1.mp4 video2.mp4 output.mp4` 

In this example, `video1.mp4` and `video2.mp4` are resized and combined into a vertical video format saved as `output.mp4`.