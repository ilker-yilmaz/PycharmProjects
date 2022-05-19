from pytube import YouTube, Channel, Playlist

link="https://www.youtube.com/watch?v=uIxOTMecMUc"
video=YouTube(link)
stream=video.streams.get_highest_resolution()
stream.download("C:/Users/eymen/Desktop")
# stream_audio=video.streams.get_audio_only()
# stream_audio.download("C:/Users/eymen/Desktop")

# p = Playlist('https://www.youtube.com/playlist?list=PLf62ntDK8WLmb6ve-frwiZgBc3oZtoTkG')
# #print(f'Downloading: {p.title}')
# #Downloading: Python Tutorial for Beginers (For Absolute Beginners)
# for video in p.videos:
#     #print(f'Downloading: {video.title}')
#     video.streams.first().download()("C:/Users/eymen/Desktop")
#     #print(f'Downloaded: {video.title}')

# c = Channel('https://www.youtube.com/channel/UCkkgrhDCJheXQNIFqUVw0_g')
# print(f'Downloading videos by: {c.channel_name}')
# #Downloading videos by: ProgrammingKnowledge
# for video in c.videos:
#     print(f'Downloading videos by: {c.channel_name}')
#     video.streams.get_highest_resolution().download("E:/sadievrenseker")
# for url in c.video_urls[:300]:
#     print(url)
