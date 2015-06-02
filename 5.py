import pickle
import requests

request = requests.get("http://www.pythonchallenge.com/pc/def/banner.p")
content = pickle.loads(request.text)

for row in content:
	for column in row:
		for i in range(column[1]):
			print column[0],