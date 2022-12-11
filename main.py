import pygame,sys
from button import Button

#import game
from Mathgame import math_home
from puzzle import puzzle_home
from StroopEffect import stroop_home
from photohunt import photohunt_home


pygame.init()

SCREEN = pygame.display.set_mode((640,480))
pygame.display.set_caption("Brianify")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

BG = pygame.image.load("Background/Background2.png")
BG2 = pygame.image.load("Background/INTRO1.png")
close_button = pygame.image.load('assets/close.png')
close_button = pygame.transform.scale(close_button, (30, 30))
width = SCREEN.get_width()
height = SCREEN.get_height()

def show_desp(name1,name2,items):
    while True:
        SCREEN.blit(BG2, (0, 0))
        BUTTON_MOUSE_POS = pygame.mouse.get_pos()

        button = pygame.image.load('assets/black rect.png')
        button = pygame.transform.scale(button, (240, 130))

        OPTIONS_TEXT = get_font(50).render(name1, True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(330, 60))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_TEXT = get_font(50).render(name2, True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(330, 120))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        for index, item in enumerate(items):
            label = get_font(14).render(item,True,'Black')
            width = label.get_width()
            height = label.get_height() + 10

            posX = (640 /2) - (width /2)
            t_h = len(items) * height
            posY = (280) - (t_h /2) + (index * height)

            SCREEN.blit(label,(posX,posY))

        EXIT_BUTTON = Button(image=button, pos=(100, 420), 
                            text_input="EXIT", font=get_font(20), base_color="White", hovering_color="Red")
        
        EXIT_BUTTON.changeColor(BUTTON_MOUSE_POS)
        EXIT_BUTTON.update(SCREEN)

        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EXIT_BUTTON.checkForInput(BUTTON_MOUSE_POS):
                    options()

        pygame.display.update()


def options():
    while True:
        SCREEN.blit(BG2, (0, 0))

        OPTION_MOUSE_POS = pygame.mouse.get_pos()
        icon_rect = pygame.image.load('assets/icon bg.png')

        QUICKMATH = Button(image=icon_rect, pos=(180, 130), 
                            text_input=None, font=get_font(23), base_color="White", hovering_color="Red")
        PUZZLE = Button(image=icon_rect, pos=(460, 130), 
                            text_input=None, font=get_font(23), base_color="White", hovering_color="Red")
        PHOTOHUNT = Button(image=icon_rect, pos=(180, 350), 
                            text_input=None, font=get_font(23), base_color="White", hovering_color="Red")
        STROOPEFFECT = Button(image=icon_rect, pos=(460, 350), 
                            text_input=None, font=get_font(23), base_color="White", hovering_color="Red")
        EXIT_BUTTON = Button(image=close_button, pos=(40, 40), 
                            text_input=None, font=get_font(23), base_color="White", hovering_color="Red")

        for button in [QUICKMATH, PUZZLE, PHOTOHUNT, STROOPEFFECT, EXIT_BUTTON]:
                button.changeColor(OPTION_MOUSE_POS)
                button.update(SCREEN)

        SCREEN.blit(pygame.image.load('assets/quick math.png'),(88,10))
        SCREEN.blit(pygame.image.load('assets/puzzle.png'),(335,38))
        SCREEN.blit(pygame.image.load('assets/photohunt.png'),(100,255))
        SCREEN.blit(pygame.image.load('assets/stroop effect.png'),(380,260))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
            	if QUICKMATH.checkForInput(OPTION_MOUSE_POS):
            		show_desp("MATH","GAME", items = ("Mathematical thinking involves complex,","interconnected brain functions to perform",
                            "even the simplest functions. This leads to","a decrease in the deterioration of ",
                            "cogniitive functions that occurs over time", "and with it the probability of suffering",
                            "from Alzheimer’s"))
            	if PUZZLE.checkForInput(OPTION_MOUSE_POS):
            		show_desp("PUZZLE",None, items = ("Puzzles is a way of stimulating our", "brains, improving our hand eye",
                            "coordination, thinking and memory skills", "For someone with dementia, completing",
                            "a puzzle can give them the 'feel-good'","effect, which is the production of dopamine",
                            "in the brain, leaving them feeling happy and ","that they've enjoyed their time ",
                            "completing puzzle."))
            	if PHOTOHUNT.checkForInput(OPTION_MOUSE_POS):
            		show_desp("PHOTO","HUNT", items = ("When looking at two picture, Players must", "stimulate their long-term memory to",
                            "remember what you see in one picture and","compare it to what you see in the other",
                            "picture.Short-term memory is also necessary", "when finding a location to", 
                            "accommodate a number of differences ","between two similar images."))
            	if STROOPEFFECT.checkForInput(OPTION_MOUSE_POS):
            		show_desp("STROOP","EFFECT", items = ("The Stroop effect is brain training games","that enhances hand-eye coordination and",
                            "stimulates the hippocampus, the area of", "the brain connected with spatial and",
                            "temporal memory."))
            	if EXIT_BUTTON.checkForInput(OPTION_MOUSE_POS):
            		introduce()

        pygame.display.update()

def introduce():
    while True:
        SCREEN.blit(BG, (0, 0))

        INTRO_MOUSE_POS = pygame.mouse.get_pos()

        INTRO_TEXT = get_font(38).render("INTRODUCE", True, "Black")
        INTRO_RECT = INTRO_TEXT.get_rect(center=(330, 170))
        SCREEN.blit(INTRO_TEXT, INTRO_RECT)

        INTRO_TEXT = get_font(38).render("MY GAME", True, "Black")
        INTRO_RECT = INTRO_TEXT.get_rect(center=(330, 240))
        SCREEN.blit(INTRO_TEXT, INTRO_RECT)

        rect = pygame.transform.scale(pygame.image.load('assets/black rect.png'), (350, 170))

        INTRO_NEXT = Button(image=rect, pos=(460, 360), 
                            text_input="NEXT", font=get_font(23), base_color="White", hovering_color="Red")
        INTRO_BACK = Button(image=close_button, pos=(40, 40), 
                            text_input=None, font=get_font(23), base_color="Black", hovering_color="Red")
        
        for button in [INTRO_NEXT,INTRO_BACK]:
                button.changeColor(INTRO_MOUSE_POS)
                button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INTRO_NEXT.checkForInput(INTRO_MOUSE_POS):
                    options()
                if INTRO_BACK.checkForInput(INTRO_MOUSE_POS):
                    homepage()

        pygame.display.update()

def process_game_1():
    while True:
        SCREEN.blit(BG2, (0, 0))

        MOUSE_POS = pygame.mouse.get_pos()
        icon_rect = pygame.image.load('assets/icon bg.png')
        button_rect = pygame.transform.scale(pygame.image.load('assets/black rect.png'), (300, 160))

        QUICKMATH = Button(image=icon_rect, pos=(180, 200), 
                        text_input=None, font=get_font(23), base_color="White", hovering_color="Red")
        PUZZLE = Button(image=icon_rect, pos=(450, 200), 
                        text_input=None, font=get_font(23), base_color="White", hovering_color="Red")
        OPTIONS_BACK = Button(image=button_rect, pos=(510, 420), 
                        text_input="homepage", font=get_font(15), base_color="White", hovering_color="Red")
        OPTIONS_NEXT = Button(image=None, pos=(600, 210), 
                        text_input=" > ", font=get_font(40), base_color="Black", hovering_color="Red")
        

        for button in [QUICKMATH, PUZZLE, OPTIONS_BACK, OPTIONS_NEXT]:
                button.changeColor(MOUSE_POS)
                button.update(SCREEN)

        SCREEN.blit(pygame.image.load('assets/quick math.png'),(80,90))
        SCREEN.blit(pygame.image.load('assets/puzzle.png'),(330,110))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(MOUSE_POS):
                    homepage()
                if OPTIONS_NEXT.checkForInput(MOUSE_POS):
                    process_game_2()
                if QUICKMATH.checkForInput(MOUSE_POS):
                    math_home()
                if PUZZLE.checkForInput(MOUSE_POS):
                    puzzle_home()

        pygame.display.update()


def process_game_2():
    while True:
        SCREEN.blit(BG2, (0, 0))

        MOUSE_POS = pygame.mouse.get_pos()
        icon_rect = pygame.image.load('assets/icon bg.png')
        button_rect = pygame.transform.scale(pygame.image.load('assets/black rect.png'), (300, 160))

        PHOTOHUNT = Button(image=icon_rect, pos=(180, 200), text_input=None,
                            font=get_font(23), base_color="White", hovering_color="Red")
        STROOPEFFECT = Button(image=icon_rect, pos=(460, 200), text_input=None, 
                            font=get_font(23), base_color="White", hovering_color="Red")
        OPTIONS_BACK = Button(image=None, pos=(30, 210), text_input=" < ",
                             font=get_font(40), base_color="Black", hovering_color="Red")
        MENU_BUTTON = Button(image=button_rect, pos=(510, 420), text_input="homepage",
                             font=get_font(15), base_color="White", hovering_color="Red")
        

        for button in [PHOTOHUNT, STROOPEFFECT, OPTIONS_BACK, MENU_BUTTON]:
                button.changeColor(MOUSE_POS)
                button.update(SCREEN)

        photo_icon = pygame.image.load('assets/photohunt.png')
        SCREEN.blit(photo_icon,(100,110))
        stroop_icon = pygame.image.load('assets/stroop effect.png')
        SCREEN.blit(stroop_icon,(390,110))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PHOTOHUNT.checkForInput(MOUSE_POS):
                    photohunt_home()
                if STROOPEFFECT.checkForInput(MOUSE_POS):
                    stroop_home()
                if OPTIONS_BACK.checkForInput(MOUSE_POS):
                    process_game_1()
                if MENU_BUTTON.checkForInput(MOUSE_POS):
                    homepage()

        pygame.display.update()

def homepage():
    while True:
        SCREEN.blit(pygame.image.load("Background/MENU.png"), (0, 0))

        MOUSE_POS = pygame.mouse.get_pos()
        blue_rect = pygame.transform.scale(pygame.image.load('assets/message.png'), (800, 600))
        SCREEN.blit(blue_rect,(-60,-10))
        yellow_rect = pygame.transform.scale(pygame.image.load('assets/messageyel.png'), (335, 78))

        MENU_BUTTON = Button(image=yellow_rect, pos=(340, 243), text_input="CHOOSE GAME", 
                        font=get_font(28), base_color="White", hovering_color="Red")
        INTRODUCE_BUTTON = Button(image=yellow_rect, pos=(340, 326), text_input="INTRODUCE",
                        font=get_font(28), base_color="White", hovering_color="Red")
        
        for button in [MENU_BUTTON, INTRODUCE_BUTTON]:
                button.changeColor(MOUSE_POS)
                button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_BUTTON.checkForInput(MOUSE_POS):
                    process_game_1()
                if INTRODUCE_BUTTON.checkForInput(MOUSE_POS):
                	introduce()

        pygame.display.update()

homepage()