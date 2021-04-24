import pytube
link = input("Enter youtube video url: ")#"https://youtu.be/P8u8md-NiHM"
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download()
