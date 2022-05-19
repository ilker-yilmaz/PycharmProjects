from pytube import YouTube, Playlist


#function takes youtube object as argument
def video_Info(yt):
    print("Title: ",yt.title)
    print("total length: ",yt.length," seconds")
    print("total views: ",yt.views)
    print("is age restricted: ",yt.age_restricted)
    print("video rating ",round(yt.rating))
    print("thumbnail url: ",yt.thumbnail_url)

link="https://www.youtube.com/watch?v=ysi8FQr5GFo"
yt=YouTube(link) ## create youtube object

#call the function
video_Info(yt)
#


def download_video(yt):
    #filter mp4 streams from object
    my_streams = yt.streams.filter(file_extension="mp4", only_video=True)
    for streams in my_streams:
        #print itag, resolution on which codec format of mp4 streams
        print(f"Video itag: {streams.itag} Resolution: {streams.resolution}")

    #enter the itag value of resoluton on which you want to download video
    input_itag = input("Enter itag value: ")
    #get video using itag value
    video=yt.streams.get_by_itag(input_itag)

    #finally download the youtube video...
    video.download()
    print("video is downloading as",yt.title+" .mp4")

link = "https://www.youtube.com/watch?v=ysi8FQr5GFo"
yt = YouTube(link)  ## create youtube object
# # call the function
download_video(yt)


def download_Playlist(p):
    #print playlist title...
    print(p.title)
    #get videos of playlist..
    for video in p.videos:
        try:
            #download all videos in best resolution
            video.streams.first().download(video.title)
        except Exception as e:
            print(e.tyoe(e))
    print("playlist is downloaded")

link = "https://www.youtube.com/playlist?list=PLf62ntDK8WLmSiy-Sq2lKNI0hUM6zRwbC"
p = Playlist(link)
#download_Playlist(p)
