from pytube import Playlist
from pytube import YouTube

down = input(" v:to download video \n p:to download playlist \n ")
if ( down == "v" ):
    link = input("Video link : ")
    video = YouTube(link)
    print(f"Video Title :\n{video.title}\n----*-----*----------* ")
    print(f"Video description :\n{video.description}\n----*-----*----------* ")
    print(f"Video views :\n{video.views}\n----*-----*----------* ")
    print(f"Video captions :\n{video.captions}\n----*-----*----------* ")
    for stream in video.streams:
        print(stream)
        def finish():
            print("Done")
            video.streams.get_highest_resolution().download(output_path="E:/")
            video.register_on_complete_callback(finish())

if ( down == "p" ):
    playlist_link = input("Playlist link : ")
    Playlist=Playlist(playlist_link)
    for video in Playlist.videos:
            video.streams.get_highest_resolution().download(output_path="E:/")
            video.register_on_complete_callback(finish())

