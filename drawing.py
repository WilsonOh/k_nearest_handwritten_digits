import pygame
import numpy as np
import k_nearest

pygame.init()
W, H = 560, 560
SIZE = (W, H)
SQ_SIZE = 20
window = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Try writing a digit!')
clock = pygame.time.Clock()


def get_mouse_pos():
    return tuple(map(lambda x: x // SQ_SIZE, pygame.mouse.get_pos()))


grid = np.zeros((W//SQ_SIZE, H//SQ_SIZE), dtype=bool)

while True:
    clock.tick(120)

    def draw():
        window.fill(pygame.Color('white'))
        for x in range(0, W, SQ_SIZE):
            pygame.draw.line(window, pygame.Color('gray'), (x, 0), (x, H))
        for y in range(0, H, SQ_SIZE):
            pygame.draw.line(window, pygame.Color('gray'), (0, y), (W, y))
        to_fill = np.argwhere(grid)
        for x, y in to_fill:
            pygame.draw.rect(window, pygame.Color('red'), pygame.Rect(x * SQ_SIZE, y * SQ_SIZE, SQ_SIZE, SQ_SIZE))
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                grid = np.zeros((W // SQ_SIZE, H // SQ_SIZE), dtype=bool)
            if event.key == pygame.K_RETURN:
                k_nearest.init(grid.T)
                grid = np.zeros((W // SQ_SIZE, H // SQ_SIZE), dtype=bool)

    if pygame.mouse.get_pressed()[0]:
        grid[get_mouse_pos()] = True

    draw()
