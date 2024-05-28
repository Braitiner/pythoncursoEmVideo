# Faça um programa em Python que abra e reproduza o audio de um arquivo MP3

import pygame

pygame.init()
pygame.mixer.music.load('D:/prog/Python/Curso_em_video/Mp3/my.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
