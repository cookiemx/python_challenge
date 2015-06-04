import Image

cave = Image.open("cave.jpg")
nsize = [ edge / 2 for edge in cave.size]
odd = even = Image.new('RGB',nsize)

for row in range(cave.size[0]):
	for column in range(cave.size[1]):
		if row+column / 2 == 1:
			odd.putpixel((row/2,column/2),cave.getpixel((row,column)))
		else:
			even.putpixel((row/2,column/2),cave.getpixel((row,column)))
			
odd.save('odd.jpg')
even.save('even.jpg')