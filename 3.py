import re
import requests

request = requests.get("http://www.pythonchallenge.com/pc/def/equality.html")
content = ''.join(request.text.split('\n')[22:-2])

words = "".join(re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',content))

print words
