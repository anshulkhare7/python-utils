import os
import sys

import requests
from youtube_transcript_api import YouTubeTranscriptApi

# Read the video ID from command-line arguments
if len(sys.argv) < 2:
    print("Please provide the YouTube video ID as a command-line argument.")
    sys.exit(1)

VIDEO_ID = sys.argv[1]
API_KEY = os.getenv('YOUTUBE_API_KEY')

def download_transcript():
    try:
        return YouTubeTranscriptApi.get_transcript(VIDEO_ID)
    except Exception as e:
        print(f"Error downloading transcript: {str(e)}")
        return None

def format_transcript(transcript):
    formatted = ""
    for entry in transcript:
        start_time = int(entry['start'])
        minutes, seconds = divmod(start_time, 60)
        hours, minutes = divmod(minutes, 60)
        timestamp = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        formatted += f"[{timestamp}] {entry['text']}\n"
    return formatted

def get_video_title(video_id):
    url = f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['items'][0]['snippet']['title']
    else:
        print(f'Error fetching video title: {response.status_code}')
        return None

def save_transcript(transcript, title):
    filename = f"{title}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(transcript)
    print(f'Transcript saved to {filename}')

# Call the function to download
transcript = download_transcript()

if transcript:
    print('Transcript downloaded successfully.')
    formatted_transcript = format_transcript(transcript)
    video_title = get_video_title(VIDEO_ID)
    if video_title:
        save_transcript(formatted_transcript, video_title)
    else:
        print('Failed to get video title. Saving with video ID.')
        save_transcript(formatted_transcript, VIDEO_ID)
else:
    print('Failed to download transcript.')