import pygame
import sys
import config # Import the config module

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True


# Write a function under this comment that lets you draw one or more rectangles
# on your Pygame window

def draw_rectangle(screen, color, rect_info, thickness):
    '''Draws a rectangle in the Pygame window.'''
    pygame.draw.rect(screen, color, rect_info, thickness)







def main():
    screen = init_game()
    clock = pygame.time.Clock() # Initialize the clock here

    running = True
    while running:
        running = handle_events()
        screen.fill(config.WHITE) # Use color from config



        # Give Python some info about what we want the rectangle to look like
       
        thickness = 0

        draw_rectangle(screen, config.GREEN, [250, 85, 350, 200], thickness)
    








        
        
        
        
        
        pygame.display.flip()

        # Limit the frame rate to the specified frames per second (FPS) 
        clock.tick(config.FPS)

    
    pygame.quit()
    sys.exit()

if __name__== "__main__":
    main()

