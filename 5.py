import pickle
import requests
import sys

request = requests.get("http://www.pythonchallenge.com/pc/def/banner.p")
content = pickle.loads(request.text)

for row in content:
	for column in row:
		for i in range(column[1]):
			sys.stdout.write(column[0])	
	sys.stdout.write("\n")
		
# for j in content:
	# print "".join([i[1] * i[0] for i in j])