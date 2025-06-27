def create_pattern(rows, cols):
	mat = [["" for _ in range(cols)] for _ in range(rows)]
	top = 0
	bottom = rows - 1
	left = 0
	right = cols - 1
	char = "x"
	while top <= bottom and left <= right:
		for i in range(left, right + 1):
			mat[top][i] = char
		top += 1
		for i in range(top, bottom + 1):
			mat[i][right] = char
		right -= 1
		if top <= bottom:
			for i in range(right, left - 1, -1):
				mat[bottom][i] = char
			bottom -= 1
		if left <= right:
			for i in range(bottom, top - 1, -1):
				mat[i][left] = char
			left += 1
		if char == "x":
			char = "0"
		else:
			char = "x"
	return mat
pattern = create_pattern(5, 6)
for row in pattern:
	print("".join(row))