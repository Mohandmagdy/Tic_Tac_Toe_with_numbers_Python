# Tic_Tac_Toe_with_numbers_Python
Tic Tac Toe numbers game (2 players) one enters odd numbers and the second one enters even numbers, To win you must complete the sum of the diagonal to be equal to 15 (like 5-6-4) (Horizontally, vertically or by a diagonals)



Code Explanation:
welcome the user 

made a two dimensional array with the structure of the board and its shape

declared the basic variables
game_running always true until the game is finished.
Sum variable which will let us know if it’s a draw or not.
Position variable./
Input (number input) variable.
Printboard(board):
made a function that can print the board in well-mannered shape as tic tac toe game in real life.
	print it in each loop (after each play).
Playerinput():
A function that takes the input from the player check if it’s available for the player or not.
Position():
A function that takes the position of the input of the player and checks if it is available or not and fits it into the two dimensional array.


next stage I checked all the win situation after every play.

check horizontal(board)
	a function that checks all the three rows if any of them sums up to 15.


check vertical(board) 
a function that checks all the three columns if any of them sums up to 15.
check diagonals(board)
	a function that checks the two diagonals if any of them sums up to 15.
Switchplayer():
	A function that changes the player after every play.
Main():
	The main function:
	Game loop:
while game_running (Which means that if game_running = true the game will continue, if it's not the game will stop):
here I used all the recent functions in this loop to continue the game process until there is a winner or it's a Draw situation.

YT video:
https://www.youtube.com/watch?v=mn_dpwiFpkY (Arabic video)
