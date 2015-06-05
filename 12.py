doc = open("evil2.gfx",'rb')
gfx = doc.read()
content = [binary for binary in gfx]
image = [],[],[],[],[]
for i in range(0,len(content),5):
	for j in range(5):
		image[j].append(content[i+j])
for k in range(5):
	output = open("image"+str(k)+".jpg",'wb')
	output.write("".join(image[k]))
doc.close()

