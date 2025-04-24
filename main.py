import pygame
import random
from apple import Apple
from snake import Snake
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
fps = 60

snake = Snake()
apple = Apple()

running = True
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif keys[pygame.K_ESCAPE]:
            running = False
        elif keys[pygame.K_w]:
            snake.snake_pos[1] -= 10
        elif keys[pygame.K_a]:
            snake.snake_pos[0] -= 10
        elif keys[pygame.K_s]:
            snake.snake_pos[1] += 10
        elif keys[pygame.K_d]:
            snake.snake_pos[0] += 10

    snake.body.insert(0, list(snake.snake_pos))
    snake.body.pop()

    screen.fill(color=(0, 0, 0))

    apple.draw()

    for position in snake.body:
        pygame.draw.rect(screen, snake.snake_color, pygame.Rect(position[0], position[1], snake.size, snake.size))


    for i in range(len(apple.apples)):
        if (pygame.Rect(snake.snake_pos[0], snake.snake_pos[1], snake.size, snake.size)).colliderect(apple.apples[i]):
            snake.body.append(apple.apples[i])
            apple.surf[i].fill(color=(0, 0, 0))
            apple.cleared[i] = "cleared"
        elif (apple.cleared[0] == "cleared") and (apple.cleared[1] == "cleared") and (apple.cleared[2] == "cleared") and (apple.cleared[3] == "cleared") and (apple.cleared[4] == "cleared"):
            print("You win!")
        for event in pygame.event.get():
            if keys[pygame.K_w]:
                snake.snake_pos[1] -= 30
            elif keys[pygame.K_a]:
                snake.snake_pos[0] -= 30
            elif keys[pygame.K_s]:
                snake.snake_pos[1] += 30
            elif keys[pygame.K_d]:
                snake.snake_pos[0] += 30


    if (snake.snake_pos[0] < 0) or (snake.snake_pos[0] > 750):
        print("Game over!")
    elif (snake.snake_pos[1] < 0) or (snake.snake_pos[1] > 750):
        print("Game Over!")


    pygame.display.update()
    clock.tick(fps)
