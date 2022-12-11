import pygame
from pygame.locals import *

# Set display size and color #
pygame.init()
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
red = (255, 0, 0)

def photohunt_home():
    # Set screen resolution and display caption #
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Photo hunt game")

    # Set font and font size #
    font = pygame.font.Font('raw_mat/ui/PressStart2P-Regular.ttf', 18)
    font_main = pygame.font.Font('raw_mat/ui/PressStart2P-Regular.ttf', 28)

    # Create text "Scoreboard" #
    text_scoreboard = font_main.render('Scoreboard', True, black, white)
    text_scoreboardRect = text_scoreboard.get_rect()
    text_scoreboardRect.center = (SCREEN_WIDTH // 2, 50)

    # Create text "1" to show that users is in stage 1 #
    text_state1 = font.render('1', True, black, white)
    text_state1Rect = text_state1.get_rect()
    text_state1Rect.center = (SCREEN_WIDTH // 2 + 60, 45)

    # Create text "2" to show that users is in stage 2 #
    text_state2 = font.render('2', True, black, white)
    text_state2Rect = text_state2.get_rect()
    text_state2Rect.center = (SCREEN_WIDTH // 2 + 60, 45)

    # Create text "3" to show that users is in stage 3 #
    text_state3 = font.render('3', True, black, white)
    text_state3Rect = text_state3.get_rect()
    text_state3Rect.center = (SCREEN_WIDTH // 2 + 60, 45)

    # Create text "4" to show that users is in stage 4 #
    text_state4 = font.render('4', True, black, white)
    text_state4Rect = text_state4.get_rect()
    text_state4Rect.center = (SCREEN_WIDTH // 2 + 60, 45)

    # Create text "5" to show that user is in stage 5 #
    text_state5 = font.render('5', True, black, white)
    text_state5Rect = text_state5.get_rect()
    text_state5Rect.center = (SCREEN_WIDTH // 2 + 60, 45)

    # Declare some variable to store picture
    # bg - store background
    # bghome - store homepage background
    # bgscore - store score page background
    # bghowtoplay - store how to play page background #
    bg = pygame.image.load("raw_mat/ui/ui_new/pygame_gameplay.jpg")
    bghome = pygame.image.load("raw_mat/ui/ui_new/home.jpg")
    bgscore = pygame.image.load("raw_mat/ui/ui_new/score.jpg")
    bghowtoplay = pygame.image.load("raw_mat/ui/ui_new/howto.jpg")

    # import exit button image #
    image_back = pygame.image.load("raw_mat/ui/ui_new/Exit.png")
    image_back = pygame.transform.scale(image_back, (30, 30))
    image_back_rect = image_back.get_rect()  # Make it in rectangle shape #
    image_back_rect.center = SCREEN_WIDTH - 30, 30  # Set the position of the image #

    # import play button image #
    image_start = pygame.image.load("raw_mat/ui/ui_new/PLAY.png")
    image_start_rect = image_start.get_rect()
    image_start_rect.center = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 70

    # import scoreboard button image #
    image_scoreboard = pygame.image.load("raw_mat/ui/ui_new/SCORE.png")
    image_scoreboard_rect = image_scoreboard.get_rect()
    image_scoreboard_rect.center = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2

    # import how to play button image #
    image_howto = pygame.image.load("raw_mat/ui/ui_new/HOW.png")
    image_howto_rect = image_howto.get_rect()
    image_howto_rect.center = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 70

    # import back button image #
    image_exit = pygame.image.load("raw_mat/ui/ui_new/BACK.png")
    image_exit_rect = image_exit.get_rect()
    image_exit_rect.center = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 140

    # import right-arrow button image #
    image_next = pygame.image.load("raw_mat/ui/ui_new/right arrow.png")
    image_next_rect = image_next.get_rect()
    image_next_rect.center = SCREEN_WIDTH - 30, SCREEN_HEIGHT - 50

    # import stage 1.1 image #
    image_game1_1 = pygame.image.load("raw_mat/photohunt_stage/pic1-1.png")
    image_game1_1rect = image_game1_1.get_rect()
    image_game1_1rect.center = 480, 240

    # import stage 1.2 image #
    image_game1_2 = pygame.image.load("raw_mat/photohunt_stage/pic1-2.png")
    image_game1_2rect = image_game1_2.get_rect()
    image_game1_2rect.center = 160, 240

    # import stage 2.1 image #
    image_game2_1 = pygame.image.load("raw_mat/photohunt_stage/pic2-1.png")
    image_game2_1rect = image_game2_1.get_rect()
    image_game2_1rect.center = 480, 240

    # import stage 2.2 image #
    image_game2_2 = pygame.image.load("raw_mat/photohunt_stage/pic2-2.png")
    image_game2_2rect = image_game2_2.get_rect()
    image_game2_2rect.center = 160, 240

    # import stage 3.1 image #
    image_game3_1 = pygame.image.load("raw_mat/photohunt_stage/pic3-1.png")
    image_game3_1rect = image_game3_1.get_rect()
    image_game3_1rect.center = 480, 240

    # import stage 3.2 image #
    image_game3_2 = pygame.image.load("raw_mat/photohunt_stage/pic 3-2.png")
    image_game3_2rect = image_game3_2.get_rect()
    image_game3_2rect.center = 160, 240

    # import stage 4.1 image #
    image_game4_1 = pygame.image.load("raw_mat/photohunt_stage/pic4-1.png")
    image_game4_1rect = image_game4_1.get_rect()
    image_game4_1rect.center = 480, 240

    # import stage 4.2 image #
    image_game4_2 = pygame.image.load("raw_mat/photohunt_stage/pic4-2.png")
    image_game4_2rect = image_game4_2.get_rect()
    image_game4_2rect.center = 160, 240

    # import stage 5.1 image #
    image_game5_1 = pygame.image.load("raw_mat/photohunt_stage/pic5-1.png")
    image_game5_1rect = image_game5_1.get_rect()
    image_game5_1rect.center = 480, 240

    # import stage 5.2 image #
    image_game5_2 = pygame.image.load("raw_mat/photohunt_stage/pic5-2.png")
    image_game5_2rect = image_game5_2.get_rect()
    image_game5_2rect.center = 160, 240

    # Score count for each stage #
    def find(num):
        x = 32
        for i in range(num):
            pygame.draw.rect(screen, red, pygame.Rect(x, SCREEN_HEIGHT - 58, 10, 10))
            x += 21

    # Set the first page as main #
    page = "main"
    running = True
    num1 = 0 # Count how many spot that user found #
    num2 = 0
    num3 = 0
    num4 = 0
    num5 = 0

    # Set the difference spot #
    game1_pos = []
    game2_pos = []
    game3_pos = []
    game4_pos = []
    game5_pos = []
    for i in range(5): # Loop for 5 positions #
        game1_pos.append(0)  # Set value = 0 if the spot is not found yet #
        game2_pos.append(0)  # Set value = 1 if the spot is already found #
        game3_pos.append(0)
        game4_pos.append(0)
        game5_pos.append(0)

    # Set the difference spot position in stage 1 #
    posGame1_1 = pygame.Rect((40, 165), (20, 20))
    posGame1_2 = pygame.Rect((120, 105), (30, 30))
    posGame1_3 = pygame.Rect((175, 250), (30, 30))
    posGame1_4 = pygame.Rect((250, 320), (30, 50))
    posGame1_5 = pygame.Rect((60, 370), (35, 20))

    # Set the difference spot position in stage 2 #
    posGame2_1 = pygame.Rect((250, 140), (20, 20))
    posGame2_2 = pygame.Rect((70, 130), (30, 30))
    posGame2_3 = pygame.Rect((100, 200), (10, 10))
    posGame2_4 = pygame.Rect((135, 225), (15, 15))
    posGame2_5 = pygame.Rect((35, 300), (35, 20))

    # Set the difference spot position in stage 3 #
    posGame3_1 = pygame.Rect((80, 120), (60, 40))
    posGame3_2 = pygame.Rect((148, 183), (10, 10))
    posGame3_3 = pygame.Rect((175, 265), (10, 10))
    posGame3_4 = pygame.Rect((90, 340), (20, 20))
    posGame3_5 = pygame.Rect((40, 300), (15, 20))

    # Set the difference spot position in stage 4 #
    posGame4_1 = pygame.Rect((45, 120), (30, 30))
    posGame4_2 = pygame.Rect((230, 130), (20, 40))
    posGame4_3 = pygame.Rect((150, 200), (20, 25))
    posGame4_4 = pygame.Rect((48, 325), (20, 20))
    posGame4_5 = pygame.Rect((240, 320), (25, 45))

    # Set the difference spot position in stage 5 #
    posGame5_1 = pygame.Rect((50, 165), (20, 20))
    posGame5_2 = pygame.Rect((210, 250), (15, 15))
    posGame5_3 = pygame.Rect((250, 220), (25, 20))
    posGame5_4 = pygame.Rect((255, 266), (20, 15))
    posGame5_5 = pygame.Rect((245, 300), (15, 20))

    start_ticks = pygame.time.get_ticks()  # Start timer #
    writeScore = 0

    while running:  # While start the game #
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
            elif event.type == QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:  # If user clicks #
                mouse_pos = pygame.mouse.get_pos()  # Get the click position #
                if page == "main":

                    # if click on the start button
                    # it will enter the game (Stage 1) #
                    if image_start_rect.collidepoint(mouse_pos):
                        print('game1')
                        page = "game1"

                    # if click on the scoreboard button
                    # it will go to scoreboard page #
                    elif image_scoreboard_rect.collidepoint(mouse_pos):
                        print('scoreboard')
                        page = "scoreboard"

                    # if click on the exit button
                    # it will leave the game #
                    elif image_exit_rect.collidepoint(mouse_pos):
                        return 0

                    # if click on the how to play button
                    # it will show the instruction of the game #
                    elif image_howto_rect.collidepoint(mouse_pos):
                        print('howtoplay')
                        page = "howtoplay"

                elif page == "game1":  # in stage 1 #
                    if image_back_rect.collidepoint(mouse_pos):  # if click on the back button #
                        print("back")  # go back to main manu #
                        page = "main"
                    if image_next_rect.collidepoint(mouse_pos) and num1 == 5: # if user found 5 spots #
                        print("next")  # show next button #
                        page = "game2"  # go to stage 2 #

                    # Set the position value to 1 if user spot the difference
                    # so user can't circle the same position again #
                    if posGame1_1.collidepoint(mouse_pos) and game1_pos[0] == 0:
                        num1 += 1
                        game1_pos[0] = 1
                    elif posGame1_2.collidepoint(mouse_pos) and game1_pos[1] == 0:
                        num1 += 1
                        game1_pos[1] = 1
                    elif posGame1_3.collidepoint(mouse_pos) and game1_pos[2] == 0:
                        num1 += 1
                        game1_pos[2] = 1
                    elif posGame1_4.collidepoint(mouse_pos) and game1_pos[3] == 0:
                        num1 += 1
                        game1_pos[3] = 1
                    elif posGame1_5.collidepoint(mouse_pos) and game1_pos[4] == 0:
                        num1 += 1
                        game1_pos[4] = 1

                elif page == "game2":  # in stage 2 #
                    if image_back_rect.collidepoint(mouse_pos):  # if click on the back button #
                        print("back")  # go back to main manu #
                        page = "main"
                    if image_next_rect.collidepoint(mouse_pos) and num2 == 5:  # if user found 5 spots #
                        print("next")  # show next button #
                        page = "game3"  # go to stage 3 #

                    # Set the position value to 1 if user spot the difference
                    # so user can't circle the same position again #
                    if posGame2_1.collidepoint(mouse_pos) and game2_pos[0] == 0:
                        num2 += 1
                        game2_pos[0] = 1
                    elif posGame2_2.collidepoint(mouse_pos) and game2_pos[1] == 0:
                        num2 += 1
                        game2_pos[1] = 1
                    elif posGame2_3.collidepoint(mouse_pos) and game2_pos[2] == 0:
                        num2 += 1
                        game2_pos[2] = 1
                    elif posGame2_4.collidepoint(mouse_pos) and game2_pos[3] == 0:
                        num2 += 1
                        game2_pos[3] = 1
                    elif posGame2_5.collidepoint(mouse_pos) and game2_pos[4] == 0:
                        num2 += 1
                        game2_pos[4] = 1

                elif page == "game3":  # in stage 3 #
                    if image_back_rect.collidepoint(mouse_pos):  # if click on the back button #
                        print("back")  # go back to main manu #
                        page = "main"
                    if image_next_rect.collidepoint(mouse_pos) and num3 == 5:  # if user found 5 spots #
                        print("next")  # show next button #
                        page = "game4"  # go to stage 4 #

                    # Set the position value to 1 if user spot the difference
                    # so user can't circle the same position again #
                    if posGame3_1.collidepoint(mouse_pos) and game3_pos[0] == 0:
                        num3 += 1
                        game3_pos[0] = 1
                    elif posGame3_2.collidepoint(mouse_pos) and game3_pos[1] == 0:
                        num3 += 1
                        game3_pos[1] = 1
                    elif posGame3_3.collidepoint(mouse_pos) and game3_pos[2] == 0:
                        num3 += 1
                        game3_pos[2] = 1
                    elif posGame3_4.collidepoint(mouse_pos) and game3_pos[3] == 0:
                        num3 += 1
                        game3_pos[3] = 1
                    elif posGame3_5.collidepoint(mouse_pos) and game3_pos[4] == 0:
                        num3 += 1
                        game3_pos[4] = 1

                elif page == "game4":  # in stage 4 #
                    if image_back_rect.collidepoint(mouse_pos):  # if click on the back button #
                        print("back")  # go back to main manu #
                        page = "main"
                    if image_next_rect.collidepoint(mouse_pos) and num4 == 5:  # if user found 5 spots #
                        print("next")  # show next button #
                        page = "game5"  # go to stage 5 #

                    # Set the position value to 1 if user spot the difference
                    # so user can't circle the same position again #
                    if posGame4_1.collidepoint(mouse_pos) and game4_pos[0] == 0:
                        num4 += 1
                        game4_pos[0] = 1
                    elif posGame4_2.collidepoint(mouse_pos) and game4_pos[1] == 0:
                        num4 += 1
                        game4_pos[1] = 1
                    elif posGame4_3.collidepoint(mouse_pos) and game4_pos[2] == 0:
                        num4 += 1
                        game4_pos[2] = 1
                    elif posGame4_4.collidepoint(mouse_pos) and game4_pos[3] == 0:
                        num4 += 1
                        game4_pos[3] = 1
                    elif posGame4_5.collidepoint(mouse_pos) and game4_pos[4] == 0:
                        num4 += 1
                        game4_pos[4] = 1

                elif page == "game5":  # in stage 5 #
                    if image_back_rect.collidepoint(mouse_pos):  # if click on the back button #
                        print("back")  # go back to main manu #
                        page = "main"
                    if image_next_rect.collidepoint(mouse_pos) and num5 == 5:  # if user found 5 spots #
                        print("next")  # show next button #
                        page = "main"  # go to main #

                    # Set the position value to 1 if user spot the difference
                    # so user can't circle the same position again #
                    if posGame5_1.collidepoint(mouse_pos) and game5_pos[0] == 0:
                        num5 += 1
                        game5_pos[0] = 1
                    elif posGame5_2.collidepoint(mouse_pos) and game5_pos[1] == 0:
                        num5 += 1
                        game5_pos[1] = 1
                    elif posGame5_3.collidepoint(mouse_pos) and game5_pos[2] == 0:
                        num5 += 1
                        game5_pos[2] = 1
                    elif posGame5_4.collidepoint(mouse_pos) and game5_pos[3] == 0:
                        num5 += 1
                        game5_pos[3] = 1
                    elif posGame5_5.collidepoint(mouse_pos) and game5_pos[4] == 0:
                        num5 += 1
                        game5_pos[4] = 1
                elif page == "scoreboard":  # in scoreboard page #
                    if image_back_rect.collidepoint(mouse_pos):  # if user click back #
                        print("back")  # go back to main manu #
                        page = "main"
                elif page == "howtoplay":  # in how to play page #
                    if image_back_rect.collidepoint(mouse_pos):  # if user click back #
                        print("back")  # go back to main manu #
                        page = "main"

        # Convert millisecond to second #
        if (page == "game1") or (page == "game2") or (page == "game3") or (page == "game4") or (page == "game5"):
            seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        else:
            start_ticks = pygame.time.get_ticks()

        # Set score in each game as 0 #
        if page == "main":
            writeScore = 0
            num1 = 0
            num2 = 0
            num3 = 0
            num4 = 0
            num5 = 0
            game1_pos = [0, 0, 0, 0, 0]
            game2_pos = [0, 0, 0, 0, 0]
            game3_pos = [0, 0, 0, 0, 0]
            game4_pos = [0, 0, 0, 0, 0]
            game5_pos = [0, 0, 0, 0, 0]
            screen.blit(bghome, (0, 0))
            screen.blit(image_start, image_start_rect)
            screen.blit(image_scoreboard, image_scoreboard_rect)
            screen.blit(image_howto, image_howto_rect)
            screen.blit(image_exit, image_exit_rect)
            pygame.display.flip()

        elif page == "game1":
            screen.blit(bg, (0, 0))
            screen.blit(text_state1, text_state1Rect)
            screen.blit(image_back, image_back_rect)
            screen.blit(image_game1_1, image_game1_1rect)
            screen.blit(image_game1_2, image_game1_2rect)

            text_time = font.render("{:.3f}.s".format(seconds), True, black)  # Show timer #
            text_timeRect = text_time.get_rect()
            text_timeRect.center = (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 210)
            screen.blit(text_time, text_timeRect)

            if num1 == 5:
                screen.blit(image_next, image_next_rect)  # if user found all difference show next button #
            if game1_pos[0] == 1:  # user found the difference #
                pygame.draw.circle(screen, red, [50, 175], 15, 2)  # circle the difference #
            if game1_pos[1] == 1:
                pygame.draw.circle(screen, red, [135, 120], 20, 2)
            if game1_pos[2] == 1:
                pygame.draw.circle(screen, red, [190, 270], 20, 2)
            if game1_pos[3] == 1:
                pygame.draw.circle(screen, red, [265, 350], 20, 2)
            if game1_pos[4] == 1:
                pygame.draw.circle(screen, red, [75, 380], 20, 2)
            find(num1)
            pygame.display.flip()

        elif page == "game2":
            screen.blit(bg, (0, 0))
            screen.blit(text_state2, text_state2Rect)
            screen.blit(image_back, image_back_rect)
            screen.blit(image_game2_1, image_game2_1rect)
            screen.blit(image_game2_2, image_game2_2rect)

            text_time = font.render("{:.3f}.s".format(seconds), True, black)  # Show timer #
            text_timeRect = text_time.get_rect()
            text_timeRect.center = (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 210)
            screen.blit(text_time, text_timeRect)

            if num2 == 5:
                screen.blit(image_next, image_next_rect)  # if user found all difference show next button #
            if game2_pos[0] == 1:  # user found the difference #
                pygame.draw.circle(screen, red, [260, 140], 20, 2)  # circle the difference #
            if game2_pos[1] == 1:
                pygame.draw.circle(screen, red, [80, 140], 20, 2)
            if game2_pos[2] == 1:
                pygame.draw.circle(screen, red, [105, 205], 10, 2)
            if game2_pos[3] == 1:
                pygame.draw.circle(screen, red, [140, 230], 10, 2)
            if game2_pos[4] == 1:
                pygame.draw.circle(screen, red, [50, 310], 20, 2)

            find(num2)
            pygame.display.flip()

        elif page == "game3":
            screen.blit(bg, (0, 0))
            screen.blit(text_state3, text_state3Rect)
            screen.blit(image_back, image_back_rect)
            screen.blit(image_game3_1, image_game3_1rect)
            screen.blit(image_game3_2, image_game3_2rect)

            text_time = font.render("{:.3f}.s".format(seconds), True, black)  # Show timer #
            text_timeRect = text_time.get_rect()
            text_timeRect.center = (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 210)
            screen.blit(text_time, text_timeRect)

            if num3 == 5:
                screen.blit(image_next, image_next_rect)  # if user found all difference show next button #
            if game3_pos[0] == 1:  # user found the difference #
                pygame.draw.circle(screen, red, [110, 140], 35, 2)  # circle the difference #
            if game3_pos[1] == 1:
                pygame.draw.circle(screen, red, [152, 188], 10, 2)
            if game3_pos[2] == 1:
                pygame.draw.circle(screen, red, [180, 270], 10, 2)
            if game3_pos[3] == 1:
                pygame.draw.circle(screen, red, [100, 350], 20, 2)
            if game3_pos[4] == 1:
                pygame.draw.circle(screen, red, [50, 310], 20, 2)

            find(num3)
            pygame.display.flip()

        elif page == "game4":
            screen.blit(bg, (0, 0))
            screen.blit(text_state4, text_state4Rect)
            screen.blit(image_back, image_back_rect)
            screen.blit(image_game4_1, image_game4_1rect)
            screen.blit(image_game4_2, image_game4_2rect)

            text_time = font.render("{:.3f}.s".format(seconds), True, black)  # Show timer #
            text_timeRect = text_time.get_rect()
            text_timeRect.center = (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 210)
            screen.blit(text_time, text_timeRect)

            if num4 == 5:
                screen.blit(image_next, image_next_rect)  # if user found all difference show next button #
            if game4_pos[0] == 1:  # user found the difference #
                pygame.draw.circle(screen, red, [60, 135], 20, 2)  # circle the difference #
            if game4_pos[1] == 1:
                pygame.draw.circle(screen, red, [240, 150], 25, 2)
            if game4_pos[2] == 1:
                pygame.draw.circle(screen, red, [160, 215], 20, 2)
            if game4_pos[3] == 1:
                pygame.draw.circle(screen, red, [58, 335], 20, 2)
            if game4_pos[4] == 1:
                pygame.draw.circle(screen, red, [252, 340], 30, 2)

            find(num4)
            pygame.display.flip()

        elif page == "game5":
            screen.blit(bg, (0, 0))

            screen.blit(text_state5, text_state5Rect)
            screen.blit(image_back, image_back_rect)
            screen.blit(image_game5_1, image_game5_1rect)
            screen.blit(image_game5_2, image_game5_2rect)

            if num5 < 5:
                text_time = font.render("{:.3f}.s".format(seconds), True, black)  # Show timer #
                text_timeRect = text_time.get_rect()
                text_timeRect.center = (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 210)
                screen.blit(text_time, text_timeRect)

            if num5 == 5:
                screen.blit(image_next, image_next_rect)  # if user found all difference show next button #
            if game5_pos[0] == 1:  # user found the difference #
                pygame.draw.circle(screen, red, [60, 175], 20, 2)  # circle the difference #
            if game5_pos[1] == 1:
                pygame.draw.circle(screen, red, [218, 258], 15, 2)
            if game5_pos[2] == 1:
                pygame.draw.circle(screen, red, [262, 230], 15, 2)
            if game5_pos[3] == 1:
                pygame.draw.circle(screen, red, [265, 275], 15, 2)
            if game5_pos[4] == 1:
                pygame.draw.circle(screen, red, [252, 310], 15, 2)

            find(num5)
            if num5 == 5 and writeScore == 0:
                file1 = open("ScorePhoto.txt", "r")  # Read file #
                r = file1.read()
                data = r.split("\n")  # Split the data #
                data_float = []
                for i in range(len(data)):
                    if data[i] != '':
                        data_float.append(float(data[i]))  # Convert string to float #
                data_float.sort()   # Ascending order score #
                file1.close()

                file1 = open("ScorePhoto.txt", "w")  # Write file #
                # Check whether scoreboard is more than 10 or not #
                if len(data_float) < 10:  # if it's less than 10 #
                    time_count = seconds
                    data_float.append(seconds)
                    data_float.sort()  # Sort data #
                    for i in range(len(data_float)):
                        file1.write(str(data_float[i]) + "\n")  # Store data #
                else:  # if it's more than 10 #
                    if seconds < data_float[9]:
                        time_count = seconds
                        data_float[9] = seconds
                        data_float.sort()  # Sort data #
                        for i in range(len(data_float)):
                            file1.write(str(data_float[i]) + "\n")  # Store data #
                file1.close()
                writeScore += 1
            if writeScore == 1:
                text_time = font.render("{:.3f}.s".format(seconds), True, black)  # Set time into 0.000 format #
                text_timeRect = text_time.get_rect()
                text_timeRect.center = (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 210)
                screen.blit(text_time, text_timeRect)

        # Scoreboard page #
        elif page == "scoreboard":
            screen.blit(bgscore, (0, 0))  # Show scoreboard background #
            screen.blit(image_back, image_back_rect)

            file1 = open("ScorePhoto.txt", "r")  # Read file #
            r = file1.read()
            data = r.split("\n")  # Split the data #
            data_float = []
            for i in range(len(data)):
                if data[i] != '':
                    data_float.append(float(data[i]))
            data_float.sort()  # Sort data #
            file1.close()

            for i in range(len(data_float)):  # Show scoreboard #
                text_score = font.render("{} : {:.3f} seconds".format(i+1, data_float[i]), True, black)
                text_scoreRect = text_score.get_rect()
                text_scoreRect.center = (300, 130 + 30 * i)
                screen.blit(text_score, text_scoreRect)

        # How to play page #
        elif page == "howtoplay":
            screen.blit(bghowtoplay, (0, 0))  # Show how to play instruction #
            screen.blit(image_back, image_back_rect)

        pygame.display.flip()

    pygame.quit()
