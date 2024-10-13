from ImageToFEN import nameAllTiles, convert_to_FEN, printAllTiles
from FENtoMove import FENtoMove
import os

# Ask the user for viewing side and active color
user_viewing_side = "BLACK" # BLACK or WHITE
user_turn_color = "b"  # or "b" for black's turn
folder_path = "."
image_files = [f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))]

if len(image_files) == 1:
    image_path = os.path.join(folder_path, image_files[0])
    board = nameAllTiles(user_viewing_side, image_path)
    printAllTiles(board)
    fen = convert_to_FEN(board, user_turn_color)
    move = FENtoMove(fen)
    print(f"FEN: {fen}")
    print("The best move is: " + move)
else:
    print("Please ensure there is exactly one image file in the folder.")
    

# board = nameAllTiles(user_viewing_side, r"img/input3.png")
# printAllTiles(board)
# fen = convert_to_FEN(board, user_turn_color)
# move = FENtoMove(fen)

# print(f"FEN: {fen}")
# print("The best move is: " + move)

