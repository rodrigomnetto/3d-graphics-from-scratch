import pygame
from . import vector

X_SIZE = 1280
Y_SIZE = 1024

def render():
    """Open a window and draw a triangle until the window is closed."""
    pygame.init()


    
    screen = pygame.display.set_mode((X_SIZE, Y_SIZE))
    pygame.display.set_caption("Simple Pygame Triangle")
    clock = pygame.time.Clock()

    cartesian_triangle = [(-100, 0), (0, 100), (100, 0)]

    cartesian_triangle = vector.rotate_2d_polygon(180, cartesian_triangle)
    
    triangle = list(map(map_from_cartesian_to_pixels, cartesian_triangle))
    background_color = (30, 30, 30)
    triangle_color = (70, 180, 255)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(background_color)
        pygame.draw.polygon(screen, triangle_color, triangle)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()




def map_from_cartesian_to_pixels(vector):
    pixel_x_zero =  X_SIZE/2
    pixel_y_zero = Y_SIZE/2

    x,y = vector
    new_x = pixel_x_zero + x
    new_y = pixel_y_zero + y

    return (new_x, new_y)
    


if __name__ == "__main__":
    render()




