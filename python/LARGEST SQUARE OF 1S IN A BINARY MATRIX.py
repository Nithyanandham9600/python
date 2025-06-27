def max_square(matrix):
	rows = len(matrix)
	cols = len(matrix[0])
	max_size = 0
	dp = [[0] * cols for _ in range(rows)]
	for i in range(rows):
		for j in range(cols):
			if matrix[i][j] == 1:
				if i == 0 or j == 0:
					dp[i][j] = 1
				else:
					dp[i][j] = 1 + min(
						dp[i-1][j],
						dp[i][j-1],
						dp[i-1][j-1]
					)
				max_size = max(max_size, dp[i][j])
	print("Biggest square size:", max_size)
mat = [ [0, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 0]
]
max_square (mat)