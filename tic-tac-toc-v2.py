class tik_tak_tok:

	def __init__(self):
		self.board = [" | | ", 
					   "-----", 
					   " | | ", 
					   "-----", 
					   " | | "]
		self.step = 0
		self.all_symbol = ["O", "X"]
		self.symbol = "X"
		self.empty = [(3,1), (3,3), (3,2), (1,3), (1,1), (1,2), (2,3), (2,1), (2,2)]

	def draw(self):
		for row in range(5):
			print(self.board[row])

	def put(self, symbol, x, y):
		def cal(index):
			if index == 1:
				return 0				
			elif index == 2:
				return 2
			elif index == 3:
				return 4		

		if y == 1:
			self.board[cal(x)] = symbol + self.board[cal(x)][1:]
		elif y == 2:
			self.board[cal(x)] = self.board[cal(x)][:2] + symbol + self.board[cal(x)][3:]
		elif y == 3:
			self.board[cal(x)] = self.board[cal(x)][:4] + symbol
		else:
			pass

		self.step += 1
		self.empty.remove((x, y))

		self.draw()
		

	def has_won(self, symbol):
		def win_row(symbol):
			# if all(self.board[0][0] == )
			for row in (0, 2, 4):
				if self.board[row][0] == symbol \
				 and self.board[row][2] == symbol \
				 and self.board[row][4] == symbol:
					return True
			return False

		def win_col(symbol):		
			if self.board[0][0] == symbol and self.board[2][0] == symbol and self.board[4][0] == symbol:
				return True
			if self.board[0][2] == symbol and self.board[2][2] == symbol and self.board[4][2] == symbol:
				return True
			if self.board[0][4] == symbol and self.board[2][4] == symbol and self.board[4][4] == symbol:
				return True
			return False

		def win_cor(symbol):
			if self.board[0][0] == symbol \
				and self.board[2][2] == symbol \
				and self.board[4][4] == symbol:
				return True
			if self.board[0][4] == symbol \
				and self.board[2][2] == symbol \
				and self.board[4][0] == symbol:
				return True 
			return False

		if win_row(symbol) or win_col(symbol) or win_cor(symbol):
			print("winner is " + symbol)
			return True
		else:
			return False

	def is_full(self):
		for row in (0, 2, 4):
			# print("row:  " + self.board[row] + "  " + str(row))
			if " " in self.board[row]:
				# print("row" + self.board[row])
				return False
		return True

	def play(self):
		valid = ('1', '2', '3')
		while not self.is_full():
			x = 4
			y = 4
			while (int(x), int(y)) not in self.empty:
				while x not in valid:
					x = input("Input Row (Please choose from (1, 2, 3):")
				while y not in valid:
					y = input("Input Column (Please choose from (1, 2, 3):")
				if (int(x), int(y)) not in self.empty:
					print("This place has already been taken, please choose another one!")
					x = 4
					y = 4

			self.put("X", int(x), int(y))

			import random
			s = random.sample(self.empty, 1)
			print(s)
			self.put("O", s[0][0], s[0][1])

			
			if self.has_won("X"):
				break

			if self.has_won("O"):
				break

playBoard = tik_tak_tok()
print(".................")
playBoard.draw()
print(".................")
# playBoard.put(playBoard.all_symbol[playBoard.step%2], 1, 1)
# print(playBoard.has_won(playBoard.all_symbol[(playBoard.step + 1)%2]))
# # print(playBoard.is_full())
# playBoard.put(playBoard.all_symbol[playBoard.step%2], 1, 2)
# # print(playBoard.is_full())
# playBoard.put(playBoard.all_symbol[playBoard.step%2], 1, 3)
# # print(playBoard.is_full())
# playBoard.put(playBoard.all_symbol[playBoard.step%2], 2, 1)
# # print(playBoard.is_full())
# playBoard.put(playBoard.all_symbol[playBoard.step%2], 2, 2)
# # print(playBoard.is_full())
# playBoard.put(playBoard.all_symbol[playBoard.step%2], 2, 3)
# # print(playBoard.is_full())
# playBoard.put(playBoard.all_symbol[playBoard.step%2], 3, 1)
# print(playBoard.is_full())
# playBoard.put(playBoard.all_symbol[playBoard.step%2], 3, 2)
# print(playBoard.is_full())
# playBoard.put(playBoard.all_symbol[playBoard.step%2], 3, 3)
# print(playBoard.is_full())

# if playBoard.has_won(playBoard.symbol):
# 	print("True")
# else:
# 	print("False")
playBoard.play()