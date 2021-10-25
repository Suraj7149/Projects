import pygame

pygame.mixer.init()

def play():
    song = "G:\Song\Jefferson Airplane -White Rabbit-.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=1)

play()