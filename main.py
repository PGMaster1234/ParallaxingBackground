import pygame
# import random
pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width = screen.get_width()
screen_height = screen.get_height()

clock = pygame.time.Clock()

layer1 = pygame.image.load('layer1.png').convert_alpha().convert()
layer2 = pygame.image.load('layer2.png').convert_alpha().convert()
layer3 = pygame.image.load('layer3.png').convert_alpha().convert()
layer4 = pygame.image.load('layer4.png').convert_alpha().convert()
layer5 = pygame.image.load('layer5.png').convert_alpha().convert()
layer6 = pygame.image.load('layer6.png').convert_alpha()
# layer7 = pygame.image.load('Screen Shot 2022-03-06 at 6.40.43 PM.png').set_alpha(50)
layer1.set_colorkey((255, 255, 255))
layer2.set_colorkey((255, 255, 255))
layer3.set_colorkey((255, 255, 255))
layer4.set_colorkey((255, 255, 255))
layer5.set_colorkey((255, 255, 255))
layer6.set_colorkey((255, 255, 255))
# layer7.set_colorkey((255, 255, 255))


# put in layers in the order where the foreground is the last one in the list
layers = [[layer1, 0], [layer2, 0], [layer3, 0], [layer4, 0], [layer5, 0], [layer6, 0]]
distance = 0.8
blit_speed = 1
speed = 3
x = 0
moving_right = False
moving_left = False

running = True
while running:
    mx, my = pygame.mouse.get_pos()

    screen.fill((200, 200, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_LEFT:
                moving_left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_LEFT:
                moving_left = False

    blit_speed = speed
    for layer in layers:
        if moving_right:
            layer[1] -= blit_speed
        if moving_left:
            layer[1] += blit_speed
        blit_speed /= distance
        round(blit_speed)
        count = 0
        for i in range(10):
            screen.blit(layer[0], (layer[1] + (screen_width*count), 0))
            count += 1

    fps = clock.get_fps()
    fps_rounded = round(fps * 10000000) / 10000000
    print(fps)

    pygame.display.update()
    clock.tick(60)
