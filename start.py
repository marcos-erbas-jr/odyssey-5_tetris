import pygame
import random

pygame.init()
screen = pygame.display.set_mode((300, 420))
pygame.display.set_caption('Tetris')
#icon = pygame.image.load('tetris.png')
#pygame.display.set_icon(icon)
clock = pygame.time.Clock()
running = True

x = 170
y = 26
final_limit = 0
block_shape = []

blocksInScreen = []


new_block = True

fall_speed = 2

o_block = [(0,0), (11,0), (0,11), (11,11)]
z_block = [(0,0), (11,0), (11,11), (22,11)]
s_block = [(11,0), (22,0), (0,11), (11,11)]
i_block = [(0,0), (0,11), (0,22), (0,33)]
l_block = [(0,0), (0,11), (0,22), (11,22)]
j_block = [(11,0), (11,11), (11,22), (0,22)]
t_block = [(11,0), (11,11), (0,1), (22,11)]

list_blocks = [o_block, z_block, s_block, i_block, l_block, j_block, t_block]
def choiceBlock():
    block_shape = random.choice(list_blocks)
    return block_shape

def margin():
    pygame.draw.lines(screen, (255, 255, 255), True,
                      [(90, 20), (260, 20), (90,20), (90, 380), (130, 380),
                       (260, 380), (260, 380),(260, 20)], 5)


while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    margin()

    if final_limit < 370:
        y += fall_speed
    else:
        blocksInScreen.append([block_shape, [x, y]])
        print(blocksInScreen)
        new_block = True
        final_limit = 0
        y = 26

    # Desenha o bloco com base em (x,y)
    if new_block:
        block_shape = choiceBlock()
        new_block = False

    else:
        for parts in block_shape:
            px, py = parts
            pygame.draw.rect(screen, (255, 255, 255), (x + px, y + py, 10, 10))
            if parts == block_shape[3]:
                final_limit = parts[1] + y

    for block in blocksInScreen:
        print(block)
        for parts in range(0, 4):
            px, py = block[0] [parts]
            pygame.draw.rect(screen, (255, 255, 255), (block[1][0] + px, block[1][1] + py, 10, 10))






    pygame.display.flip()
    clock.tick(60)



pygame.quit()