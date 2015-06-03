import Image,sys,re

oxygen = Image.open("oxygen.png")

output = [oxygen.getpixel((x,45)) for x in range(0,oxygen.size[0],7)]
message = [r for r,g,b,a in output if r==g==b]
chars = re.findall("\d+","".join(map(chr,message)))
integers = map(int,chars)
answer = "".join(map(chr,integers))
print answer