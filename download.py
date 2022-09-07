import pytube
import moviepy.editor
import os
import re

def download_musica(link_video,pasta_arquivo):
    link = pytube.YouTube(link_video)
    diretorio = pasta_arquivo
    download = link.streams.filter(only_audio = True).first().download(diretorio)
    for file in os.listdir(diretorio):
        if re.search("mp4",file):
            mp4_path = os.path.join(diretorio,file)
            mp3_converte = os.path.join(diretorio,os.path.splitext(file)[0]+".mp3")
            arquivo_mp3 = moviepy.editor.AudioFileClip(mp4_path)
            arquivo_mp3.write_audiofile(mp3_converte)
            os.remove(mp4_path)

def download_video(link_video,pasta_arquivo):
    link = link_video
    diretorio = pasta_arquivo
    youtube = pytube.YouTube(link)
    download = youtube.streams.filter(progressive = True, file_extension="mp4").first().download(diretorio)

