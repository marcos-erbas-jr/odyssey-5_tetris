import pygame
import random

pygame.init()
screen = pygame.display.set_mode((300, 420))
pygame.display.set_caption('Tetris')
#icon = pygame.image.load('tetris.png')
#pygame.display.set_icon(icon)
clock = pygame.time.Clock()
running = True

x = 1
y = 1

o_block = [(x, y), (x+11, y), (x, y+11), (x+11, y+11)]
z_block = [(x, y), (x+11, y), (x+11, y+11), (x+22, y+11)]
s_block = [(x, y+11), (x+11, y+11), (x+11, y), (x+22, y)]
i_block = [(x, y), (x, y+11), (x, y+22), (x, y+33)]
l_block = [(x, y), (x, y+11), (x, y+22), (x+11, y+22)]
j_block = [(x+11, y), (x+11, y+11), (x+11, y+22), (x, y+22)]
t_block = [(x, y+11), (x+11, y+11), (x+22, y+11), (x+11, y)]

list_blocks = [o_block, z_block, s_block, i_block, l_block, j_block, t_block]
block = random.choice(list_blocks)

def margin():
    pygame.draw.lines(screen, (255, 255, 255), True,
                      [(130, 20), (260, 20), (130,20), (130, 380), (130, 380),
                       (260, 380), (260, 380),(260, 20)], 5)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    margin()

#teste de desenho de blocos
    for parts in block:
        pygame.draw.rect(screen, (255, 255, 255), (parts, (10, 10)))



    pygame.display.flip()
    pygame.time.Clock().tick()



pygame.quit()