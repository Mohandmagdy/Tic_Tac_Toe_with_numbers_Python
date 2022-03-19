# Tic_Tac_Toe_with_numbers_Python
Tic Tac Toe numbers game (2 players) one enters odd numbers and the second one enters even numbers, To win you must complete the sum of the diagonal to be equal to 15 (like 5-6-4) (Horizontally, vertically or by a diagonals)



Code Explanation:
welcome the user 

made a list with the structure of the board and its shape

declared the basic variables 
	first player.
	list of numbers available for the first player.
	list of numbers available for the second player.
	game_running always true until the game is finished.


print board(board)
made a function that can print the board in well-mannered shape as tic tac toe game in real life.
	print it in each loop (after each play).

player input()
made a function that takes the input from the user and check if the number is in the (list of numbers available for the player) and if it's not, prints error message and let this player to try again.
it also takes the position that the player wants to put his number into and check if this position or empty or not or if it even exists, if it's not empty or it does not exist it prints error message and let this player to try again.

next stage I checked all the win situation after every play.

check horizontal(board)
	a function that checks all the three rows if any of them sums up to 15.
check vertical(board) 
a function that checks all the three columns if any of them sums up to 15.
check diagonals(board)
	a function that checks the two diagonals if any of them sums up to 15.

win or not()
a function that checks if the winning situation was found to end the game or to complete.
it also congratulates the winner if the winning situation was found and change game_running to False to end the game .

check tie()
a function that checks if the board is full and no one won to tell the player that it's a draw.
	then it changes game_running to False to end the game.

switch the player()
	function that changes the current player after every play.

GAME LOOP
while game_running (Which means that if game_running = true the game will continue, if it's not the game will stop):
here i used all the recent functions in this loop to continue the game process until there is a winner or it's a Draw situation.

YT video:
https://www.youtube.com/watch?v=VYVJ2_6Jnkc (Arabic Explanation Video)
