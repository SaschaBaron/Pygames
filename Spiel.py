import pygame , sys

pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Hallo Pygame")
clock = pygame.time.Clock()
fps = 60
clock.tick((fps))

#define game variables



"""load images
img = pygame.image.load(img path)"""

running = True
while running:

    #screen.blit.load(img path)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
            sys.exit()
    pygame.display.update()
    screen.fill(pygame.Color("Purple"))





