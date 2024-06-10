import pygame
from sys import exit # just to close game

pygame.init()

screen_width = 800 # set screen height
screen_height = 400 # and width

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Runner") # set the title bar to say Runner
icon = pygame.image.load('player_stand.png') # set value icon to the path of the image
pygame.display.set_icon(icon) # display the image as the icon for the window
clock = pygame.time.Clock() # Create a clock object

gamelive = True

# Surfaces
sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')

while gamelive :
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # When we call pygame.quit
            pygame.quit() # Quit the screen
            exit()

    screen.blit(sky_surface,(0,0)) # add one surface to annother
    screen.blit(ground_surface,(0,300)) # add the ground

# All our elements in here
# Where everything gets updated
    pygame.display.update()
    clock.tick(60) # No more than 60 frames per second
