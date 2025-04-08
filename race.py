import pygame  # type: ignore
import random

pygame.init()

screen = pygame.display.set_mode((400, 600))
road = pygame.image.load(r"C:\Users\User\OneDrive\Рабочий стол\aza\lab8\racer\AnimatedStreet.png")
my_car = pygame.image.load(r"C:\Users\User\OneDrive\Рабочий стол\aza\lab8\racer\Player.png")
cars = pygame.image.load(r"C:\Users\User\OneDrive\Рабочий стол\aza\lab8\racer\Enemy.png")
clock = pygame.time.Clock()

x = 185
y = 500
cars_x = random.uniform(60, 240)
cars_y = 0
speed = 6

score = 0
score_font = pygame.font.Font(None, 36)
coin_radius = 20
next_speed_increase = 5 

def generate_coin():
    coin_x = random.uniform(60, 240)
    coin_y = 0
    weight = random.randint(1, 3)  
    return [coin_x, coin_y, weight]

coin = generate_coin()


pygame.mixer.music.load(r"C:\Users\User\OneDrive\Рабочий стол\aza\lab8\racer\background.wav")
pygame.mixer.music.play(-1)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and x < 350:
        x += 5
    if keys[pygame.K_LEFT] and x > 0:
        x -= 5

    
    if cars_y >= 600:
        cars_y = 0
        cars_x = random.uniform(60, 240)
    else:
        cars_y += speed

    
    if (cars_x <= x <= cars_x + 40 or cars_x <= x + 40 <= cars_x + 40) and \
       (cars_y <= y <= cars_y + 80 or cars_y <= y + 80 <= cars_y + 80):
        screen.fill((255, 0, 0))
        pygame.mixer.music.stop()
        pygame.mixer.music.load(r"C:\Users\User\OneDrive\Рабочий стол\aza\lab8\racer\crash.wav")
        pygame.mixer.music.play()
        font = pygame.font.Font(None, 75)
        game_over = font.render("GAME OVER!", True, (0, 0, 0))
        screen.blit(game_over, (30, 300))
        pygame.display.update()
        pygame.time.wait(4000)
        break

    
    coin[1] += 3  
    if coin[1] >= 600:
        coin = generate_coin()

    
    if (y <= coin[1] <= y + 80 and x <= coin[0] <= x + 40) or \
       (y <= coin[1] + coin_radius <= y + 80 and x <= coin[0] + coin_radius <= x + 40):
        score += coin[2]  
        coin = generate_coin()

        
        if score >= next_speed_increase:
            speed += 1
            next_speed_increase += 5

    
    screen.blit(road, (0, 0))
    screen.blit(cars, (cars_x, cars_y))
    pygame.draw.circle(screen, (255, 215, 0), (int(coin[0]), int(coin[1])), coin_radius)  
    screen.blit(my_car, (x, y))

    
    score_text = score_font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
