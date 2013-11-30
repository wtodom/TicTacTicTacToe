import curses


marks = ["-", "X", "O"]
player = 1  # this will be used as the index of the above list to place marks
HEIGHT = 12
WIDTH = 24

# default these to a zero.
# change to appropriate player value (from above) when noventile is won.
nontiles = [[0, 0, 0],
			[0, 0, 0],
			[0, 0, 0]]


def main(stdscr):
	# Clear screen
	stdscr.clear()

	setup(stdscr)

	x = 2
	y = 5
	stdscr.move(y, x)

	while True:
		key = stdscr.getkey()
		if key == "x":
			break
		elif key == "r":
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
		else:
			stdscr.addstr(key)


def setup(stdscr):
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
└-------┴-------┴-------┘
"""

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
	# horiz_border = "-------"
	# x = y = 0

	# def full_row(y, x, l, m, r):
	# 	stdscr.addch(y, x, l)
	# 	x += 1
	# 	stdscr.addstr(y, x, horiz_border)
	# 	x += len(horiz_border)
	# 	stdscr.addch(y, x, m)
	# 	x += 1
	# 	stdscr.addstr(y, x, horiz_border)
	# 	x += len(horiz_border)
	# 	stdscr.addch(y, x, m)
	# 	x += 1
	# 	stdscr.addstr(y, x, horiz_border)
	# 	x += len(horiz_border)
	# 	stdscr.addch(y, x, r)
	# 	y += 1
	# 	x = 0
	# 	return y, x

	# def empty_row(y, x, l, m, r):
	# 	stdscr.addch(y, x, l)
	# 	x += 1
	# 	stdscr.addstr(y, x, " " * len(horiz_border))
	# 	x += len(horiz_border)
	# 	stdscr.addch(y, x, m)
	# 	x += 1
	# 	stdscr.addstr(y, x, " " * len(horiz_border))
	# 	x += len(horiz_border)
	# 	stdscr.addch(y, x, m)
	# 	x += 1
	# 	stdscr.addstr(y, x, " " * len(horiz_border))
	# 	x += len(horiz_border)
	# 	stdscr.addch(y, x, r)
	# 	y += 1
	# 	x = 0
	# 	return y, x


	# stdscr.addstr(y, x, "Use the arrow keys to move the cursor.")
	# y += 1
	# stdscr.addstr(y, x, "Press the spacebar to place your mark.")
	# y += 1
	# stdscr.addstr(y, x, "Press 'r' to reset the game.")
	# y += 1
	# stdscr.addstr(y, x, "Press 'x' to quit.")
	# y += 1

	# # top line of grid
	# y, x = full_row(y, x, curses.ACS_ULCORNER, curses.ACS_TTEE, curses.ACS_URCORNER)

	# for i in range(3):
	# 	y, x = empty_row(y, x, curses.ACS_VLINE, curses.ACS_VLINE, curses.ACS_VLINE)

	# # lines for the first row of boards
	# y, x = full_row(y, x, curses.ACS_LTEE, curses.ACS_VLINE, curses.ACS_RTEE)

	# # empty rows between 1 and 2
	# for i in range(3):
	# 	y, x = empty_row(y, x, curses.ACS_VLINE, curses.ACS_VLINE, curses.ACS_VLINE)

	# # lines for row 2
	# y, x = full_row(y, x, curses.ACS_LTEE, curses.ACS_VLINE, curses.ACS_RTEE)

	# # empty rows between 2 and 3
	# for i in range(3):
	# 	y, x = empty_row(y, x, curses.ACS_VLINE, curses.ACS_VLINE, curses.ACS_VLINE)

	# # bottom row of grid
	# y, x = full_row(y, x, curses.ACS_LLCORNER, curses.ACS_BTEE, curses.ACS_LRCORNER)


curses.wrapper(main)