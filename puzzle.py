import pygame, sys, random
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((640, 480))   
pygame.display.set_caption("Puzzle Game")

BG = pygame.image.load("Background/puzzle.png")
BG2 = pygame.image.load("Background/puzzle_2.png")

WHITE = (255, 255, 255)

# load font file
def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)


# This function used for give the information that user need to know before play puzzle game.
# How-to-play in puzzle game has 4 pages.
# step4() function is the forth page. 
def step4():

    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 480
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    load_step = pygame.image.load("assets/step4.png")
    step = pygame.transform.scale(load_step,(600,360))

    while True:

        SCREEN.blit(BG2, (0, 0))

        STEP_MOUSE_POS = pygame.mouse.get_pos()

        STEP_TEXT = get_font(30).render("How to Play", True, "Black")
        STEP_RECT = STEP_TEXT.get_rect(center=(320, 20))

        # This button is the shortcut button that place on the top of this page.
        # User can click on the number that represent to the page number of how-to-play.
        SHORTCUT_TEXT = get_font(20).render("Page:", True, "Black")
        SHORTCUT_RECT = SHORTCUT_TEXT.get_rect(center=(65, 55))
        STEP1_SHORTCUT = Button(image=pygame.image.load("assets/stepSC.png"), pos=(130, 55),text_input="1", font=get_font(15), base_color="BLACK", hovering_color="Green")
        STEP2_SHORTCUT = Button(image=pygame.image.load("assets/stepSC.png"), pos=(277, 55),text_input="2", font=get_font(15), base_color="BLACK", hovering_color="Green")
        STEP3_SHORTCUT = Button(image=pygame.image.load("assets/stepSC.png"), pos=(424, 55),text_input="3", font=get_font(15), base_color="BLACK", hovering_color="Green")
        STEP4_SHORTCUT = Button(image=pygame.image.load("assets/stepSC.png"), pos=(571, 55),text_input="4", font=get_font(15), base_color="BLACK", hovering_color="Green")

        SCREEN.blit(STEP_TEXT, STEP_RECT)
        SCREEN.blit(SHORTCUT_TEXT, SHORTCUT_RECT)
        screen.blit(step,(20,80))

        rect=pygame.image.load("assets/Rectangle 9965.png")
        STEP_BACK = Button(image=pygame.image.load("assets/button.png"), pos=(48, 280),text_input="<", font=get_font(18), base_color="BLACK", hovering_color="Green")
        HOME_BACK = Button(image=rect, pos=(500, 450),text_input="Back to Menu", font=get_font(18), base_color="BLACK", hovering_color="Green")

        for button in [STEP1_SHORTCUT, STEP2_SHORTCUT, STEP3_SHORTCUT, STEP4_SHORTCUT,STEP_BACK,HOME_BACK]:
            button.changeColor(STEP_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if STEP1_SHORTCUT.checkForInput(STEP_MOUSE_POS):
                    howto()
                if STEP2_SHORTCUT.checkForInput(STEP_MOUSE_POS):
                    step2()
                if STEP3_SHORTCUT.checkForInput(STEP_MOUSE_POS):
                    step3()
                if STEP4_SHORTCUT.checkForInput(STEP_MOUSE_POS):
                    step4()
                if HOME_BACK.checkForInput(STEP_MOUSE_POS):
                    puzzle_home()
                if STEP_BACK.checkForInput(STEP_MOUSE_POS):
                    step3()
                

        pygame.display.update()




# This function used for give the information that user need to know before play puzzle game.
# How-to-play in puzzle game has 4 pages.
# step3() function is the third page.
def step3():

    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 480
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    load_step = pygame.image.load("assets/step3.png")
    step = pygame.transform.scale(load_step,(600,360))

    while True:

        SCREEN.blit(BG2, (0, 0))

        STEP_MOUSE_POS = pygame.mouse.get_pos()

        STEP_TEXT = get_font(30).render("How to Play", True, "Black")
        STEP_RECT = STEP_TEXT.get_rect(center=(320, 20))

        # This button is the shortcut button that place on the top of this page.
        # User can click on the number that represent to the page number of how-to-play.
        SHORTCUT_TEXT = get_font(20).render("Page:", True, "Black")
        SHORTCUT_RECT = SHORTCUT_TEXT.get_rect(center=(65, 55))
        STEP1_SHORTCUT = Button(image=pygame.image.load("assets/stepSC.png"), pos=(130, 55),text_input="1", font=get_font(15), base_color="BLACK", hovering_color="Green")
        STEP2_SHORTCUT = Button(image=pygame.image.load("assets/stepSC.png"), pos=(277, 55),text_input="2", font=get_font(15), base_color="BLACK", hovering_color="Green")
        STEP3_SHORTCUT = Button(image=pygame.image.load("assets/stepSC.png"), pos=(424, 55),text_input="3", font=get_font(15), base_color="BLACK", hovering_color="Green")
        STEP4_SHORTCUT = Button(image=pygame.image.load("assets/stepSC.png"), pos=(571, 55),text_input="4", font=get_font(15), base_color="BLACK", hovering_color="Green")

        SCREEN.blit(STEP_TEXT, STEP_RECT)
        SCREEN.blit(SHORTCUT_TEXT, SHORTCUT_RECT)
        screen.blit(step,(20,80))

        # This button used for go to the previous page
        STEP_BACK = Button(image=pygame.image.load("assets/button.png"), pos=(48, 280),text_input="<", font=get_font(18), base_color="BLACK", hovering_color="Green")
        
        # This button used for go to the next page
        STEP_GO = Button(image=pygame.image.load("assets/button.png"), pos=(590, 280),text_input=">", font=get_font(18), base_color="BLACK", hovering_color="Green")

        rect=pygame.image.load("assets/Rectangle 9965.png")
        HOME_BACK = Button(image=rect, pos=(500, 450),text_input="Back to Menu", font=get_font(18), base_color="BLACK", hovering_color="Green")

        for button in [STEP1_SHORTCUT, STEP2_SHORTCUT, STEP3_SHORTCUT, STEP4_SHORTCUT,STEP_BACK, STEP_GO,HOME_BACK]:
            button.changeColor(STEP_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if STEP1_SHORTCUT.checkForInput(STEP_MOUSE_POS):
                    howto()
                if STEP2_SHORTCUT.checkForInput(STEP_MOUSE_POS):
                    step2()
                if STEP3_SHORTCUT.checkForInput(STEP_MOUSE_POS):
                    step3()
                if STEP4_SHORTCUT.checkForInput(STEP_MOUSE_POS):
                    step4()
                if HOME_BACK.checkForInput(STEP_MOUSE_POS):
                    puzzle_home()
                if STEP_BACK.checkForInput(STEP_MOUSE_POS):
                    step2()
                if STEP_GO.checkForInput(STEP_MOUSE_POS):
                    step4()

        pygame.display.update()



# This function used for give the information that user need to know before play puzzle game.
# How-to-play in puzzle game has 4 pages.
# step2() function is the second page.
def step2():

    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 480
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    load_step = pygame.image.load("assets/step2.png")
    step = pygame.transform.scale(load_step,(600,360))

    while True:

        SCREEN.blit(BG2, (0, 0))

        STEP_MOUSE_POS = pygame.mouse.get_pos()

        STEP_TEXT = get_font(30).render("How to Play", True, "Black")
        STEP_RECT = STEP_TEXT.get_rect(center=(320, 20))

        # This button is the shortcut button that place on the top of this page.
        # User can click on the number that represent to the page number of how-to-play.
        SHORTCUT_TEXT = get_font(20).render("Page:", True, "Black")
        SHORTCUT_RECT = SHORTCUT_TEXT.get_rect(center=(65, 55))
        STEP1_SHORTCUT = Button(image=pygame.image.load("assets/stepSC.png"), pos=(130, 55),text_input="1", font=get_font(15), base_color="BLACK", hovering_color="Green")
        STEP2_SHORTCUT = Button(image=pygame.image.load("assets/stepSC.png"), pos=(277, 55),text_input="2", font=get_font(15), base_color="BLACK", hovering_color="Green")
        STEP3_SHORTCUT = Button(image=pygame.image.load("assets/stepSC.png"), pos=(424, 55),text_input="3", font=get_font(15), base_color="BLACK", hovering_color="Green")
        STEP4_SHORTCUT = Button(image=pygame.image.load("assets/stepSC.png"), pos=(571, 55),text_input="4", font=get_font(15), base_color="BLACK", hovering_color="Green")

        SCREEN.blit(STEP_TEXT, STEP_RECT)
        SCREEN.blit(SHORTCUT_TEXT, SHORTCUT_RECT)
        screen.blit(step,(20,80))

        # This button used for go to the previous page
        STEP_BACK = Button(image=pygame.image.load("assets/button.png"), pos=(48, 280),text_input="<", font=get_font(18), base_color="BLACK", hovering_color="Green")
        
        # This button used for go to the next page
        STEP_GO = Button(image=pygame.image.load("assets/button.png"), pos=(590, 280),text_input=">", font=get_font(18), base_color="BLACK", hovering_color="Green")

        rect=pygame.image.load("assets/Rectangle 9965.png")
        HOME_BACK = Button(image=rect, pos=(500, 450),text_input="Back to Menu", font=get_font(18), base_color="BLACK", hovering_color="Green")

        for button in [STEP1_SHORTCUT, STEP2_SHORTCUT, STEP3_SHORTCUT, STEP4_SHORTCUT,STEP_BACK, STEP_GO,HOME_BACK]:
            button.changeColor(STEP_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if STEP1_SHORTCUT.checkForInput(STEP_MOUSE_POS):
                    howto()
                if STEP2_SHORTCUT.checkForInput(STEP_MOUSE_POS):
                    step2()
                if STEP3_SHORTCUT.checkForInput(STEP_MOUSE_POS):
                    step3()
                if STEP4_SHORTCUT.checkForInput(STEP_MOUSE_POS):
                    step4()
                if HOME_BACK.checkForInput(STEP_MOUSE_POS):
                    puzzle_home()
                if STEP_BACK.checkForInput(STEP_MOUSE_POS):
                    howto()
                if STEP_GO.checkForInput(STEP_MOUSE_POS):
                    step3()

        pygame.display.update()



# In the main menu page, if user want to look up for the how to play the puzzle game.
# The program goes in the howto() function.
# This function used for give the information that user need to know before play puzzle game.
# How-to-play in puzzle game has 4 pages.
# howto() function is the first page.
def howto():

    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 480
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    # Load and optimize a first page of how-to-play picture
    load_step = pygame.image.load("assets/step1.png")
    step = pygame.transform.scale(load_step,(600,360))

    while True:

        SCREEN.blit(BG2, (0, 0))

        HOWTO_MOUSE_POS = pygame.mouse.get_pos()

        HOWTO_TEXT = get_font(30).render("How to Play", True, "Black")
        HOWTO_RECT = HOWTO_TEXT.get_rect(center=(320, 20))

        # This button is the shortcut button that place on the top of this page.
        # User can click on the number that represent to the page number of how-to-play.
        SHORTCUT_TEXT = get_font(20).render("Page:", True, "Black")
        SHORTCUT_RECT = SHORTCUT_TEXT.get_rect(center=(65, 55))
        STEP1_SHORTCUT = Button(image=pygame.image.load("assets/stepSC.png"), pos=(130, 55),text_input="1", font=get_font(15), base_color="BLACK", hovering_color="Green")
        STEP2_SHORTCUT = Button(image=pygame.image.load("assets/stepSC.png"), pos=(277, 55),text_input="2", font=get_font(15), base_color="BLACK", hovering_color="Green")
        STEP3_SHORTCUT = Button(image=pygame.image.load("assets/stepSC.png"), pos=(424, 55),text_input="3", font=get_font(15), base_color="BLACK", hovering_color="Green")
        STEP4_SHORTCUT = Button(image=pygame.image.load("assets/stepSC.png"), pos=(571, 55),text_input="4", font=get_font(15), base_color="BLACK", hovering_color="Green")

        # This button used for go to the next page
        rect=pygame.image.load("assets/Rectangle 9965.png")
        HOW_GO = Button(image=pygame.image.load("assets/button.png"), pos=(590, 280),text_input=">", font=get_font(18), base_color="BLACK", hovering_color="Green")
        HOME_BACK = Button(image=rect, pos=(500, 450),text_input="Back to Menu", font=get_font(18), base_color="BLACK", hovering_color="Green")


        SCREEN.blit(HOWTO_TEXT, HOWTO_RECT)
        SCREEN.blit(SHORTCUT_TEXT, SHORTCUT_RECT)
        screen.blit(step,(20,80))

        for button in [STEP1_SHORTCUT, STEP2_SHORTCUT, STEP3_SHORTCUT, STEP4_SHORTCUT, HOW_GO, HOME_BACK]:
            button.changeColor(HOWTO_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if STEP1_SHORTCUT.checkForInput(HOWTO_MOUSE_POS):
                    howto()
                if STEP2_SHORTCUT.checkForInput(HOWTO_MOUSE_POS):
                    step2()
                if STEP3_SHORTCUT.checkForInput(HOWTO_MOUSE_POS):
                    step3()
                if STEP4_SHORTCUT.checkForInput(HOWTO_MOUSE_POS):
                    step4()
                if HOME_BACK.checkForInput(HOWTO_MOUSE_POS):
                    puzzle_home()
                if HOW_GO.checkForInput(HOWTO_MOUSE_POS):
                    step2()

        pygame.display.update()



# When user want to look up for a hint in easy level, it will go to easy_hint().
# This function used for displays the full image of easy-level picture.
def easy_hint():

    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 480
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    bg = pygame.image.load("image/dish.jpg").convert()
    bg_rect = bg.get_rect()
    bg_rect.topleft = (0, 0)    # set position of image

    while True:

        screen.blit(bg, bg_rect)    # show full image

        HINT_MOUSE_POS = pygame.mouse.get_pos()

        HINT_BACK = Button(image=None, pos=(200,450),
                    text_input="Back to Game", font=get_font(25), base_color="BLACK", hovering_color="Green")
        HINT_BACK.changeColor(HINT_MOUSE_POS)
        HINT_BACK.update(SCREEN)

        HINT_QUIT = Button(image=None, pos=(570, 450), 
                    text_input="QUIT", font=get_font(25), base_color="BLACK", hovering_color="RED")
        HINT_QUIT.changeColor(HINT_MOUSE_POS)
        HINT_QUIT.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if HINT_BACK.checkForInput(HINT_MOUSE_POS):
                    easy_play()
                if HINT_QUIT.checkForInput(HINT_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()



# When user want to look up for a hint in medium level, it will go to med_hint().
# This function used for displays the full image of medium-level picture.
def med_hint():

    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 480
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    bg = pygame.image.load("image/play.png").convert()
    bg_rect = bg.get_rect()
    bg_rect.topleft = (0, 0)    # set position of image

    while True:
        screen.blit(bg, bg_rect)    # show full image

        HINT_MOUSE_POS = pygame.mouse.get_pos()

        HINT_BACK = Button(image=None, pos=(200,450),
                    text_input="Back to Game", font=get_font(25), base_color="BLACK", hovering_color="Green")
        HINT_BACK.changeColor(HINT_MOUSE_POS)
        HINT_BACK.update(SCREEN)

        HINT_QUIT = Button(image=None, pos=(570, 450), 
                    text_input="QUIT", font=get_font(25), base_color="BLACK", hovering_color="RED")
        HINT_QUIT.changeColor(HINT_MOUSE_POS)
        HINT_QUIT.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if HINT_BACK.checkForInput(HINT_MOUSE_POS):
                    med_play()
                if HINT_QUIT.checkForInput(HINT_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()



# When user want to look up for a hint in hard level, it will go to hard_hint().
# This function used for displays the full image of hard-level picture.
def hard_hint():

    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 480
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    bg = pygame.image.load("image/garden.png").convert()
    bg_rect = bg.get_rect()
    bg_rect.topleft = (0, 0)    # set position of image

    while True:
        screen.blit(bg, bg_rect)    # show full image

        HINT_MOUSE_POS = pygame.mouse.get_pos()

        HINT_BACK = Button(image=None, pos=(200,450),
                    text_input="Back to Game", font=get_font(25), base_color="BLACK", hovering_color="Green")
        HINT_BACK.changeColor(HINT_MOUSE_POS)
        HINT_BACK.update(SCREEN)

        HINT_QUIT = Button(image=None, pos=(570, 450), 
                    text_input="QUIT", font=get_font(25), base_color="BLACK", hovering_color="RED")
        HINT_QUIT.changeColor(HINT_MOUSE_POS)
        HINT_QUIT.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if HINT_BACK.checkForInput(HINT_MOUSE_POS):
                    hard_play()
                if HINT_QUIT.checkForInput(HINT_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()



# When user select the easy level, it will go to easy_play().
# This function used for play puzzle game in a easy level.
def easy_play():
    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 480
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Puzzle Game')

    FPS = 10
    clock = pygame.time.Clock()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    CRIMSON = (220, 20, 60)
    ORANGE = (255, 127, 0)
    green = (92, 145, 101)
    bright_green = (121, 175, 127)
    salmon = (250, 128, 114)
    salmon_light = (255, 160, 122)

    bg = pygame.image.load("image/dish.jpg").convert()
    bg_rect = bg.get_rect()
    bg_rect.topleft = (0, 0)    # set position of image

    selected_img = None
    is_game_over = False

    rows = 3
    cols = 3
    num_cells = rows * cols

    cell_width = WINDOW_WIDTH // rows        #rows
    cell_height = WINDOW_HEIGHT // cols      #cols

    cells = []
    rand_indexes = list(range(0, num_cells))    # random index

    for i in range(num_cells):
        x = (i % rows) * cell_width
        y = (i // cols) * cell_height
        rect = pygame.Rect(x, y, cell_width, cell_height)
        rand_pos = random.choice(rand_indexes)
        rand_indexes.remove(rand_pos)
        cells.append({'rect': rect, 'border': WHITE, 'order': i, 'pos':rand_pos})

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not is_game_over:
                mouse_pos = pygame.mouse.get_pos()

                for cell in cells:
                    rect = cell['rect']
                    order = cell['order']

                    if rect.collidepoint(mouse_pos):    #image order
                        if not selected_img:
                            selected_img = cell
                            cell['border'] = RED        # Selected piece has a red border
                        else:
                            current_img = cell
                            if current_img['order'] != selected_img['order']:
                                #swap images
                                temp = selected_img['pos']
                                cells[selected_img['order']]['pos'] = cells[current_img['order']]['pos']
                                cells[current_img['order']]['pos'] = temp

                                cells[selected_img['order']]['border'] = WHITE
                                selected_img = None

                                # check if puzzle is solved
                                is_game_over = True
                                for cell in cells:
                                    if cell['order'] != cell['pos']:   # compare with order and position
                                        is_game_over = False

            screen.fill(WHITE)

            if not is_game_over:
                # Get in the loop when user does not complete solve the puzzle.
                for i, val in enumerate(cells):
                    pos = cells[i]['pos']
                    img_area = pygame.Rect(cells[pos]['rect'].x, cells[pos]['rect'].y, cell_width, cell_height)
                    screen.blit(bg, cells[i]['rect'], img_area)
                    pygame.draw.rect(screen, cells[i]['border'], cells[i]['rect'], 1)

                    PLAY_MOUSE_POS = pygame.mouse.get_pos()

                    LOOK_UP = Button(image=None, pos=(580, 450), text_input="hint", font=get_font(16), base_color="BLACK", hovering_color="Green")

                    LOOK_UP.changeColor(PLAY_MOUSE_POS)
                    LOOK_UP.update(SCREEN)

                    EASY_BACK = Button(image=None, pos=(83, 450), text_input="Main Menu", font=get_font(16), base_color="BLACK", hovering_color="Green")

                    EASY_BACK.changeColor(PLAY_MOUSE_POS)
                    EASY_BACK.update(SCREEN)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if LOOK_UP.checkForInput(PLAY_MOUSE_POS):
                            easy_hint()
                        if EASY_BACK.checkForInput(PLAY_MOUSE_POS):
                            puzzle_main()

                    
            else:
                # Show the full image when user complete solve the puzzle
                # and show the 2 bottons that consist of
                # Main menu and
                # Quit
                screen.blit(bg, bg_rect)    # show full image

                PLAY_MOUSE_POS = pygame.mouse.get_pos()

                PLAY_BACK = Button(image=None, pos=(320, 150), 
                            text_input="Main Menu", font=get_font(55), base_color="BLACK", hovering_color="Green")

                PLAY_BACK.changeColor(PLAY_MOUSE_POS)
                PLAY_BACK.update(SCREEN)

                QUIT = Button(image=None, pos=(320, 310), 
                            text_input="QUIT", font=get_font(50), base_color="BLACK", hovering_color="Green")

                QUIT.changeColor(PLAY_MOUSE_POS)
                QUIT.update(SCREEN)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        puzzle_main()
                    if QUIT.checkForInput(PLAY_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

        pygame.display.update()



# When user select the medium level, it will go to med_play().
# This function used for play puzzle game in a medium level.
def med_play():
    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 480
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Puzzle Game')

    FPS = 10
    clock = pygame.time.Clock()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    CRIMSON = (220, 20, 60)
    ORANGE = (255, 127, 0)
    green = (92, 145, 101)
    bright_green = (121, 175, 127)
    salmon = (250, 128, 114)
    salmon_light = (255, 160, 122)

    # Load and optimize a medium-level picture
    bg = pygame.image.load("image/play.png").convert()
    bg_rect = bg.get_rect()
    bg_rect.topleft = (0, 0)    # set position of image

    selected_img = None
    is_game_over = False

    rows = 4
    cols = 4
    num_cells = rows * cols

    cell_width = WINDOW_WIDTH // rows        #rows
    cell_height = WINDOW_HEIGHT // cols      #cols

    cells = []
    rand_indexes = list(range(0, num_cells))    # random index

    for i in range(num_cells):
        x = (i % rows) * cell_width
        y = (i // cols) * cell_height
        rect = pygame.Rect(x, y, cell_width, cell_height)
        rand_pos = random.choice(rand_indexes)
        rand_indexes.remove(rand_pos)
        cells.append({'rect': rect, 'border': WHITE, 'order': i, 'pos':rand_pos})

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not is_game_over:
                mouse_pos = pygame.mouse.get_pos()

                for cell in cells:
                    rect = cell['rect']
                    order = cell['order']

                    if rect.collidepoint(mouse_pos):    #image order
                        if not selected_img:
                            selected_img = cell
                            cell['border'] = RED        # Selected piece has a red border
                        else:
                            current_img = cell
                            if current_img['order'] != selected_img['order']:
                                #swap images
                                temp = selected_img['pos']
                                cells[selected_img['order']]['pos'] = cells[current_img['order']]['pos']
                                cells[current_img['order']]['pos'] = temp

                                cells[selected_img['order']]['border'] = WHITE
                                selected_img = None

                                # Check if puzzle is solved
                                is_game_over = True
                                for cell in cells:
                                    if cell['order'] != cell['pos']:   # Compare with order and position
                                        is_game_over = False

            screen.fill(WHITE)

            if not is_game_over:
                # Get in the loop when user does not complete solve the puzzle.
                for i, val in enumerate(cells):
                    pos = cells[i]['pos']
                    img_area = pygame.Rect(cells[pos]['rect'].x, cells[pos]['rect'].y, cell_width, cell_height)
                    screen.blit(bg, cells[i]['rect'], img_area)
                    pygame.draw.rect(screen, cells[i]['border'], cells[i]['rect'], 1)

                    PLAY_MOUSE_POS = pygame.mouse.get_pos()

                    LOOK_UP = Button(image=None, pos=(580, 450), text_input="hint", font=get_font(16), base_color="BLACK", hovering_color="Green")

                    LOOK_UP.changeColor(PLAY_MOUSE_POS)
                    LOOK_UP.update(SCREEN)

                    MED_BACK = Button(image=None, pos=(83, 450), text_input="Main Menu", font=get_font(16), base_color="BLACK", hovering_color="Green")

                    MED_BACK.changeColor(PLAY_MOUSE_POS)
                    MED_BACK.update(SCREEN)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if LOOK_UP.checkForInput(PLAY_MOUSE_POS):
                            med_hint()
                        if MED_BACK.checkForInput(PLAY_MOUSE_POS):
                            puzzle_main()

                    
            else:
                # Show the full image when user complete solve the puzzle
                # and show the 2 bottons that consist of
                # Main menu and
                # Quit
                screen.blit(bg, bg_rect)    # show full image

                PLAY_MOUSE_POS = pygame.mouse.get_pos()

                PLAY_BACK = Button(image=None, pos=(320, 150), 
                            text_input="Main Menu", font=get_font(55), base_color="BLACK", hovering_color="Green")

                PLAY_BACK.changeColor(PLAY_MOUSE_POS)
                PLAY_BACK.update(SCREEN)

                QUIT = Button(image=None, pos=(320, 310), 
                            text_input="QUIT", font=get_font(50), base_color="BLACK", hovering_color="Green")

                QUIT.changeColor(PLAY_MOUSE_POS)
                QUIT.update(SCREEN)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        puzzle_main()
                    if QUIT.checkForInput(PLAY_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

        pygame.display.update()



# When user select the hard level, it will go to hard_play().
# This function used for play puzzle game in a hard level.
def hard_play():
    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 480
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Puzzle Game')

    FPS = 10
    clock = pygame.time.Clock()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    CRIMSON = (220, 20, 60)
    ORANGE = (255, 127, 0)
    green = (92, 145, 101)
    bright_green = (121, 175, 127)
    salmon = (250, 128, 114)
    salmon_light = (255, 160, 122)

    # Load and optimize a hard-level picture
    bg = pygame.image.load("image/garden.png").convert()
    bg_rect = bg.get_rect()
    bg_rect.topleft = (0, 0)    # set position of image

    selected_img = None
    is_game_over = False

    rows = 5
    cols = 5
    num_cells = rows * cols

    cell_width = WINDOW_WIDTH // rows           #rows
    cell_height = WINDOW_HEIGHT // cols         #cols

    cells = []
    rand_indexes = list(range(0, num_cells))    # random index

    for i in range(num_cells):
        x = (i % rows) * cell_width
        y = (i // cols) * cell_height
        rect = pygame.Rect(x, y, cell_width, cell_height)
        rand_pos = random.choice(rand_indexes)
        rand_indexes.remove(rand_pos)
        cells.append({'rect': rect, 'border': WHITE, 'order': i, 'pos':rand_pos})

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not is_game_over:
                mouse_pos = pygame.mouse.get_pos()

                for cell in cells:
                    rect = cell['rect']
                    order = cell['order']

                    if rect.collidepoint(mouse_pos):    #image order
                        if not selected_img:
                            selected_img = cell
                            cell['border'] = RED        # Selected piece has a red border
                        else:
                            current_img = cell
                            if current_img['order'] != selected_img['order']:
                                # Swap images
                                temp = selected_img['pos']
                                cells[selected_img['order']]['pos'] = cells[current_img['order']]['pos']
                                cells[current_img['order']]['pos'] = temp

                                cells[selected_img['order']]['border'] = WHITE
                                selected_img = None

                                # Check if puzzle is solved
                                is_game_over = True
                                for cell in cells:
                                    if cell['order'] != cell['pos']:   # compare with order and position
                                        is_game_over = False

            screen.fill(WHITE)

            if not is_game_over:
                # Get in the loop when user does not complete solve the puzzle.
                for i, val in enumerate(cells):
                    pos = cells[i]['pos']
                    img_area = pygame.Rect(cells[pos]['rect'].x, cells[pos]['rect'].y, cell_width, cell_height)
                    screen.blit(bg, cells[i]['rect'], img_area)
                    pygame.draw.rect(screen, cells[i]['border'], cells[i]['rect'], 1)

                    PLAY_MOUSE_POS = pygame.mouse.get_pos()

                    LOOK_UP = Button(image=None, pos=(580, 450), text_input="hint", font=get_font(16), base_color="BLACK", hovering_color="Green")

                    LOOK_UP.changeColor(PLAY_MOUSE_POS)
                    LOOK_UP.update(SCREEN)


                    HARD_BACK = Button(image=None, pos=(83, 450), text_input="Main Menu", font=get_font(16), base_color="BLACK", hovering_color="Green")

                    HARD_BACK.changeColor(PLAY_MOUSE_POS)
                    HARD_BACK.update(SCREEN)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if LOOK_UP.checkForInput(PLAY_MOUSE_POS):
                            hard_hint()
                        if HARD_BACK.checkForInput(PLAY_MOUSE_POS):
                            puzzle_main()

            else:
                # Show the full image when user complete solve the puzzle
                # and show the 2 bottons that consist of
                # Main menu and
                # Quit
                screen.blit(bg, bg_rect)    # show full image

                PLAY_MOUSE_POS = pygame.mouse.get_pos()

                PLAY_BACK = Button(image=None, pos=(320, 150), 
                            text_input="Main Menu", font=get_font(16), base_color="BLACK", hovering_color="Green")

                PLAY_BACK.changeColor(PLAY_MOUSE_POS)
                PLAY_BACK.update(SCREEN)

                QUIT = Button(image=None, pos=(320, 310), 
                            text_input="QUIT", font=get_font(16), base_color="BLACK", hovering_color="Green")

                QUIT.changeColor(PLAY_MOUSE_POS)
                QUIT.update(SCREEN)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        puzzle_main()
                    if QUIT.checkForInput(PLAY_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

        pygame.display.update()



# Go to level selection that consist of
# Level 1: Easy (3x3)
# Level 2: Medium (4x4)
# Level 3: Hard (5x5)
def puzzle_main():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        close_button = pygame.image.load('assets/close.png')
        close_button = pygame.transform.scale(close_button, (30, 30))

        MENU_TEXT = get_font(58).render("Puzzle", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(320, 80))

        EASY_BUTTON = Button(image=pygame.image.load("assets/Easy Rect.png"), pos=(320, 180), 
                            text_input="Easy (3 x 3)", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        MEDIUM_BUTTON = Button(image=pygame.image.load("assets/Medium Rect.png"), pos=(320, 280), 
                            text_input="Medium (4 x 4)", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        HARD_BUTTON = Button(image=pygame.image.load("assets/Hard Rect.png"), pos=(320, 380), 
                            text_input="Hard (5 x 5)", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        HOME_BACK = Button(image=close_button, pos=(40, 40), 
                            text_input=None, font=get_font(30), base_color="Black", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [EASY_BUTTON, MEDIUM_BUTTON, HARD_BUTTON, HOME_BACK]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    easy_play()
                if MEDIUM_BUTTON.checkForInput(MENU_MOUSE_POS):
                    med_play()
                if HARD_BUTTON.checkForInput(MENU_MOUSE_POS):
                    hard_play()
                if HOME_BACK.checkForInput(MENU_MOUSE_POS):
                    puzzle_home()

        pygame.display.update()



# Go to puzzle main menu
# Main menu has 3 bottons consist of Play Game, How to play, Back to Home
def puzzle_home():
    while True:
        SCREEN.blit(BG, (0, 0))

        HOME_MOUSE_POS = pygame.mouse.get_pos()

        HOME_TEXT = get_font(58).render("Puzzle", True, "Black")
        HOME_RECT = HOME_TEXT.get_rect(center=(320, 80))

        menu_rect = pygame.image.load('assets/label.png')
        menu_rect = pygame.transform.scale(menu_rect, (350, 80))

        PLAY_BUTTON = Button(image=menu_rect, pos=(330, 200), 
                            text_input="PLAY", font=get_font(30), base_color="Black", hovering_color="Blue")
        HOWTO_BUTTON = Button(image=menu_rect, pos=(330, 300), 
                            text_input="HOW TO PLAY", font=get_font(26), base_color="Black", hovering_color="Blue")
        HOME_BUTTON = Button(image=menu_rect, pos=(330,400), 
                            text_input="BACK", font=get_font(30), base_color="Black", hovering_color="Blue")

        SCREEN.blit(HOME_TEXT, HOME_RECT)

        for button in [PLAY_BUTTON, HOWTO_BUTTON, HOME_BUTTON]:
            button.changeColor(HOME_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(HOME_MOUSE_POS):
                    puzzle_main()
                if HOWTO_BUTTON.checkForInput(HOME_MOUSE_POS):
                    howto()
                if HOME_BUTTON.checkForInput(HOME_MOUSE_POS):
                    from main import homepage
                    homepage()
        pygame.display.update()