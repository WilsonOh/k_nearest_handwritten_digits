import numpy as np
import pygame

import k_nearest

pygame.init()
W, H = 560, 560
SIZE = (W, H)
SQ_SIZE = 20
window = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Try writing a digit!')
clock = pygame.time.Clock()


def get_mouse_pos():
    """Returns a tuple containing the mouse position coords
        in blocks of [SQ_SIZE]"""
    return tuple(map(lambda s: (s // SQ_SIZE), pygame.mouse.get_pos()))


# a 28 x 28 matrix representing the handwritten digit, initallized to false
grid = np.zeros((W//SQ_SIZE, H//SQ_SIZE), dtype=bool)

while True:
    clock.tick(120)

    def draw():
        """Handles the drawing of gridlines and the filling of
            squares onto the window"""
        window.fill(pygame.Color('white'))
        for x in range(0, W, SQ_SIZE):
            pygame.draw.line(window, pygame.Color('gray'), (x, 0), (x, H))
        for y in range(0, H, SQ_SIZE):
            pygame.draw.line(window, pygame.Color('gray'), (0, y), (W, y))

        # Generate a list of tuples where the square on the grid is "True"
        to_fill = np.argwhere(grid)
        for x, y in to_fill:
            pygame.draw.rect(window, pygame.Color('red'), pygame.Rect(
                x * SQ_SIZE, y * SQ_SIZE, SQ_SIZE, SQ_SIZE))
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # Reset the canvas
                grid = np.zeros((W // SQ_SIZE, H // SQ_SIZE), dtype=bool)
            if event.key == pygame.K_RETURN:
                # Sends the digit matrix for processing to the k_nearest module
                k_nearest.init(grid.T)
                # Reset the canvas
                grid = np.zeros((W // SQ_SIZE, H // SQ_SIZE), dtype=bool)

    # Checks if the user presses down the left mouse button
    if pygame.mouse.get_pressed()[0]:
        # Mark the square the cursor is on for drawing
        grid[get_mouse_pos()] = True
        i, j = get_mouse_pos()
        # Mark surrounding squares for drawing too in order to
        # make the lines drawn "thicker"
        if i < 27 and j < 27:
            grid[i + 1, j] = True
            grid[i, j + 1] = True
            grid[i + 1, j + 1] = True

    draw()
