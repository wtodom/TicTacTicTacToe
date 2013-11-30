TicTacTicTacToe
===============

A (hopefully) simple project to introduce me to curses.

## Rules of Tic Tac Tic Tac Toe

1. The first player can go anywhere they want. From then on, play continues as follows:

	1. Note the location within the subsection that the current player placed their mark.

	2. The other player must place their next mark somewhere in the corresponding subsection. The cursor will automatically move to the correct subsection for you.

	3. If the subsection in which you would have to place your mark is either full or already won, you may place your mark anywhere on the board.

2. Play continues in this manner until either someone wins three consecutive vertical, horizontal, or diagonal subsections (essentially treating subsections like regular spaces from traditional Tic Tac Toe) making that player the winner, or until all subsections are finished or won but without anyone scoring three-in-a-row, which is considered a tie game.