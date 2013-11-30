import curses


up = curses.KEY_UP
down = curses.KEY_DOWN
left = curses.KEY_LEFT
right = curses.KEY_RIGHT

player_1 = 1
player_2 = -1

# default these to a zero.
# change to appropriate player value (from above) when noventile is won.
noventiles = [[0, 0, 0],
			  [0, 0, 0],
			  [0, 0, 0]]


def main(stdscr):
	# Clear screen
	stdscr.clear()

	setup(stdscr)

	while True:
		key = stdscr.getkey()
		if key == "x":
			break
		elif key == "r":
			x = y = 0

		stdscr.refresh()

def setup(stdscr):
	horiz_border = "------------------------"
	x = y = 0
	stdscr.addstr(y, x, "Use the arrow keys to move the cursor.")
	y += 1
	stdscr.addstr(y, x, "Press the spacebar to place your mark.")
	y += 1
	stdscr.addstr(y, x, "Press 'r' to reset the game.")
	y += 1
	stdscr.addstr(y, x, "Press 'x' to quit.")
	y += 1
	stdscr.addch(y, x, curses.ACS_ULCORNER)
	x += 1
	stdscr.addstr(y, x, 3 * horiz_border)
	x += len(3 * horiz_border)
	stdscr.addch(y, x, curses.ACS_URCORNER)
	y += 1
	x = 0




curses.wrapper(main)