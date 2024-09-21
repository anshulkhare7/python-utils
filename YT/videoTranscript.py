import os
import sys

import requests
from youtube_transcript_api import YouTubeTranscriptApi

# Read the playlist ID from command-line arguments
if len(sys.argv) < 2:
    print("Please provide the YouTube playlist ID as a command-line argument.")
    sys.exit(1)

PLAYLIST_ID = sys.argv[1]
API_KEY = os.getenv('YOUTUBE_API_KEY')

def get_playlist_items(playlist_id):
    items = []
    next_page_token = None
    while True:
        url = f'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId={playlist_id}&key={API_KEY}'
        if next_page_token:
            url += f'&pageToken={next_page_token}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            items.extend(data['items'])
            next_page_token = data.get('nextPageToken')
            if not next_page_token:
                break
        else:
            print(f'Error fetching playlist items: {response.status_code}')
            return None
    return items

def download_transcript(video_id):
    try:
        return YouTubeTranscriptApi.get_transcript(video_id)
    except Exception as e:
        print(f"Error downloading transcript for video {video_id}: {str(e)}")
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

def save_transcript(transcript, title):
    # Remove any characters that are not allowed in filenames
    safe_title = ''.join(c for c in title if c.isalnum() or c in (' ', '.', '_')).rstrip()
    filename = f"{safe_title}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(transcript)
    print(f'Transcript saved to {filename}')

# Get all videos in the playlist
playlist_items = get_playlist_items(PLAYLIST_ID)

if playlist_items:
    print(f'Found {len(playlist_items)} videos in the playlist.')
    for item in playlist_items:
        video_id = item['snippet']['resourceId']['videoId']
        video_title = item['snippet']['title']
        print(f'Processing video: {video_title}')
        
        transcript = download_transcript(video_id)
        if transcript:
            formatted_transcript = format_transcript(transcript)
            save_transcript(formatted_transcript, video_title)
        else:
            print(f'Failed to download transcript for video: {video_title}')
else:
    print('Failed to retrieve playlist items.')