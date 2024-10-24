from ImageToFEN import nameAllTiles, convert_to_FEN, printAllTiles
from FENtoMove import FENtoMove
import os

# Ask the user for viewing side and active color
user_viewing_side = input("Is the image being viewed from the White or Black POV? (white / black)\n").lower() 

while user_viewing_side not in ['white', 'black']:
    print("Invalid input for viewing side. Please enter 'White' or 'Black'.")
    user_viewing_side = input("Is the image being viewed from the White or Black POV? (white / black)\n").lower() 
    

user_turn_color = input("Whose turn is it? (white / black)\n") 

while user_turn_color not in ['white', 'black']:
    print("Invalid input for turn color. Please enter 'w' for White or 'b' for Black.")
    user_turn_color = input("Whose turn is it? (white / black)\n") 
    
folder_path = "/app/images"  # SPECIFICALLY FOR DOCKER MOUNTED IMAGES

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

