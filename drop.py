import pygame

# Define some colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GRAY = (200, 200, 200)

# Initialize Pygame
# pygame.init()

# Set the width and height of the screen
# SCREEN_WIDTH = 400
# SCREEN_HEIGHT = 300
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the caption
# pygame.display.set_caption("A* Pathfinding Algorithm")

# Font for menu items
# font = pygame.font.Font(None, 24)

# Menu items
# menu_items = ["Euclidean Distance", "Manhattan Distance", "Chebyshev Distance", "Octile Distance", "Minkowski Distance"]
# selected_item = None

# # Function to get distance metric based on selected item
def get_distance_metric(item):
    if item == "Euclidean Distance":
        print("euclidean_distance")
        return "1"
    elif item == "Manhattan Distance":
        print("manhattan_distance")
        return "2"
    elif item == "Chebyshev Distance":
        print("chebyshev_distance")
        return "3"
    elif item == "Octile Distance":
        print("octile_distance")
        return "4"
    elif item == "Minkowski Distance":
        print("minkowski_distance")
        return "5"

# Main loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             if event.button == 1:  # Left mouse button
#                 # Check if the mouse click is inside the menu area
#                 if 50 <= event.pos[0] <= 350 and 50 <= event.pos[1] <= 300:
#                     # Determine which menu item was clicked
#                     index = (event.pos[1] - 50) // 25
#                     selected_item = menu_items[index]
#                     # Get the selected distance metric function
#                     distance_metric_function = get_distance_metric(selected_item)
#                     # Print the selected item (for demonstration)
#                     print("Selected Distance Metric:", selected_item)

#     # Clear the screen
#     screen.fill(WHITE)

#     # Draw the menu area
#     pygame.draw.rect(screen, GRAY, (50, 50, 300, 125))

#     # Draw the menu items
#     for i, item in enumerate(menu_items):
#         text = font.render(item, True, BLACK)
#         text_rect = text.get_rect(center=(200, 62.5 + i * 25))
#         screen.blit(text, text_rect)

#     # Highlight the selected item
#     if selected_item is not None:
#         pygame.draw.rect(screen, BLACK, (50, 50 + menu_items.index(selected_item) * 25, 300, 25), 2)

#     # Update the display
#     pygame.display.flip()

# # Quit Pygame
# pygame.quit()


def option():
    pygame.init()
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)
    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 300
    pygame.display.set_caption("A* Pathfinding Algorithm")
    font = pygame.font.Font(None, 24)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    menu_items = ["Euclidean Distance", "Manhattan Distance", "Chebyshev Distance", "Octile Distance", "Minkowski Distance"]
    selected_item = None

    flag = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    # Check if the mouse click is inside the menu area
                    if 50 <= event.pos[0] <= 350 and 50 <= event.pos[1] <= 300:
                        # Determine which menu item was clicked
                        index = (event.pos[1] - 50) // 25
                        selected_item = menu_items[index]
                        # Get the selected distance metric function
                        distance_metric_function = get_distance_metric(selected_item)
                        # Print the selected item (for demonstration)
                        print("Selected Distance Metric:", selected_item)
                        flag = 1
                        running = False
                        print("FLAG###", flag)
                        # pygame.quit()
        if flag != 0:
            break
        screen.fill(WHITE)

        pygame.draw.rect(screen, GRAY, (50, 50, 300, 125))

        # Draw the menu items
        for i, item in enumerate(menu_items):
            text = font.render(item, True, BLACK)
            text_rect = text.get_rect(center=(200, 62.5 + i * 25))
            screen.blit(text, text_rect)

        # Highlight the selected item
        if selected_item is not None:
            pygame.draw.rect(screen, BLACK, (50, 50 + menu_items.index(selected_item) * 25, 300, 25), 2)

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    return distance_metric_function

# def option(screen):
#     # Initialize Pygame
#     pygame.init()

#     # Set the caption
#     pygame.display.set_caption("Dropdown Menu")

#     # Font for menu items
#     font = pygame.font.Font(None, 24)

#     # Menu items
#     menu_items = ["Euclidean Distance", "Manhattan Distance", "Chebyshev Distance", "Octile Distance", "Minkowski Distance"]
#     selected_item = None

#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 if event.button == 1:  # Left mouse button
#                     # Check if the mouse click is inside the menu area
#                     if 50 <= event.pos[0] <= 350 and 50 <= event.pos[1] <= 300:
#                         # Determine which menu item was clicked
#                         index = (event.pos[1] - 50) // 25
#                         selected_item = menu_items[index]
#                         # Get the selected distance metric function
#                         distance_metric_function = get_distance_metric(selected_item)
#                         # Print the selected item (for demonstration)
#                         print("Selected Distance Metric:", selected_item)

#         # Clear the screen
#         screen.fill(WHITE)

#         # Draw the menu area
#         pygame.draw.rect(screen, GRAY, (50, 50, 300, 125))

#         # Draw the menu items
#         for i, item in enumerate(menu_items):
#             text = font.render(item, True, BLACK)
#             text_rect = text.get_rect(center=(200, 62.5 + i * 25))
#             screen.blit(text, text_rect)

#         # Highlight the selected item
#         if selected_item is not None:
#             pygame.draw.rect(screen, BLACK, (50, 50 + menu_items.index(selected_item) * 25, 300, 25), 2)

#         # Update the display
#         pygame.display.flip()

#     # Quit Pygame
#     pygame.quit()

#     return selected_item
if __name__ == "__main__":
    selected = option()
    print("retuen ", selected)