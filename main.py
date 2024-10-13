from ImageToFEN import nameAllTiles, convert_to_FEN, printAllTiles
from FENtoMove import FENtoMove
import os

# Ask the user for viewing side and active color
user_viewing_side = "BLACK" # BLACK or WHITE
user_turn_color = "b"  # or "b" for black's turn

board = nameAllTiles(user_viewing_side, r"img/input3.png")
printAllTiles(board)
fen = convert_to_FEN(board, user_turn_color)
move = FENtoMove(fen)

print(f"FEN: {fen}")
print("The best move is: " + move)

