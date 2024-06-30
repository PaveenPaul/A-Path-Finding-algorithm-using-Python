import pygame
from main import Spot
# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Initialize Pygame
pygame.init()

# Set the width and height of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the caption
pygame.display.set_caption("A* Pathfinding Algorithm")

# Font for menu items
font = pygame.font.Font(None, 24)

# Menu items
menu_items = ["Euclidean Distance", "Manhattan Distance", "Chebyshev Distance", "Octile Distance", "Minkowski Distance"]
selected_item = None

# Function to get distance metric based on selected item
def get_distance_metric(item):
    if item == "Euclidean Distance":
        print("euclidean_distance")
        # return euclidean_distance
    elif item == "Manhattan Distance":
        print("manhattan_distance")
        # return manhattan_distance
    elif item == "Chebyshev Distance":
        print("chebyshev_distance")
        # return chebyshev_distance
    elif item == "Octile Distance":
        print("octile_distance")
        # return octile_distance
    elif item == "Minkowski Distance":
        print("minkowski_distance")
        # return minkowski_distance

# Main loop
def main(win, width):
    spot = 
    ROWS = 10
    grid = make_grid(ROWS, width)
    
    start = None
    end = None
    
    run = True
    while run:
        # Clear the screen
        screen.fill(WHITE)
        
        # Draw the dropdown menu
        pygame.draw.rect(screen, GRAY, (50, 50, 200, 125))
        for i, item in enumerate(menu_items):
            text = font.render(item, True, BLACK)
            text_rect = text.get_rect(center=(150, 62.5 + i * 25))
            screen.blit(text, text_rect)
        
        # Highlight the selected item
        if selected_item is not None:
            pygame.draw.rect(screen, BLACK, (50, 50 + menu_items.index(selected_item) * 25, 200, 25), 2)
        
        # Draw the grid
        draw_grid(win, grid, ROWS, width)
        
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    # Check if the mouse click is inside the menu area
                    if 50 <= event.pos[0] <= 250 and 50 <= event.pos[1] <= 175:
                        # Determine which menu item was clicked
                        index = (event.pos[1] - 50) // 25
                        selected_item = menu_items[index]
                        # Get the selected distance metric function
                        distance_metric_function = get_distance_metric(selected_item)
                        # Print the selected item (for demonstration)
                        print("Selected Distance Metric:", selected_item)
                else:
                    # Handle grid interaction (left click for adding obstacles, right click for removing)
                    pos = pygame.mouse.get_pos()
                    row, col = get_clicked_pos(pos, ROWS, width
                    spot = grid[row][col]
                    if pygame.mouse.get_pressed()[0]:  # Left click
                        if not start and spot != end:
                            start = spot
                            start.make_start()
                        elif not end and spot != start:
                            end = spot
                            end.make_end()
                        elif spot != end and spot != start:
                            spot.make_barrier()
                    elif pygame.mouse.get_pressed()[2]:  # Right click
                        spot.reset()
                        if spot == start:
                            start = None
                        elif spot == end:
                            end = None
        
        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

def make_grid(rows, width):
    grid = []
    gap = width // rows
    
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)
    return grid

def draw_grid(win, grid, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GRAY, (50, 50 + i * gap), (250, 50 + i * gap))
        for j in range(rows):
            pygame.draw.line(win, GRAY, (50 + j * gap, 50), (50 + j * gap, 250))

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    row = (y - 50) // gap
    col = (x - 50) // gap
    return row, col

main(screen, SCREEN_WIDTH - 300)
