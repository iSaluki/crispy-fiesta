import pygame

pygame.display.init()

# Create a window to house the simulation

frame = pygame.display.set_mode(size=(1920,1080))
pygame.display.set_caption("Traffic Light Simulation")

# Variable definitions
fps = 30    
fpsClock = pygame.time.Clock()
keepLooping = True

while keepLooping:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    # Create a blank frame
    frame.fill((255,255,255))
    # Draw the frame content
    pygame.draw.rect(frame,(0,0,0), pygame.Rect(0,500,1920,100))
    


    # Handle display update
    pygame.display.flip()
    fpsClock.tick(fps)

