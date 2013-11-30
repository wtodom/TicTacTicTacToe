import curses

class TicTacTicTacToe:

	def __init__(self):
		self.q1 = [[5,2], [5,10], [5,18], [9,2], [9,10], [9,18], [13,2], [13,10], [13,18]]
		self.q2 = [[5,4], [5,12], [5,20], [9,4], [9,12], [9,20], [13,4], [13,12], [13,20]]
		self.q3 = [[5,6], [5,14], [5,22], [9,6], [9,14], [9,22], [13,6], [13,14], [13,22]]
		self.q4 = [[6,2], [6,10], [6,18], [10,2], [10,10], [10,18], [14,2], [14,10], [14,18]]
		self.q5 = [[6,4], [6,12], [6,20], [10,4], [10,12], [10,20], [14,4], [14,12], [14,20]]
		self.q6 = [[6,6], [6,14], [6,22], [10,6], [10,14], [10,22], [14,6], [14,14], [14,22]]
		self.q7 = [[7,2], [7,10], [7,18], [11,2], [11,10], [11,18], [15,2], [15,10], [15,18]]
		self.q8 = [[7,4], [7,12], [7,20], [11,4], [11,12], [11,20], [15,4], [15,12], [15,20]]
		self.q9 = [[7,6], [7,14], [7,22], [11,6], [11,14], [11,22], [15,6], [15,14], [15,22]]

		self.marks = ["X", "O"]
		self.player = 0  # this will be used as the index of the above list to place marks

		# default these to a zero.
		# change to appropriate player value (from above) when noventile is won.
		self.captured_nontiles = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

	def main(self, stdscr):
		# Clear screen
		stdscr.clear()

		self.setup(stdscr)

		x = 2
		y = 5
		stdscr.move(y, x)

		while True:
			key = stdscr.getkey()
			if key == "x":
				break
			elif key == "r":
				self.setup(stdscr)
				x = 2
				y = 5
				stdscr.move(y, x)
			elif key == "KEY_UP":
				if y > 5:
					y -= 1
					if y == 8 or y == 12:
						y -= 1
					stdscr.move(y, x)
					stdscr.refresh()
			elif key == "KEY_DOWN":
				if y < 15:
					y += 1
					if y == 8 or y == 12:
						y += 1
					stdscr.move(y, x)
					stdscr.refresh()
			elif key == "KEY_LEFT":
				if x > 2:
					x -= 2
					if x == 8 or x == 16:
						x -= 2
					stdscr.move(y, x)
					stdscr.refresh()
			elif key == "KEY_RIGHT":
				if x < 22:
					x += 2
					if x == 8 or x == 16:
						x += 2
					stdscr.move(y, x)
					stdscr.refresh()
			elif key == " ":
				if stdscr.instr(1) == b"-":
					stdscr.addstr(self.marks[self.player])
					self.player = not self.player
					y, x = self.translate(y, x)
					stdscr.move(y, x)
					stdscr.refresh()
				else:
					pass
			else:
				pass

	def translate(self, y, x):
		loc = [y, x]
		if loc in self.q1:
			return 6, 4
		elif loc in self.q2:
			return 6, 12
		elif loc in self.q3:
			return 6, 20
		elif loc in self.q4:
			return 10, 4
		elif loc in self.q5:
			return 10, 12
		elif loc in self.q6:
			return 10, 20
		elif loc in self.q7:
			return 14, 4
		elif loc in self.q8:
			return 14, 12
		else:  # if loc in q9:
			return 14, 20

	def setup(self, stdscr):
		grid ="""
┌-------┬-------┬-------┐
| - - - | - - - | - - - |
| - - - | - - - | - - - |
| - - - | - - - | - - - |
├-------|-------|-------┤
| - - - | - - - | - - - |
| - - - | - - - | - - - |
| - - - | - - - | - - - |
├-------|-------|-------┤
| - - - | - - - | - - - |
| - - - | - - - | - - - |
| - - - | - - - | - - - |
└-------┴-------┴-------┘"""

		x = y = 0

		stdscr.addstr(y, x, "Use the arrow keys to move the cursor.")
		y += 1
		stdscr.addstr(y, x, "Press the spacebar to place your mark.")
		y += 1
		stdscr.addstr(y, x, "Press 'r' to reset the game.")
		y += 1
		stdscr.addstr(y, x, "Press 'x' to quit.")
		y += 1
		stdscr.addstr(grid)


if __name__ == '__main__':
	game = TicTacTicTacToe()
	curses.wrapper(game.main)