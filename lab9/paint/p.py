import pygame
# Initializing Pygame
pygame.init()

# Function to play background music
def song():
    file = "soundp1.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)

# Define colors
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)

# Frames per second
fps = 60

# Create a clock object to control the frame rate
timer = pygame.time.Clock()

# Set screen dimensions
WIDTH = 800
HEIGHT = 600

# Initialize variables for brush size and color 
active_size = 0
active_color = WHITE

# Create the game window
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Paint!')

# Play background music
song()

# List ot store painting data
painting = []

# Function to draw the menu
def draw_menu(size, color):
    pygame.draw.rect(screen, GRAY, [0, 0, WIDTH, 70])
    pygame.draw.line(screen, BLACK, (0,70), (WIDTH,70), 3)
    xl_brush = pygame.draw.rect(screen, BLACK, [10, 10, 50, 50])
    pygame.draw.circle(screen, WHITE, (35, 35), 20)
    l_brush = pygame.draw.rect(screen, BLACK, [70, 10, 50, 50])
    pygame.draw.circle(screen, WHITE, (95, 35), 15)
    m_brush = pygame.draw.rect(screen, BLACK, [130, 10, 50, 50])
    pygame.draw.circle(screen, WHITE, (155, 35), 10)
    s_brush = pygame.draw.rect(screen, BLACK, [190, 10, 50, 50])
    pygame.draw.circle(screen, WHITE, (215, 35), 5)
    brush_list = [xl_brush, l_brush, m_brush, s_brush]

    # Highlight the selected brush size
    if size == 20:
        pygame.draw.rect(screen, 'green', [10, 10, 50, 50], 3)
    elif size == 15:
        pygame.draw.rect(screen, 'green', [70, 10, 50, 50], 3)
    elif size == 10:
        pygame.draw.rect(screen, 'green', [130, 10, 50, 50], 3)
    elif size == 5:
        pygame.draw.rect(screen, 'green', [190, 10, 50, 50], 3)

    # Draw the color palette
    pygame.draw.circle(screen, color, (400, 35), 30)
    pygame.draw.circle(screen, 'dark gray', (400, 35), 30, 3)

    blue = pygame.draw.rect(screen, (0, 0, 255), [WIDTH -35, 10, 25, 25])
    red = pygame.draw.rect(screen, (255, 0, 0), [WIDTH -35, 35, 25, 25])
    green = pygame.draw.rect(screen, (0, 255, 0), [WIDTH -60, 10, 25, 25])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [WIDTH -60, 35, 25, 25])
    teal = pygame.draw.rect(screen, (0, 255, 255), [WIDTH -85, 10, 25, 25])
    purple = pygame.draw.rect(screen, (255, 0, 255), [WIDTH -85, 35, 25, 25])
    white = pygame.draw.rect(screen, (0, 0, 0), [WIDTH -110, 10, 25, 25])
    black = pygame.draw.rect(screen, (255, 255, 255), [WIDTH -110, 35, 25, 25])
    eraser = pygame.draw.rect(screen, WHITE, [WIDTH -135, 10, 25, 25])
    brush_list.append(eraser)
    color_rect = [blue, red, green,yellow, teal, purple, white, black]
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 255, 255), (255, 0, 255), (0, 0, 0), (255, 255, 255)]
    return brush_list, color_rect, rgb_list

    
# Function to draw the painting
def draw_painting(paints):
    for i in range(len(paints)):
        pygame.draw.circle(screen, paints[i][0], paints[i][1], paints[i][2])

# Function to draw a square
def draw_square(x, y, size, color):
    pygame.draw.rect(screen, color, (x - size//2, y - size//2, size, size), 2)

# function to draw a right triangle
def draw_right_triangle(x, y, size, color):
    points = [(x - size//2, y + size//2), (x + size//2, y + size//2), (x - size//2, y - size//2)]
    pygame.draw.polygon(screen, color, points, 2)

# Function to draw an equilateral triangle
def draw_equilateral_triangle(x, y, size, color):
    height = int(size * (3 ** 0.5) / 2)
    points = [(x, y - size//2), (x - size//2, y + height//2), (x + size//2, y + height//2)]
    pygame.draw.polygon(screen, color, points, 2)

# Function to draw a rhombus
def draw_rhombus(x, y, size, color):
    points = [(x, y - size//2), (x + size//2, y), (x, y + size//2), (x - size//2, y)]
    pygame.draw.polygon(screen, color, points, 2)

# Main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill(WHITE)
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    if left_click and mouse[1] > 70:
        painting.append((active_color, mouse, active_size))

    draw_painting(painting)

    if mouse[1] > 70:
        if pygame.mouse.get_pressed()[2]:
            active_color = WHITE
        else:
            pygame.draw.circle(screen, active_color, mouse, active_size)

    brushes, colors, rgbs = draw_menu(active_size, active_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):
                    active_size = 20 - (i*5)
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:  # Draw Square
                draw_square(mouse[0], mouse[1], 50, active_color)
            elif event.key == pygame.K_2:  # Draw Right Triangle
                draw_right_triangle(mouse[0], mouse[1], 50, active_color)
            elif event.key == pygame.K_3:  # Draw Equilateral Triangle
                draw_equilateral_triangle(mouse[0], mouse[1], 50, active_color)
            elif event.key == pygame.K_4:    # Draw Rhombus
                draw_rhombus(mouse[0], mouse[1], 50, active_color)
        
    pygame.display.update()

# quit pygame
pygame.quit()