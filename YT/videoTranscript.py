import argparse
import os
import sys

import requests
from youtube_transcript_api import TranscriptsDisabled, YouTubeTranscriptApi

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
        # First, try to get the English transcript
        return YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
    except TranscriptsDisabled:
        print(f"Transcripts are disabled for video {video_id}")
        return None
    except Exception as e:
        if "No transcripts were found" in str(e):
            print(f"No English transcript found for video {video_id}. Trying other languages...")
            try:
                # If English is not available, get a list of available transcripts
                transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
                
                # Try to get the transcript in any available language
                for transcript in transcript_list:
                    return transcript.fetch()
                
                print(f"No transcripts found in any language for video {video_id}")
                return None
            except Exception as inner_e:
                print(f"Error fetching transcript for video {video_id}: {str(inner_e)}")
                return None
        else:
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
    safe_title = ''.join(c for c in title if c.isalnum() or c in (' ', '.', '_')).rstrip()
    filename = f"{safe_title}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(transcript)
    print(f'Transcript saved to {filename}')

def log_missing_transcript(title):
    with open('missingTranscript.log', 'a', encoding='utf-8') as f:
        f.write(f"{title}\n")
    print(f'Logged missing transcript for: {title}')

def process_video(video_id, video_title):
    print(f'Processing video: {video_title}')
    transcript = download_transcript(video_id)
    if transcript:
        if isinstance(transcript[0], dict) and 'text' in transcript[0]:
            formatted_transcript = format_transcript(transcript)
        else:
            # Handle case where transcript might be in a different format
            formatted_transcript = "\n".join([entry for entry in transcript])
        save_transcript(formatted_transcript, video_title)
    else:
        print(f'Failed to download transcript for video: {video_title}')
        log_missing_transcript(video_title)

def get_video_title(video_id):
    url = f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'items' in data and data['items']:
            return data['items'][0]['snippet']['title']
    print(f"Couldn't fetch title for video {video_id}")
    return f"Video_{video_id}"

def main(args):
    if args.playlist:
        playlist_items = get_playlist_items(args.playlist)
        if playlist_items:
            print(f'Found {len(playlist_items)} videos in the playlist.')
            for item in playlist_items:
                video_id = item['snippet']['resourceId']['videoId']
                video_title = item['snippet']['title']
                process_video(video_id, video_title)
        else:
            print('Failed to retrieve playlist items.')
    elif args.video:
        video_id = args.video
        video_title = get_video_title(video_id)
        process_video(video_id, video_title)
    else:
        print("Please provide either a playlist ID or a video ID.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download YouTube video transcripts")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-p', '--playlist', help="YouTube playlist ID")
    group.add_argument('-v', '--video', help="YouTube video ID")
    args = parser.parse_args()
    main(args)