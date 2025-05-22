# Link to view project: https://codeinplace.stanford.edu/cip5/share/sYc04iGGDk3uGfCNQEqT

# Import to let us use "Canvas"
from graphics import Canvas

# Canvas height and width
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 200
# Number of boxes
N_BOXES = 5
# Use integer division for precise pixels
BOX_SIZE = CANVAS_WIDTH // N_BOXES 
# Height of each bottom box
BOX_HEIGHT = 80  

# Main Function 
def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    bottom = CANVAS_HEIGHT
    top = bottom - BOX_HEIGHT  # make boxes shorter

    for i in range(N_BOXES):
        left = i * BOX_SIZE
        right = left + BOX_SIZE
        canvas.create_rectangle(left, top, right, bottom, 'white', outline='black')

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
