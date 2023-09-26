# vamos importar a biblioteca e pedir para o usuario colar o link do video desejado
# vamos definir funções para download, de low,medium e high quality 

from pytube import YouTube

link=input('Paste link from video here:  ')
url=link
video= YouTube(url)
#stream= video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
stream=video.streams.get_highest_resolution()
#print(str(stream))