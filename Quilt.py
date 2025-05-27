# Link to view project: https://codeinplace.stanford.edu/cip5/share/WYHe14Q4Be7W6ORgIYIv

from graphics import Canvas

# Each patch is a square with this width and height:
PATCH_SIZE = 100

# The canvas is 4 patches wide and 2 patches tall
CANVAS_WIDTH = PATCH_SIZE * 4
CANVAS_HEIGHT = PATCH_SIZE * 2

def main():
    # Create the drawing canvas
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # First row of patches (top row)
    draw_square_patch(canvas, 0, 0)                    # Top-left patch
    draw_circle_patch(canvas, PATCH_SIZE, 0)           # Second patch
    draw_square_patch(canvas, PATCH_SIZE * 2, 0)       # Third patch
    draw_circle_patch(canvas, PATCH_SIZE * 3, 0)       # Fourth patch

    # Second row of patches (bottom row)
    draw_circle_patch(canvas, 0, PATCH_SIZE)           # Bottom-left patch
    draw_square_patch(canvas, PATCH_SIZE, PATCH_SIZE)  # Second patch
    draw_circle_patch(canvas, PATCH_SIZE * 2, PATCH_SIZE)  # Third patch
    draw_square_patch(canvas, PATCH_SIZE * 3, PATCH_SIZE)  # Fourth patch

def draw_circle_patch(canvas, start_x, start_y):
    """
    Draws a salmon-colored circle that fills an entire patch.
    The top-left corner of the patch is (start_x, start_y).
    """
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    canvas.create_oval(start_x, start_y, end_x, end_y, 'salmon')

def draw_square_patch(canvas, start_x, start_y):
    """
    Draws a purple square patch with a smaller white square inside it.
    The top-left corner of the patch is (start_x, start_y).
    """
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    inset = 20  # Margin for the inner white square
    
    # Draw the full purple square (outer border)
    canvas.create_rectangle(start_x, start_y, end_x, end_y, 'purple')
    
    # Draw the smaller white square inside the purple frame
    canvas.create_rectangle(start_x + inset, start_y + inset, 
                            end_x - inset, end_y - inset, 'white')

# No changes from here   
if __name__ == '__main__':
    main()
