#coding=utf-8
import pygame, sys
from pygame.locals import *
from random import *

pygame.init()

bg_size = width, height = 1440, 900

screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("15计科1班专业抽（keng）号（ren）软件")

num = 0 #初始化号码

font = pygame.font.Font("font/font.ttf", 550)

text_font = pygame.font.Font("font/font.ttf", 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                num = randint(1, 45)

        text_image = text_font.render("Next LUCKY number is :", True, (0, 0 ,0))

        text_image_rect = text_image.get_rect()

        text_image_rect.left, text_image_rect.top = (width - text_image_rect.width) // 2, 50

        num_image = font.render(str(num), True, (0, 0, 0))

        num_image_rect = num_image.get_rect()

        num_image_rect.left, num_image_rect.top = (width - num_image_rect.width) // 2, (height - num_image_rect.height) // 2

        screen.fill((255, 255, 255))

        screen.blit(text_image, text_image_rect)

        screen.blit(num_image, num_image_rect)

        pygame.display.flip()

        pygame.time.delay(20)

