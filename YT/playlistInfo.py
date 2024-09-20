import os
import sys

from googleapiclient.discovery import build

# Read the API key from environment variable
api_key = os.environ.get('YOUTUBE_API_KEY')

if not api_key:
    raise ValueError("Please set the YOUTUBE_API_KEY environment variable")

# Set up the YouTube API client
youtube = build('youtube', 'v3', developerKey=api_key)

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

        # Extract video titles
        for item in response['items']:
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

    print(f"\nTitles have been saved to playlist_titles.txt")

if __name__ == "__main__":
    main()