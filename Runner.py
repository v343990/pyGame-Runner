import pygame
from sys import exit # just to close game

def display_score():
    current_time = int(pygame.time.get_ticks() / 100) - start_time
    score_surf = test_font.render(f'{current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)

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
start_time = 0

# Surfaces
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

#  Background positions
sky_x_pos = 0
sky_x_pos1 = screen_width
ground_x_pos = 0
ground_x_pos1 = screen_width
scroll_speed = 5

left_boundary = 200
right_boundary = screen_width - 200

# score_surf = test_font.render('My Game',False,(64,64,64))
# score_rect = score_surf.get_rect(center  = (400,50)) # create rectangle for score

# player stuff
player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80,300)) # ground is at 300
player_gravity = 0
player_speed = 5



snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (600,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # When we call pygame.quit
            pygame.quit() # Quit the screen
            exit()

        ''' if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                player_gravity = -20 '''
 
        if event.type == pygame.MOUSEBUTTONDOWN: # when the mouse moves
            if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300: # see if mouse collides with player rect
                player_gravity = -20

    if gamelive:
        

        # Player Movement with scrolling background
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if player_rect.right < right_boundary: # If not within boundary then
                player_rect.x += player_speed      # player will move to the boundary
            else:
                sky_x_pos -= player_speed   
                sky_x_pos1 -= player_speed        # If in boundary sky and ground
                ground_x_pos -= player_speed      # Sky and ground will move instead
                ground_x_pos1 -= player_speed
        if keys[pygame.K_LEFT]:
            if player_rect.left > left_boundary:
                player_rect.x -= player_speed
            else:
                sky_x_pos += player_speed
                sky_x_pos1 += player_speed
                ground_x_pos += player_speed
                ground_x_pos1 +- player_speed

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and player_rect.bottom >= 300:
            player_gravity = -20
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player_rect.bottom >= 300:
            player_gravity = -20
        
        screen.blit(sky_surface,(sky_x_pos, 0)) # add one surface to another
        screen.blit(sky_surface, (sky_x_pos1, 0))
        screen.blit(ground_surface,(ground_x_pos, 300)) # add the ground
        screen.blit(ground_surface,(ground_x_pos1, 300))

        # pygame.draw.rect(screen,"#c0e8ec",score_rect,0,5) # pink rectangle
        # pygame.draw.line(screen,"Gold",(0,0),pygame.mouse.get_pos(),10)
        # screen.blit(score_surf,score_rect) # add the text
        display_score()
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
        '''if player_rect.right < 0:
            player_rect.left = screen_width
        if player_rect.left > screen_width:
            player_rect.right = 0 '''
        
        if snail_rect.colliderect(player_rect):
            gamelive = False
    else:
        screen.fill((25,200,16))
        end_surf = test_font.render("Game Over",False,(64,64,64))
        end_rect = end_surf.get_rect(center = (400,50))
        screen.blit(end_surf,end_rect)
        playagain_surf = test_font.render("Play Again?",False,"Black")
        playagain_rect = playagain_surf.get_rect(center = (400, 150))
        screen.blit(playagain_surf,playagain_rect)
        quit_surf = test_font.render("Quit",False,"Red")
        quit_rect = quit_surf.get_rect(center = (400,350))
        screen.blit(quit_surf,quit_rect)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if quit_rect.collidepoint(event.pos):
                pygame.quit()
                exit()
                       
        if event.type == pygame.MOUSEBUTTONDOWN:
            if playagain_rect.collidepoint(event.pos):
                gamelive = True
                snail_rect.left = 800
                player_rect.left = 80
                start_time = int(pygame.time.get_ticks() / 100)
            
# All our elements in here
# Where everything gets updated
    pygame.display.update()
    clock.tick(60) # No more than 60 frames per second