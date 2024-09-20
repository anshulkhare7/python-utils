import os
import re
import sys

from googleapiclient.discovery import build

# Read the API key from environment variable
api_key = os.environ.get('YOUTUBE_API_KEY')

if not api_key:
    raise ValueError("Please set the YOUTUBE_API_KEY environment variable")

# Set up the YouTube API client
youtube = build('youtube', 'v3', developerKey=api_key)

def get_video_details(video_id):
    request = youtube.videos().list(
        part="contentDetails",
        id=video_id
    )
    response = request.execute()
    return response['items'][0]['contentDetails'] if response['items'] else None

def parse_duration(duration):
    match = re.match(r'PT(\d+H)?(\d+M)?(\d+S)?', duration)
    if not match:
        return 0
    
    hours = int(match.group(1)[:-1]) if match.group(1) else 0
    minutes = int(match.group(2)[:-1]) if match.group(2) else 0
    seconds = int(match.group(3)[:-1]) if match.group(3) else 0
    
    return hours * 3600 + minutes * 60 + seconds

def is_short(duration):
    # YouTube Shorts are typically 60 seconds or less
    return parse_duration(duration) <= 60

def get_playlist_titles(playlist_id):
    titles = []
    next_page_token = None

    while True:
        # Make the API request
        request = youtube.playlistItems().list(
            part='snippet',
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        response = request.execute()

        # Extract video details and filter out shorts
        for item in response['items']:
            video_id = item['snippet']['resourceId']['videoId']
            video_details = get_video_details(video_id)
            if video_details and not is_short(video_details['duration']):
                titles.append(item['snippet']['title'])

        # Check if there are more pages
        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    return titles

def main():
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <playlist_id>")
        sys.exit(1)

    playlist_id = sys.argv[1]
    video_titles = get_playlist_titles(playlist_id)

    # Print the titles
    for title in video_titles:
        print(title)

    # Save titles to a file
    with open('playlist_titles.txt', 'w', encoding='utf-8') as f:
        for title in video_titles:
            f.write(f"{title}\n")

    print(f"\nTitles of {len(video_titles)} regular videos have been saved to playlist_titles.txt")

if __name__ == "__main__":
    main()