def sort_matrix(matrix):
	all_numbers = []
	for row in matrix:
		for num in row:
			all_numbers.append(num)
	all_numbers.sort()
	k = 0
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			matrix[i][j] = all_numbers[k]
			k += 1
	return matrix

mat = [[5, 4], [1, 2]]
result = sort_matrix(mat)
for row in result:
	print(row)