from PIL import Image, ImageDraw

def bw(pix, draw, w, h):
	for i in range(w):
		for j in range(h):
			print((i, j))

			mid = sum(pix[i, j]) // 3
			draw.point((i, j), tuple([mid])*3)

def invert(pix, draw, w, h):
	for i in range(w):
		for j in range(h):
			print((i, j))

			draw.point((i, j), tuple(map(lambda color: 255-color, pix[i, j])))

image = Image.open('example.jpg')
draw = ImageDraw.Draw(image)

w, h = image.size
pix = image.load()

invert(pix, draw, w, h)
image.show()
