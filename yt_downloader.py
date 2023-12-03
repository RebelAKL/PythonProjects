from pytube import YouTube
video_url = 'link'
yt = YouTube(video_url)
desired_resolution = '480p'
video_stream = yt.streams.filter(res=desired_resolution, progressive=True).first()
download_path = '/path/to/download/directory'
video_stream.download(output_path=download_path)
print('Download complete!')