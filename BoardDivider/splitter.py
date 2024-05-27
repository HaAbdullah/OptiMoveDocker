#import cropper #USE THIS IF YOU'RE RUNNING FILE INDEPENDENTLY
from . import cropper #USE THIS IF YOU'RE USING nameALlTiles.py
 
import cv2

def splitter(path, viewing_side):
    """
    Split the chessboard image into individual tiles and save them as separate images.

    Parameters:
        path (str): The path to the chessboard image file.
        viewing_side (str): The viewing side of the chessboard. 
            Specify "WHITE" if viewing from the white side (a-h from left to right, 8-1 from top to bottom).
            Specify "BLACK" if viewing from the black side (h-a from left to right, 1-8 from top to bottom).

    Returns:
        None

    Saves:
        Individual images for each tile in the "output_tiles" directory, named according to their position on the chessboard.
    """
    viewing_side = viewing_side.upper()
    
    cropper.cropper(path)
    
    img = cv2.imread("output.jpg") #USE THIS IF INDEPENDENT
    # shape = (width, height, channel)
    width = img.shape[0]
    height = img.shape[1]
    block_width = int(width/8)
    block_height = int(height/8)

    # Determines if the tiles are viewed and arranged from white side or black side (top left to bottom right)
    # White side: a -> h && 8 -> 1 
    # Black side: h -> a && 1 -> 8

    starting_letter = 97 if viewing_side == "WHITE" else 104
    starting_number = 8 if viewing_side == "WHITE" else 1
    
    ending_letter = 105 if viewing_side == "WHITE" else 96
    ending_number = 0 if viewing_side == "WHITE" else 9
    
    iteration = -1 if viewing_side == "WHITE" else 1

    # iterate 8,8 array and split image into tiles from top left -> top right and then move on to next line
    # Counter for tile in y direction
    yCounter = 0
    for number in range(starting_number, ending_number, iteration):
        # Counter for current tile in x direction 
        xCounter = 0
        
        for letter in range(starting_letter, ending_letter, -iteration):
            # [y:y+h, x:x+w]
            cropped_image = img[block_height * yCounter:block_height + block_height * yCounter, block_width * xCounter:block_width+block_width * xCounter]
            
            xCounter += 1
            #cv2.imwrite(f"output_tiles/{chr(letter)}-{number}.png", cropped_image) #INDEPENDENT
            cv2.imwrite(f"BoardDivider/output_tiles/{chr(letter)}-{number}.png", cropped_image) #WITH nameAllTiles.py
            #print(f"output_tiles/{chr(letter)}-{number}.jpg")
            
            # Display each tile (trust me, it's pretty satisfying)
            # cv2.imshow('Cropped Image', cropped_image)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            
        yCounter += 1
    print("splitting complete!")
        
#splitter('images/chess.jpg', "black")