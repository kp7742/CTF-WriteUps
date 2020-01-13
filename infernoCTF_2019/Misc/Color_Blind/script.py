from PIL import Image

im = Image.open('colorblind.png') 
pix = im.load()
print(im.size)  


for x in range(im.size[0]):
	for y in range(im.size[1]):
		for z in range(3):
			print(chr(pix[x,y][z]), end='')