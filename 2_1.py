import requests

request = requests.get("http://www.pythonchallenge.com/pc/def/ocr.html")
content = ''.join(request.text.split('\n')[37:-3])

dic = {}
for i in content:
	dic[i] = dic.get(i,0)+1
	
print dic

for x in sorted(dic.keys()):
    print x, dic[x]