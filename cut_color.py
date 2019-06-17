def cut_color(color):
	new = []

	for c in color:
		if c not in range(0, 256):
			new.append((255, 0)[c < 0])
		else:
			new.append(c)

	return tuple(new)

if __name__ == '__main__':
	print(cut_color( tuple(map(int, input().split())) ))
