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

score_surf = test_font.render('My Game',False,(64,64,64))
score_rect = score_surf.get_rect(center  = (400,50)) # create rectangle for score

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80,300)) # ground is at 300
player_gravity = 0

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (600,300))

while gamelive :
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # When we call pygame.quit
            pygame.quit() # Quit the screen
            exit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and player_rect.bottom >= 300:
            player_gravity = -20

        ''' if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                player_gravity = -20 '''
 
        if event.type == pygame.MOUSEBUTTONDOWN: # when the mouse moves
            if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300: # see if mouse collides with player rect
                player_gravity = -20


    screen.blit(sky_surface,(0,0)) # add one surface to annother
    screen.blit(ground_surface,(0,300)) # add the ground
    pygame.draw.rect(screen,"#c0e8ec",score_rect,0,5) # pink rectangle
    # pygame.draw.line(screen,"Gold",(0,0),pygame.mouse.get_pos(),10)
    screen.blit(score_surf,score_rect) # add the text
    snail_rect.x -=4 # move the snail -4 every iteration
    if snail_rect.right <=0: # check the rectangle position if it's less than 0
        snail_rect.left = 800 # reset the snail to 800
    screen.blit(snail_surface,(snail_rect)) # Put the snail on the screen using the rectangle

    #player
    player_gravity += 1 # Increase gravity by 1
    player_rect.y += player_gravity # apply the gravity to the player_rect
    if player_rect.bottom >= 300:
        player_rect.bottom = 300
    screen.blit(player_surf,player_rect) # apply rectangle to the screen
    player_rect.x += 5
    if player_rect.right >= 800:
        player_rect.right = 800
    elif player_rect.left <= 0:
        player_rect.left = 0
    
    ''' keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        print("jump") '''
    ''' if player_rect.colliderect(snail_rect):
        print("Collision")
    else:
        print("No Collision") '''
    
    ''' if player_rect.collidepoint(mouse_pos):
        print(pygame.mouse.get_pressed()) '''


# All our elements in here
# Where everything gets updated
    pygame.display.update()
    clock.tick(60) # No more than 60 frames per second