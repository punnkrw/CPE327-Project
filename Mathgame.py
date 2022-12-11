import pygame, sys, random, time
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((640,480))
pygame.display.set_caption("Quick Math")

# load background image
BG = pygame.image.load("Background/QUIZE MATH.png")
# create the score counter
scores=[0]*10

# load image for creating closing button
close_button = pygame.image.load('assets/close.png')
close_button = pygame.transform.scale(close_button, (30, 30))

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def get_font2(size): # Returns Raleway Black in the desired size
    return pygame.font.SysFont("Raleway Black", size)

# These will set num1,num2,result for addition, subtraction, multiplication 
#  and division. 
def set_problem(problem):
    if problem["operation"] == " + ":
        problem["num1"] = random.randint(0,99)
        problem["num2"] = random.randint(0,99)
        problem["result"] = problem["num1"] + problem["num2"]
        randnum = [random.randint(1,198),random.randint(1,198),random.randint(1,198)]
    elif problem["operation"] == " - ":
        problem["num1"] = random.randint(0,99)
        problem["num2"] = random.randint(0,99)
        if problem["num2"] > problem["num1"]:
            problem["num2"], problem["num1"] = problem["num1"], problem["num2"]
        problem["result"] = problem["num1"] - problem["num2"]
        randnum = [random.randint(1,99),random.randint(1,99),random.randint(1,99)]
    elif problem["operation"] == " x ":
        problem["num1"] = random.randint(0,12)
        problem["num2"] = random.randint(0,12)
        problem["result"] = problem["num1"] * problem["num2"]
        randnum = [random.randint(1,144),random.randint(1,144),random.randint(1,144)]
    elif problem["operation"] == " ÷ ":
        problem["num2"] = random.randint(1,12)
        problem["num1"] = problem["num2"]*random.randint(1,12)
        problem["result"] = problem["num1"] / problem["num2"]
        problem["result"] = int(problem["result"])
        randnum = [random.randint(1,12),random.randint(1,12),random.randint(1,12)]

    return randnum

# this function creates 4 button while assigning one of the buttons with the right answer
def process_events(count,score,problem):
    choice = random.randint(1,3)
    randnum = set_problem(problem)
    while True:
        SCREEN.blit(BG, (0, 0))
        BUTTON_MOUSE_POS = pygame.mouse.get_pos()
        rect = pygame.transform.scale(pygame.image.load('assets/answer box.png'),(320,70))

        PLAY_TEXT = get_font(45).render(str(problem["num1"])+problem["operation"]+str(problem["num2"])+ " = ?", True, "Black")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(320, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        SCORE_TEXT = get_font(20).render("SCORE: "+str(score), True, "Black")
        SCORE_RECT = SCORE_TEXT.get_rect(center=(100, 30))
        SCREEN.blit(SCORE_TEXT, SCORE_RECT)
        
        if choice == 1:
            CHOICE1_BACK = Button(image=rect, pos=(320,200), 
                            text_input=str(problem["result"]), font=get_font(40), base_color="Black", hovering_color="Green")
        else:
            CHOICE1_BACK = Button(image=rect, pos=(320,200), 
                            text_input=str(randnum[0]), font=get_font(40), base_color="Black", hovering_color="Green")

        if choice == 2:
            CHOICE2_BACK = Button(image=rect, pos=(320,280), 
                            text_input=str(problem["result"]), font=get_font(40), base_color="Black", hovering_color="Green")
        else: 
            CHOICE2_BACK = Button(image=rect, pos=(320,280), 
                            text_input=str(randnum[1]), font=get_font(40), base_color="Black", hovering_color="Green")
        if choice == 3:
            CHOICE3_BACK = Button(image=rect, pos=(320,360), 
                            text_input=str(problem["result"]), font=get_font(40), base_color="Black", hovering_color="Green")
        else: 
            CHOICE3_BACK = Button(image=rect, pos=(320,360), 
                            text_input=str(randnum[2]), font=get_font(40), base_color="Black", hovering_color="Green")

        for button in [CHOICE1_BACK,CHOICE2_BACK,CHOICE3_BACK]:
                button.changeColor(BUTTON_MOUSE_POS)
                button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (CHOICE1_BACK.checkForInput(BUTTON_MOUSE_POS)) or (CHOICE2_BACK.checkForInput(BUTTON_MOUSE_POS) or (CHOICE3_BACK.checkForInput(BUTTON_MOUSE_POS))):
                    count += 1
                    # We'll add score by 10 if the user
                    # answer correctly the problem
                    if ((CHOICE1_BACK.checkForInput(BUTTON_MOUSE_POS) and choice==1) or
                        (CHOICE2_BACK.checkForInput(BUTTON_MOUSE_POS) and choice==2) or
                        (CHOICE3_BACK.checkForInput(BUTTON_MOUSE_POS) and choice==3)):
                        score += 10
                    # if the count gets to 20 that means that the game is over
                    # and we are going to store total score of the user
                    if count == 10:
                        pygame.time.wait(2000)
                        file = open('ScoreMath.txt', 'a')
                        file.write(str(score))
                        file.write('\n')
                        file.close()
                        play()
                    process_events(count,score,problem)   

        pygame.display.update()

# This function display 4 modes of the game which are:
# 1: Addition, 2: Subtraction
# 3: Multiplication, 4: Division
def play():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        rect = pygame.image.load('assets/choice_rect.png')
        rect = pygame.transform.scale(rect, (460,86))
        problem = {"num1":0,"num2":0,"result":0,"operation":None}

        ADD_BUTTON = Button(image=rect, pos=(330, 80), 
                            text_input="ADDITION", font=get_font(26), base_color="White", hovering_color="Green")
        SUB_BUTTON = Button(image=rect, pos=(330, 190), 
                            text_input="SUBTRACTION", font=get_font(26), base_color="White", hovering_color="Green")
        MUL_BUTTON = Button(image=rect, pos=(330, 292), 
                            text_input="MULTIPLICATION", font=get_font(26), base_color="White", hovering_color="Green")
        DIV_BUTTON = Button(image=rect, pos=(330, 395), 
                            text_input="DIVISION", font=get_font(26), base_color="White", hovering_color="Green")
        EXIT_BUTTON = Button(image=close_button, pos=(40,40), 
                            text_input=None, font=get_font(30), base_color="Black", hovering_color="White")

        for button in [ADD_BUTTON,SUB_BUTTON,MUL_BUTTON,DIV_BUTTON,EXIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ADD_BUTTON.checkForInput(MENU_MOUSE_POS):
                    process_events(0,0,problem= {"num1":0,"num2":0,"result":0,"operation":" + "})
                if SUB_BUTTON.checkForInput(MENU_MOUSE_POS):
                    process_events(0,0,problem= {"num1":0,"num2":0,"result":0,"operation":" - "})
                if MUL_BUTTON.checkForInput(MENU_MOUSE_POS):
                    process_events(0,0,problem= {"num1":0,"num2":0,"result":0,"operation":" x "})
                if DIV_BUTTON.checkForInput(MENU_MOUSE_POS):
                    process_events(0,0,problem= {"num1":0,"num2":0,"result":0,"operation":" ÷ "})
                if EXIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    math_home()

        pygame.display.update()

# this function read the score from "ScoreMath.txt" and display five highest score in ascending order 
def score():
    scores=[0]*5
    while True:
        item_order = ("1ST","2ND","3RD","4TH","5TH")
        SCORE_MOUSE_POS = pygame.mouse.get_pos()

        screen_cover = pygame.transform.scale(pygame.image.load("assets/box.png"), (700, 650))
        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(screen_cover, (-25, -90))

        PAGE_HEADER = get_font(37).render("HIGH", True, "Black")
        SCREEN.blit(PAGE_HEADER,(200,36))
        PAGE_HEADER = get_font(37).render("SCORE", True, "Black")
        SCREEN.blit(PAGE_HEADER,(300,77))

        SCREEN.blit(pygame.image.load("assets/score icon.png"), (210, 60))

        file = open('ScoreMath.txt','r')              # 1. Open file
        for index in range(5):                  # 2. read data from file
            scores[index]=file.readline()[:-1]  # read variables after removing newline
        scores.sort(reverse=True)

        for index in range(5):                  
            width = SCREEN.get_width()
            height = SCREEN.get_height()
            
            posX = 650 - (width /2)
            # t_h: total height of text block
            t_h = len(scores[index]) * height
            posY = 170 + (index*50)

            if len(scores[index]) != 0:
                SCORE_LIST = get_font(26).render('{:<5}{:>10}'.format(item_order[index],scores[index]), True, "Black")
                SCORE_RECT = SCORE_LIST.get_rect(center=(posX,posY))
                SCREEN.blit(SCORE_LIST, SCORE_RECT)
        file.close() 

        button = pygame.image.load('assets/black rect.png')
        button = pygame.transform.scale(button, (290, 190))

        BACK_HOME = Button(image=button, pos=(540, 430), 
                            text_input="BACK", font=get_font(20), base_color="White", hovering_color="Green")

        BACK_HOME.changeColor(SCORE_MOUSE_POS)
        BACK_HOME.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_HOME.checkForInput(SCORE_MOUSE_POS):
                    math_home()

        pygame.display.update()

# In the main menu page, if user want to look up for the how to play the math game.
# The program goes in the howto() function.
# This function used for give the information that user need to know before play math game.
# How-to-play in puzzle game has 4 pages.
# howto() function is the first page.
def howto():
    while True:
        HOWTO_MOUSE_POS = pygame.mouse.get_pos()

        screen_cover = pygame.transform.scale(pygame.image.load("assets/box.png"), (800, 680))
        game_mode = pygame.transform.scale(pygame.image.load("assets/mode.png"), (600, 470))

        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(screen_cover, (-80, -100))
        SCREEN.blit(game_mode, (30, 40))

        HOWTO_TEXT = get_font(25).render("HOW TO PLAY" , True, "Black")
        HOWTO_RECT = HOWTO_TEXT.get_rect(center=(330, 50))
        SCREEN.blit(HOWTO_TEXT, HOWTO_RECT)

        HOWTO_TEXT = get_font2(35).render("1. Select mode of the game" , True, "Black")
        HOWTO_RECT = HOWTO_TEXT.get_rect(center=(320, 100))
        SCREEN.blit(HOWTO_TEXT, HOWTO_RECT)

        HOWTO_NEXT = Button(image=None, pos=(555, 420), 
                            text_input=" → ", font=get_font(35), base_color="Black", hovering_color="Green")

        HOWTO_NEXT.changeColor(HOWTO_MOUSE_POS)
        HOWTO_NEXT.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if HOWTO_NEXT.checkForInput(HOWTO_MOUSE_POS):
                    howto_2()

        pygame.display.update()

# This function used for give the information that user need to know before play math game.
# HOWTO in math game has 3 pages, user can choose to go back to previous page or to next page.
# howto_2() function is the second page.
def howto_2():
     while True:
        HOWTO_MOUSE_POS = pygame.mouse.get_pos()

        screen_cover = pygame.transform.scale(pygame.image.load("assets/box.png"), (800, 680))
        image = pygame.transform.scale(pygame.image.load("assets/Example1.png"), (620, 550))

        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(screen_cover, (-80, -100))
        SCREEN.blit(image,(42,42))

        OPTIONS_TEXT = get_font2(40).render("2. Select the Correct numbers", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(320, 68))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_TEXT = get_font2(40).render("which satisfy the equations", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(320, 110))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(555, 420), 
                            text_input=" → ", font=get_font(35), base_color="Black", hovering_color="Green")
        OPTIONS_RETURN = Button(image=None, pos=(84, 420), 
                            text_input=" ← ", font=get_font(35), base_color="Black", hovering_color="Green")

        for button in [OPTIONS_BACK,OPTIONS_RETURN]:
            button.changeColor(HOWTO_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(HOWTO_MOUSE_POS):
                    howto_3()
                if OPTIONS_RETURN.checkForInput(HOWTO_MOUSE_POS):
                    howto()

        pygame.display.update()

# This function used for give the information that user need to know before play math game.
# HOWTO in puzzle game has 3 pages, user can choose to go back to previous howto or return to homepage.
# howto_3() function is the third page. 
def howto_3():
     while True:
        HOWTO_MOUSE_POS = pygame.mouse.get_pos()

        screen_cover = pygame.transform.scale(pygame.image.load("assets/box.png"), (800, 680))
        image1 = pygame.transform.scale(pygame.image.load("assets/Example1.png"), (400, 400))
        image2 = pygame.transform.scale(pygame.image.load("assets/Example2.png"), (400, 400))

        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(screen_cover, (-80, -100))
        SCREEN.blit(image1,(150,-10))
        SCREEN.blit(image2,(150,250))

        OPTIONS_TEXT = get_font2(28).render("3. If you answer right the box will turns GREEN", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(320, 55))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_TEXT = get_font2(28).render("and if you answer wrong, the box will turns RED", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(320, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_NEXT = Button(image=None, pos=(555, 420), 
                            text_input=" → ", font=get_font(37), base_color="Black", hovering_color="Green")
        OPTIONS_RETURN = Button(image=None, pos=(84, 420), 
                            text_input=" ← ", font=get_font(37), base_color="Black", hovering_color="Green")

        for button in [OPTIONS_NEXT,OPTIONS_RETURN]:
            button.changeColor(HOWTO_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_NEXT.checkForInput(HOWTO_MOUSE_POS):
                    math_home()
                if OPTIONS_RETURN.checkForInput(HOWTO_MOUSE_POS):
                    howto_2()

        pygame.display.update()

# Go to puzzle main menu
# Main menu has 3 bottons consist of PLAY, SCORE, HOWTO
def math_home():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        menu_rect = pygame.image.load('assets/label.png')
        menu_rect = pygame.transform.scale(menu_rect, (350, 80))

        HOME_TEXT = get_font(50).render("Quick Math", True, "Black")
        HOME_RECT = HOME_TEXT.get_rect(center=(320, 95))

        PLAY_BUTTON = Button(image=menu_rect, pos=(330, 180), 
                            text_input="PLAY", font=get_font(30), base_color="Black", hovering_color="Blue")
        SCORE_BUTTON = Button(image=menu_rect, pos=(330, 282), 
                            text_input="SCORE", font=get_font(30), base_color="Black", hovering_color="Blue")
        HOWTO_BUTTON = Button(image=menu_rect, pos=(330, 385), 
                            text_input="HOWTO", font=get_font(30), base_color="Black", hovering_color="Blue")
        EXIT_BUTTON = Button(image=close_button, pos=(40, 40), 
                            text_input=None, font=get_font(30), base_color="Black", hovering_color="White")

        SCREEN.blit(HOME_TEXT, HOME_RECT)

        for button in [PLAY_BUTTON, SCORE_BUTTON, HOWTO_BUTTON,EXIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if SCORE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    score()
                if HOWTO_BUTTON.checkForInput(MENU_MOUSE_POS):
                    howto()
                if EXIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    from main import homepage
                    homepage()
        pygame.display.update()
