import sys
import zipfile
import re

nothing = "90052"
txt = ".txt"
while 1:
	zip = zipfile.ZipFile("/home/xiao/python_challenge/channel.zip")
	content = zip.read(nothing+txt)
	info = zip.getinfo(nothing+txt)
	sys.stdout.write(info.comment)
	nothing = "".join(re.findall(r'Next nothing is (\d+)',content))
	# print nothing
	if nothing == "":
		break