import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Drawing App")
    clock = pygame.time.Clock()

    radius = 5
    mode = 'blue'  
    draw_mode = 'line'  
    drawing = False
    start_pos = None
    base_layer = pygame.Surface((640, 480))
    base_layer.fill((0, 0, 0))

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held or \
                   event.key == pygame.K_F4 and alt_held or \
                   event.key == pygame.K_ESCAPE:
                    return

                
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_y:
                    mode = 'yellow'
                elif event.key == pygame.K_w:
                    mode = 'white'

                
                if event.key == pygame.K_F1:
                    draw_mode = 'line'
                elif event.key == pygame.K_F2:
                    draw_mode = 'rect'
                elif event.key == pygame.K_F3:
                    draw_mode = 'circle'
                elif event.key == pygame.K_F4:
                    draw_mode = 'square'
                elif event.key == pygame.K_F5:
                    draw_mode = 'rt_triangle'
                elif event.key == pygame.K_F6:
                    draw_mode = 'eq_triangle'
                elif event.key == pygame.K_F7:
                    draw_mode = 'rhombus'
                elif event.key == pygame.K_e:
                    draw_mode = 'eraser'

                
                if event.key == pygame.K_UP:
                    radius = min(100, radius + 1)
                elif event.key == pygame.K_DOWN:
                    radius = max(1, radius - 1)

            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                drawing = True
                start_pos = event.pos

            
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                end_pos = event.pos
                color = get_color(mode)
                if draw_mode == 'rect':
                    pygame.draw.rect(base_layer, color, get_rect(start_pos, end_pos), radius)
                elif draw_mode == 'circle':
                    center = start_pos
                    radius_circ = int(math.hypot(end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
                    pygame.draw.circle(base_layer, color, center, radius_circ, radius)
                elif draw_mode == 'square':
                    draw_square(base_layer, start_pos, end_pos, color, radius)
                elif draw_mode == 'rt_triangle':
                    draw_right_triangle(base_layer, start_pos, end_pos, color, radius)
                elif draw_mode == 'eq_triangle':
                    draw_equilateral_triangle(base_layer, start_pos, end_pos, color, radius)
                elif draw_mode == 'rhombus':
                    draw_rhombus(base_layer, start_pos, end_pos, color, radius)
                drawing = False

            
            if event.type == pygame.MOUSEMOTION and drawing:
                if draw_mode == 'line':
                    pygame.draw.circle(base_layer, get_color(mode), event.pos, radius)
                elif draw_mode == 'eraser':
                    pygame.draw.circle(base_layer, (0, 0, 0), event.pos, radius)

        screen.blit(base_layer, (0, 0))
        pygame.display.flip()
        clock.tick(60)



def get_color(mode):
    colors = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'yellow': (255, 255, 0),
        'white': (255, 255, 255)
    }
    return colors.get(mode, (255, 255, 255))



def get_rect(start, end):
    x1, y1 = start
    x2, y2 = end
    left = min(x1, x2)
    top = min(y1, y2)
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    return pygame.Rect(left, top, width, height)



def draw_square(surface, start, end, color, width):
    x1, y1 = start
    x2, y2 = end
    side = min(abs(x2 - x1), abs(y2 - y1))
    rect = pygame.Rect(x1, y1, side if x2 >= x1 else -side, side if y2 >= y1 else -side)
    pygame.draw.rect(surface, color, rect, width)



def draw_right_triangle(surface, start, end, color, width):
    x1, y1 = start
    x2, y2 = end
    points = [start, (x2, y1), (x2, y2)]
    pygame.draw.polygon(surface, color, points, width)



def draw_equilateral_triangle(surface, start, end, color, width):
    x1, y1 = start
    x2, y2 = end
    base = math.dist((x1, y1), (x2, y2))
    mid = ((x1 + x2) // 2, (y1 + y2) // 2)
    height = base * math.sqrt(3) / 2
    direction = -1 if y2 < y1 else 1
    p1 = (x1, y2)
    p2 = (x2, y2)
    p3 = (mid[0], y2 + direction * height)
    pygame.draw.polygon(surface, color, [p1, p2, p3], width)



def draw_rhombus(surface, start, end, color, width):
    x1, y1 = start
    x2, y2 = end
    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2
    dx = abs(x2 - x1) // 2
    dy = abs(y2 - y1) // 2
    points = [(cx, y1), (x2, cy), (cx, y2), (x1, cy)]
    pygame.draw.polygon(surface, color, points, width)

main()
