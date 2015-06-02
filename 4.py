import re
import requests

leading = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nothing = "12345"
while 1:
	request = requests.get(leading+nothing)
	content = ''.join(request.text.split('\n'))
	nothing = "".join(re.findall(r'nothing is (\d+)',content))
	print nothing
	if nothing == "":
		print content
		break

nothing = "8022"
while 1:
	request = requests.get(leading+nothing)
	content = ''.join(request.text.split('\n'))
	nothing = "".join(re.findall(r'nothing is (\d+)',content))
	print nothing
	if nothing == "":
		print content
		break

