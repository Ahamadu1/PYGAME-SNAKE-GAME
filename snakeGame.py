import pygame
pygame.init()
import random
win = pygame.display.set_mode((500,500))
x = 250
y = 250
width = 40
height = 40
speed = 1
run = True
x_axis = True
border =  False
food = pygame.Surface((50, 40))
food.fill((250,250,250))
foodrect = food.get_rect()
foodrect.x = random.randint(0,460)
foodrect.y = random.randint(0,440)
foodw = 40
foodh = 40
image = pygame.Surface((50, 40))
image.fill((250,250,250))
rect = image.get_rect()
rect.centerx = 250
rect.centery = 250
add = False
rectx = [rect]
recty = [rect.y]
def check_border():
    global border
    global x, y


    if rect.x < 0:
        rect.x = 0
    elif rect.x > 460:
        rect.x = 460
    if rect.y < 0:
        rect.y = 0
    elif rect.y > 440:

        rect.y = 440
running = True
while running:
    pygame.time.delay(15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x_axis = True
                speed = 2
            if  event.key == pygame.K_LEFT:
                x_axis = True
                speed = -2
            if  event.key == pygame.K_UP:
                x_axis = False
                speed = -2


            if  event.key == pygame.K_DOWN:
                x_axis = False
                speed = 2


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                x_axis = True
                speed = 2
                print(speed)
            if event.key == pygame.K_LEFT:
                x_axis = True
                speed = -2

            if  event.key == pygame.K_UP:
                x_axis = False
                speed = -2

            if  event.key == pygame.K_DOWN:
                x_axis = False
                speed = 2

    check_border()
    if x_axis:
        rect.x += speed

    elif not x_axis:
        rect.y += speed

    if rect.colliderect(foodrect):
        foodrect.x = random.randint(0, 460)
        foodrect.y = random.randint(0, 440)
        add = True

    if add:
        nrect = image.get_rect()
        # nrect.left = (rectx[-1]).right
        nrect.x = (rectx[-1]).x + 41

        rectx.append(nrect)







    win.fill(0)

    for rect in rectx:
        pygame.draw.rect(win,(255,255,255),(rect))

    pygame.draw.rect(win, (255, 0, 0), (foodrect))
    pygame.display.update()
    # pygame.draw.all_sprites.rect(win)
    pygame.display.flip()
pygame.quit()