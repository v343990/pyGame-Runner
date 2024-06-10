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
test_font = pygame.font.Font('font/Pixeltype.ttf',50)

gamelive = True

# Surfaces
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My Game',False,'Black')
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (600,300))

while gamelive :
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # When we call pygame.quit
            pygame.quit() # Quit the screen
            exit()

    screen.blit(sky_surface,(0,0)) # add one surface to annother
    screen.blit(ground_surface,(0,300)) # add the ground
    screen.blit(text_surface,(350,50)) # add the text
    snail_rect.x -=4 # move the snail -4 every iteration
    if snail_rect.right <=0: # check the rectangle position if it's less than 0
        snail_rect.left = 800 # reset the snail to 800
    screen.blit(snail_surface,(snail_rect)) # Put the snail on the screen using the rectangle

# All our elements in here
# Where everything gets updated
    pygame.display.update()
    clock.tick(48) # No more than 60 frames per second
