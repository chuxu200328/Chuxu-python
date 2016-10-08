board = [[0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0],
		 [0,0,0,0,0,0,0,0]]

def check(row ,col):
	valid = False

	#上边
	if row > 7 or col > 7:
		return False
	
	for i in range(row):
		if board[i][col] == 1:
			return False  
	#左上
	if row == col:
		for i in range(row):
			if board[i][i]:
				return False
	elif row > col:
		for i in range(col):
				if board[row - i - 1][col - i - 1]:
					return False
	else:
		for i in range(row):
				if board[row - i - 1][col - i - 1]:
					return False

	#右上
	t_range = max(row,col)
	for i in range(t_range):
		t_row = row - i - 1
		t_col = col + i + 1
		if t_col > 7 or t_row > 7:
			break
		elif board[t_row][t_col]:
			return False
	
	return True
def find(board, row):
	col_position = -1

	for i in range(len(board[row])):
		if board[row][i] == 1:
			return i

	return -1

current_row = 0
current_col = 0

while True:

	if check (current_row, current_col) == True:
		board[current_row][current_col] = 1
		current_row += 1
		current_col = 0

		if current_row == 8:
			break

	else:
		current_col += 1

		if current_col > 7:
			current_row -= 1
			
			t_col = find(board, current_row)
			
			board[current_row][t_col] = 0
			
			current_col =t_col + 1

			
for i in board:
	print(i)