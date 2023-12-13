import pygame
def music():
    c = ["Music/track_0.mp3", "Music/track_1.mp3", "Music/track_2.mp3", "Music/track_3.mp3", "Music/track_4.mp3",
     "Music/track_5.mp3"]
    pygame.mixer.music.load(c[0])
    pygame.mixer.music.play()
    pygame.mixer.music.queue(c[1])
    pygame.mixer.music.queue(c[2])
    pygame.mixer.music.queue(c[3])
    pygame.mixer.music.queue(c[4])