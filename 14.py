import Image

wire = Image.open("wire.png",'r')
around = Image.new(wire.mode,(100,100))

xmin,xmax = 0,99
ymin,ymax = 0,99

pos = [0,0]
count = 0

while not (xmin + 1 == xmax and ymin + 1 == ymax):
	for x in range(xmin,xmax+1):
		pos[0] = x
		count+=1
		around.putpixel(pos,wire.getpixel((count,0)))
	ymin +=1
	for y in range(ymin,ymax+1):
		pos[1] = y
		count+=1
		around.putpixel(pos,wire.getpixel((count,0)))
	xmax -=1
	for x in range(xmax,xmin-1,-1):
		pos[0] = x
		count+=1
		around.putpixel(pos,wire.getpixel((count,0)))
	ymax -=1
	for y in range(ymax,ymin-1,-1):
		pos[1] = y
		count+=1
		around.putpixel(pos,wire.getpixel((count,0)))
	xmin+=1
	
around.save('around.jpg')
	