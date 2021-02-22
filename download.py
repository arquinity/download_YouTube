from pytube import YouTube
import os

#crefitos
os.system("clear")
print("""\033[1;31m✞✞ ĆŘ€ĐƗŦØŞ ✞✞
GHOST ==> https://github.com/GH05T3-404/
ARQUINITY ==> https://github.com/arquinity/\n""")


# Digite o link do vídeo e o local que deseja salvar o video #
link = input("Digite o link do vídeo que deseja baixar ==>  ")
path = input("Digite o diretório que deseja salvar o vídeo ==>  ")
yt = YouTube(link)

# Mostra os detalhes do video #
os.system("clear")
print("=======INF============")
print("Título: ", yt.title)
print("Número de views: ", yt.views)
print("Tamanho do vídeo: ", yt.length, "segundos")
print("Avaliação do vídeo: ", yt.rating)
print("=======INF============")

# Usa a maior resolucao #
ys = yt.streams.get_highest_resolution()

# Começa o Download do vídeo #
print("Download iniciado")
print("Isso pode levar alguns minutos !!!")
ys.download(path)
print("Download completo!")