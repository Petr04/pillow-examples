from PIL import Image, ImageDraw

def merge(images, bg=tuple([255])*3):
	pixs = [i.load() for i in images]
	sizes = [i.size for i in images]
	print(sizes)

	new_size = []
	for pair in zip(*sizes):
		new_size.append(max(pair))

	new = Image.new('RGB', new_size, bg)
	draw = ImageDraw.Draw(new)
	new_pix = new.load()

	for pix, size in zip(pixs, sizes):
		print(size)
		for i in range(size[0]):
			for j in range(size[1]):
				print(i, j)

				new_color = []
				for n, c in enumerate(pix[i, j]):
					new_color.append((c + new_pix[i, j][n]) // 2)

				new_color = tuple(new_color)

				draw.point((i, j), new_color)

	return new

images = [Image.open('examples/{}'.format(i)) for i in ('1.jpg', '2.jpg')]

merge(images).show()
