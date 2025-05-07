import pygame
import random

# Initialize
pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Simple Snake Game")
clock = pygame.time.Clock()

# Snake setup
block_size = 20
snake = [pygame.Rect(250, 250, block_size, block_size)]
direction = pygame.K_RIGHT

# Food setup
food = pygame.Rect(random.randint(0, 24) * block_size,
                   random.randint(0, 24) * block_size,
                   block_size, block_size)

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Main loop
running = True
speed = 3



def game_over_screen(win, score):
    font = pygame.font.SysFont('Arial', 40)
    small_font = pygame.font.SysFont('Arial', 25)

    text = font.render('Game Over', True, (255, 0, 0))
    score_text = small_font.render(f'Score: {score}', True, (255, 255, 255))
    restart_text = small_font.render('Press R to Restart or Q to Quit', True, (200, 200, 200))

    win.fill((0, 0, 0))
    win.blit(text, (130, 150))
    win.blit(score_text, (190, 210))
    win.blit(restart_text, (100, 270))
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False  # Exit screen and restart game
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()


while running:
    clock.tick(speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Directional input
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                # Prevent snake from going backwards
                if (event.key == pygame.K_UP and direction != pygame.K_DOWN) or \
                   (event.key == pygame.K_DOWN and direction != pygame.K_UP) or \
                   (event.key == pygame.K_LEFT and direction != pygame.K_RIGHT) or \
                   (event.key == pygame.K_RIGHT and direction != pygame.K_LEFT):
                    direction = event.key

    # Move the snake
    head = snake[0].copy()
    if direction == pygame.K_UP:
        head.y -= block_size
    elif direction == pygame.K_DOWN:
        head.y += block_size
    elif direction == pygame.K_LEFT:
        head.x -= block_size
    elif direction == pygame.K_RIGHT:
        head.x += block_size

    # Check collisions
    if head.collidelist(snake) != -1 or head.x < 0 or head.y < 0 or head.x >= 500 or head.y >= 500:
        game_over_screen(win, len(snake) - 1)  # show screen with score
        # Restart the game by reinitializing variables
        snake = [pygame.Rect(250, 250, block_size, block_size)]
        direction = pygame.K_RIGHT
        food.x = random.randint(0, 24) * block_size
        food.y = random.randint(0, 24) * block_size

    snake.insert(0, head)

    if head.colliderect(food):
        speed += 2
        food.x = random.randint(0, 24) * block_size
        food.y = random.randint(0, 24) * block_size
    else:
        snake.pop()

    # Drawing
    win.fill(BLACK)
    for segment in snake:
        pygame.draw.rect(win, WHITE, segment)
    pygame.draw.rect(win, RED, food)
    pygame.display.update()

pygame.quit()
