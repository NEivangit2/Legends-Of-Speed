from pygame import *
from random import randint
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

screen = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Legends Of Speed')

bg_image = image.load('road1.png')
bg_image = transform.scale(bg_image, (WIDTH, HEIGHT))

player_img = image.load('playercar.png').convert_alpha()
player_img = transform.scale(player_img, (150, 225))
player_rect = player_img.get_rect()
player_rect.center = (WIDTH // 2, HEIGHT - 150)

enemy_img = image.load('enemycar.png').convert_alpha()
enemy_img = transform.scale(enemy_img, (150, 225))

enemies = []
enemy_speed = 5
spawn_timer = 0

clock = time.Clock()
player_speed = 7
FPS = 60
game_over = False
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    if not game_over:
        keys = key.get_pressed()
        if keys[K_LEFT]:
            player_rect.x -= player_speed
        if keys[K_RIGHT]:
            player_rect.x += player_speed

        spawn_timer += 1
        if spawn_timer > 75:
            new_enemy_rect = enemy_img.get_rect(midtop=(randint(50, WIDTH-50), -100))
            enemies.append(new_enemy_rect)
            spawn_timer = 0

        screen.blit(bg_image, (0, 0))
        screen.blit(player_img, player_rect)
        
        for enemy in enemies:
            screen.blit(enemy_img, enemy)
        
        for enemy in enemies[:]:
            enemy.y += enemy_speed

            if enemy.top > HEIGHT:
                enemies.remove(enemy)
            
            if player_rect.colliderect(enemy):
                game_over = True
    
    else:
        screen.fill((200, 0, 0))

    display.flip()
    clock.tick(60)
quit()