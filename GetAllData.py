import scrapetube
from traceback import format_exc
import json

def GetAllVideo(channel_id:str, Re):
	try:
		DropVideo = 0
		if Re:
			with open("data", "r", encoding="utf-8") as file:
				data = json.load(file)
			channel_id = data[1]
			DropVideo = data[0]
		videos = scrapetube.get_channel(channel_id)
		NList = []
		for video in videos:
			NList.append(video['videoId'])
		All = len(NList)
		for i in range(DropVideo):
			NList.pop(0)
		return NList, All
	except: print(format_exc())