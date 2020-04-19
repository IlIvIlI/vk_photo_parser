from urllib import request
import time
import vk_api
from datetime import datetime

vk = vk_api.VkApi(token="insert_token_here") #replace insert_token_here with user's token

start_from = "0"

peer_id = int(input("Input ID: "))

while True:

	line = vk.method('messages.getHistoryAttachments', {'peer_id':peer_id, "media_type":"photo", "count":200, "start_from":start_from})
	try:
		start_from = line["next_from"]
	except KeyError:
		print("Photos downloaded!")
		exit(0)
	print(start_from)
	line = str(line)

	last_bracket = line.rfind("]")

	while last_bracket != -1:
		last_jpg = line.rfind(".jpg", 1, last_bracket)
		last_https = line.rfind("https://", 1, last_jpg)
		link = line[last_https : (last_jpg + 4)]
		last_slash = link.rfind("/")
		request.urlretrieve(link, (link[last_slash + 1 : -1] + "g"))
		last_bracket = line.rfind("]", 1, last_https)
