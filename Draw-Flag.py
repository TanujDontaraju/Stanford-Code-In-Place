# Link to view project: https://codeinplace.stanford.edu/cip5/share/1Cx2X0UQCbIjh73Y7yAp

# Lets us utilize "Canvas" functions
from graphics import Canvas

# Predetermined width and height 
CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300

# Main functon 
def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    left = 0
    top = 0
    right = 450
    bottom = 150
    color = 'red'

    # Makes a rectangle shape 
    rect = canvas.create_rectangle(left, top, right, bottom, color)

# No changes from here 
if __name__ == '__main__':
    main()
