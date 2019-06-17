from PIL import Image, ImageDraw

import random

from cut_color import cut_color

def gray(pix, draw, w, h):
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

def bw(pix, draw, w, h):
	for i in range(w):
		for j in range(h):
			print((i, j))

			if sum(pix[i, j]) // 3 <= 255 // 2:
				draw.point((i, j), tuple([0])*3)
			else:
				draw.point((i, j), tuple([255])*3)

def noise(pix, draw, w, h, rng):
	for i in range(w):
		for j in range(h):
			print((i, j))

			new = []
			diff = random.randint(-(rng // 2), rng // 2 + (rng % 2))
			for c in pix[i, j]:
				new.append(c + diff)

			new = cut_color(new)

			draw.point((i, j), new)

def mirror(pix, draw, w, h):
	for i in range(w):
		for j in range(h):
			print((i, j))

			draw.point((w-i, j), pix[i, j])

def diff(pix, draw, w, h, color):
	for i in range(w):
		for j in range(h):
			print((i, j))

			new = []
			for n, c in enumerate(pix[i, j]):
				new.append(c + color[n])

			new = cut_color(new)

			draw.point((i, j), new)

image = Image.open('examples/1.jpg')
new = Image.new('RGB', image.size)
draw = ImageDraw.Draw(new)

w, h = image.size
pix = image.load()

diff(pix, draw, w, h, (-100, -100, -100))
new.show()
