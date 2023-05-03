from pytube import YouTube
from GetAllData import GetAllVideo
from threading import Thread
import os, json
from traceback import format_exc

def clean():
    os.system("cls")

def DownloadVideo(id = "o5wC0QqqN1c"):
    try:
        print("Инициализация нового видео")
        yt = YouTube('https://www.youtube.com/watch?v='+id, use_oauth=True, allow_oauth_cache=True)
        yt.streams.filter(file_extension='mp4')
        stream = yt.streams.get_by_resolution("720p")
        stream.download()
    except:
        print(format_exc())
        try: DownloadVideo(id)
        except: pass
    PB.value += 1

class ProgressBar():
    def __init__(self, end:int) -> None:
        self.value = 0
        self.__end = end
        self.__LastValue = -1
    def UpdateProgressBar(self):
        clean()
        print(f"{self.value}/{self.__end}|{round(self.value / self.__end*100)}%")
    def Loop(self):
        global ChId
        self.UpdateProgressBar()
        with open("data", "w", encoding="utf-8") as file:
            json.dump([PB.value, ChId], file)
ChId = input("id youtube канала (пусто - для продолжения предидущей операции) ")
Re = False
if ChId == "":
    with open("data", "r", encoding="utf-8") as file:
        ChId = json.load(file)[1]
    Re = True
AllVideo, AllVideoCount = GetAllVideo(ChId, Re)
PB = ProgressBar(AllVideoCount)
PB.value = AllVideoCount - len(AllVideo)
for id in AllVideo:
    DownloadVideo(id)
    PB.Loop()