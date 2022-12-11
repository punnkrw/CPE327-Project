import pygame, sys, os

def displayHowTo(screen, background):
    #insert game's how to play image 
    background = pygame.image.load("Background/NewHowTo.png")
    screen.blit(background,(0,0))

    pygame.display.update() #update

    #back to menu
    showHint = True
    while showHint:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                showHint = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                showHint = False
