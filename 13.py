import xmlrpclib

url = "http://www.pythonchallenge.com/pc/phonebook.php"

object = xmlrpclib.ServerProxy(url)
print object.system.listMethods()

help = object.system.methodHelp("phone")
print help

print object.phone("Bert")

