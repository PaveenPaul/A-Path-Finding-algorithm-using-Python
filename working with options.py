import pygame
import math
from queue import PriorityQueue
import time

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path finding algorithm")


RED = (0, 255, 0)
# RED = (255, 0, 0)
GREEN = (47, 79, 79)
# GREEN = (0, 255, 0)
BLUE = (0, 0, 255) 
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# PURPLE = (128, 0, 128)
PURPLE = (139, 69, 19)
ORANGE = (139, 0, 139)
# ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
# TURQUOISE = (64, 224, 208)
TURQUOISE = (0, 139, 139)


class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = WIDTH
        self.total_rows = total_rows
        
    def get_pos(self):
        return self.row, self.col
    
    def is_closed(self):
        return self.color == RED
    def is_open(self):
        return self.color == GREEN
    def is_barrier(self):
        return self.color == BLACK
    def is_start(self):
        return self.color == ORANGE
    def is_end(self):
        return self.color == TURQUOISE
    
    def reset(self):
        self.color = WHITE
        
    def make_start(self):
        self.color = ORANGE
    
    def make_closed(self):
        self.color = RED
    
    def make_open(self):
        self.color = GREEN
    
    def make_barrier(self):
        self.color = BLACK
    
    def make_end(self):
        self.color = TURQUOISE
        
    def make_path(self):
        self.color = PURPLE
        
    def draw(self,win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
        
    def update_neighbours(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): #down
            self.neighbors.append(grid[self.row + 1][self.col])
            
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): #up
            self.neighbors.append(grid[self.row - 1][self.col])
            
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): #right
            self.neighbors.append(grid[self.row][self.col + 1])
            
        if self.col >  0 and not grid[self.row][self.col - 1 ].is_barrier(): #left
            self.neighbors.append(grid[self.row][self.col - 1])
    
    def __lt__(self, other):
        return False
    
def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()
        
        
def algorithm(draw, grid, start, end, function):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))  #f-score
    came_from = {}   #what not it came from not C from note B
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = function(start.get_pos(), end.get_pos())
    
    
    open_set_hash = {start}
    
    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current = open_set.get()[2]
        open_set_hash.remove(current)
        
        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True
            
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1
            
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + function(neighbor.get_pos(),end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        draw()
        if current != start:
            current.make_closed()
    return False

def euclidean_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def minkowski_distance(p1, p2, p=2):
    x1, y1 = p1
    x2, y2 = p2
    return ((abs(x1 - x2))**p + (abs(y1 - y2))**p)**(1/p)

def octile_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    return max(dx, dy) + (math.sqrt(2) - 1) * min(dx, dy)

def chebyshev_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return max(abs(x1 - x2), abs(y1 - y2))

def manhattan_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1 - y2)




def make_grid(rows, width):
    grid = []
    gap = width // rows
    
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)
    return grid

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY , (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY , (j * gap, 0), (j*gap, width))
            
def draw(win, grid, rows, width):
    win.fill(WHITE)
    
    for row in grid:
        for spot in row:
            spot.draw(win)
    
    draw_grid(win, rows, width)
    pygame.display.update()
    
def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    
    row = y // gap
    col = x // gap
    return row, col


def main(win, width):
    ROWS = 10
    grid = make_grid(ROWS, width)
    
    start = None
    end = None
    
    run = True
    while run:
        # Draw the enlarged caption area
        pygame.init() 
        font = pygame.font.Font(None, 36)
        caption_text = font.render("A* Path finding algorithm - Select distance metric:", True, (0, 0, 0))
        caption_rect = caption_text.get_rect(center=(WIDTH // 2, 20))
        win.blit(caption_text, caption_rect)
        
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if pygame.mouse.get_pressed()[0]:   # left click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not start and spot != end:
                    start = spot
                    start.make_start()
                elif not end and spot != start:
                    end = spot
                    end.make_end()
                elif spot != end and spot !=start:
                    spot.make_barrier()
                
            elif pygame.mouse.get_pressed()[2]: # right click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None
        
            display_popup(win)  
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_1:
                    selected_option = 1
                    for row in grid:
                        for spot in row:
                            spot.update_neighbours(grid)
                    
                    algorithm(lambda : draw(win, grid, ROWS, width), grid, start, end,euclidean_distance)
                    
                    # run = False
                    print(selected_option,",################################")  
                elif event.key == pygame.K_2:
                    selected_option = 2
                    # run = False  
                    print(selected_option,",################################") 
                elif event.key == pygame.K_3:
                    selected_option = 3
                    # run = False
                    print(selected_option,",################################") 
                elif event.key == pygame.K_4:
                    selected_option = 4
                    # run = False        
                    print(selected_option,",################################")                         
                elif event.key == pygame.K_5:
                    selected_option = 5
                    print(selected_option,",################################") 
                    
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbours(grid)
                    if selected_option == 1:
                        algorithm(lambda : draw(win, grid, ROWS, width), grid, start, end,euclidean_distance)
                        
                    elif selected_option == 2:
                        algorithm(lambda : draw(win, grid, ROWS, width), grid, start, end,manhattan_distance)
                        print("selected", selected_option) 
                                               
                    elif selected_option == 3:
                        algorithm(lambda : draw(win, grid, ROWS, width), grid, start, end,chebyshev_distance)
                        print("selected", selected_option)
                                                                   
                    elif selected_option == 4:
                        algorithm(lambda : draw(win, grid, ROWS, width), grid, start, end,octile_distance)
                        print("selected", selected_option)
                                                                                           
                    elif selected_option == 5:
                        algorithm(lambda : draw(win, grid, ROWS, width), grid, start, end,minkowski_distance)
                        print("selected", selected_option)
                 
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)
                    
        
    pygame.quit()
    

def display_popup(screen):
    pygame.init() 
    font = pygame.font.Font(None, 36)
    
    # Render and display "Select distance metric" text
    text = font.render("Select distance metric:", True, (0, 0, 0))
    text_rect = text.get_rect(center=(400, 200))
    screen.blit(text, text_rect)
    
    # Render and display each option with appropriate vertical spacing
    options = ["Euclidean Distance", "Manhattan Distance", "Chebyshev Distance", "Octile Distance", "Minkowski Distance"]
    y_position = 250
    for index, option in enumerate(options, start=1):
        option_text = font.render(f"{index}. {option}", True, (0, 0, 0))
        option_rect = option_text.get_rect(center=(400, y_position))
        screen.blit(option_text, option_rect)
        y_position += 50
    
    pygame.display.flip()
     
main(WIN, WIDTH)
    
    # 1:02
    
    
