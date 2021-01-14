from pytube import YouTube

YouTube('https://www.youtube.com/watch?v=D2Tsh4oH9Zc').streams.first().download()