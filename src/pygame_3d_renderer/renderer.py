import pygame
from . import vector
from . import Polygon

X_SIZE = 1280
Y_SIZE = 1024


octahedron = [
[(1,0,0), (0,1,0), (0,0,1)],
[(1,0,0), (0,0,-1), (0,1,0)],
[(1,0,0), (0,0,1), (0,-1,0)],
[(1,0,0), (0,-1,0), (0,0,-1)],
[(-1,0,0), (0,0,1), (0,1,0)],
[(-1,0,0), (0,1,0), (0,0,-1)],
[(-1,0,0), (0,-1,0), (0,0,1)],
[(-1,0,0), (0,0,-1), (0,-1,0)],
]


def render():
    """Open a window and draw a triangle until the window is closed."""
    pygame.init()
    
    screen = pygame.display.set_mode((X_SIZE, Y_SIZE))
    pygame.display.set_caption("Simple Pygame Triangle")
    clock = pygame.time.Clock()

    polygons = render_object(octahedron, (1, 2, 3))

  
    background_color = (30, 30, 30)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(background_color)

        for p in polygons:
            p_vertices = []
            for v in p.vertices:
                p_vertices.append(map_from_cartesian_to_pixels(vector.scale(400, v)))
            pygame.draw.polygon(screen, p.color, p_vertices)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

def render_object(faces, light):
    unit_light = vector.unit(light)
    polygons = []
    for face in faces:
        n = vector.unit(vector.normal(face))
        if (n[2] > 0): #camera positioned at z axis
            face_2d = vector.face_to_2d(face)
            print(face_2d)
            print(vector.dot_product(n, unit_light))
            color = color_map(vector.dot_product(n, unit_light))
            print(color)
            polygons.append(Polygon(vertices=face_2d, color=color))
    return polygons


def color_map(intensity):
    intensity = max(0, intensity)
    dark_blue = (0., 15., 45.)
    light_blue = (180., 225., 255.)
    color = vector.add(dark_blue, vector.scale(intensity, vector.subtract(light_blue, dark_blue)))

    return color



def map_from_cartesian_to_pixels(vector):
    pixel_x_zero =  X_SIZE/2
    pixel_y_zero = Y_SIZE/2

    x,y = vector
    new_x = pixel_x_zero + x
    new_y = pixel_y_zero - y

    return (new_x, new_y)
    


if __name__ == "__main__":
    render()




