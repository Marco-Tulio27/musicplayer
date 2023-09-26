# vamos importar a biblioteca e pedir para o usuario colar o link do video desejado
# vamos definir funções para download, de low,medium e high quality 

from pytube import YouTube
class video:
    def __init__(self):
        self.link=input('Paste link from video here:  ')
        self.url=self.link
        print('Selecione a sua opção de download: \n alta definição 1 \n baixa resolução 2 ')
        self.resolucao= input('Opção: ') 
    def download(self):   
        if self.resolucao == '1':
            video= YouTube(self.url)
            stream= video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
            stream.download()
        if self.resolucao == '2':
            video=YouTube(self.url)
            stream=video.streams.first().download()
            stream.download()
    
baixar = video()
baixar.download()

# MP4 (H.264)
# WEBM (VP9)
# 3GP
# FLV

#https://www.youtube.com/watch?v=_TV7MUfZZNs