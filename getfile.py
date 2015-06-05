import urllib

print "Enter a file name:",
filename = raw_input()

urllib.urlretrieve("http://huge:file@www.pythonchallenge.com/pc/return/"+filename, filename)