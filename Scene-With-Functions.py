# Link to view project: https://codeinplace.stanford.edu/cip5/share/30mWsIEgU6SeVZfyJhpk

from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

CLOUD_WIDTH = 120
CLOUD_HEIGHT = 80

TRUNK_HEIGHT = 80
TRUNK_WIDTH = 20
LEAVES_SIZE = 60

TREE_BOTTOM_Y = CANVAS_HEIGHT - 20  # Y position of the tree base

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)  # Create canvas

    # Draw clouds at different positions with colors
    draw_cloud(canvas, 20, 10, 'pink')
    draw_cloud(canvas, 140, 10, 'salmon')
    draw_cloud(canvas, 260, 10, 'purple')

    # Draw trees at different x positions with colors
    draw_tree(canvas, 60, 'green')
    draw_tree(canvas, 140, 'red')
    draw_tree(canvas, 220, 'orange')

def draw_cloud(canvas, x, y, color):
    # Calculate vertical positions for cloud bottom and top parts
    cloud_bottom_start_y = y + (1/3) * CLOUD_HEIGHT
    cloud_bottom_end_y = y + CLOUD_HEIGHT
    cloud_top_start_x = x + (1/4) * CLOUD_WIDTH
    cloud_top_end_x = x + (3/4) * CLOUD_WIDTH

    # Draw left bottom oval of cloud
    canvas.create_oval(
        x, 
        cloud_bottom_start_y,
        x + (3/4) * CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )
    # Draw right bottom oval of cloud
    canvas.create_oval(
        x + (1/4) * CLOUD_WIDTH, 
        cloud_bottom_start_y,
        x + CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )
    # Draw top oval of cloud
    canvas.create_oval(
        cloud_top_start_x,
        y,
        cloud_top_end_x,
        y + (2/3) * CLOUD_HEIGHT,
        color
    )

def draw_tree(canvas, x, color):
    trunk_top_y = TREE_BOTTOM_Y - TRUNK_HEIGHT  # Calculate top of the trunk
    # Draw tree trunk rectangle
    canvas.create_rectangle(
        x - TRUNK_WIDTH // 2, trunk_top_y,
        x + TRUNK_WIDTH // 2, TREE_BOTTOM_Y,
        'brown'
    )
    leaves_center_y = trunk_top_y  # Center y for leaves oval
    # Draw leaves as oval above the trunk
    canvas.create_oval(
        x - LEAVES_SIZE // 2, leaves_center_y - LEAVES_SIZE // 2,
        x + LEAVES_SIZE // 2, leaves_center_y + LEAVES_SIZE // 2,
        color
    )

if __name__ == '__main__':
    main()
