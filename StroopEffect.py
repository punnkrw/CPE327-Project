import pygame, sys, os
import random
import highScoreCheck
import showHowTo

pygame.init()
screen = pygame.display.set_mode((640, 480))
background = pygame.image.load("Background/NewHome.png")

pygame.display.set_caption("Stroop Effect")

class buttonStroop():
    ### Menu buttons ###
    def __init__(self,screen,left,top,width,height,name):
        self.label = name
        self.buttonColor = (240,255,255) #white buttons
        self.buttonRect = pygame.Rect(left,top,width,height)
        self.buttonSurface = pygame.Surface(self.buttonRect.size)

    def drawButton(self,screen):
        ### Draws a button for the menu ###
        self.buttonSurface.fill(self.buttonColor)
        self.buttonSurface.convert()
        screen.blit(self.buttonSurface, (self.buttonRect.x,self.buttonRect.y))
        pygame.draw.rect(self.buttonSurface,self.buttonColor, self.buttonRect,1)
        self.drawText(screen)

    def drawText(self, screen):
        ### write text on button ###
        buttonTextFont = pygame.font.SysFont("Impact", 30) #text font
        buttonText = buttonTextFont.render(self.label,True,(0,0,0),self.buttonColor) #button font's color
        buttonText = buttonText.convert()
        screen.blit(buttonText,self.buttonRect)        

class coloredWord():
    ###color word in the game###

    def __init__(self,fontColor, word):    
        wordFont = pygame.font.SysFont("Press Start 2P",40)    
        self.theColorText = wordFont.render(word,True,fontColor)
        self.position = [random.randrange(60,290),random.randrange(60,310)] #random position for each color

    def drawWord(self,screen):
        screen.blit(self.theColorText, self.position)

    def moveWord(self, screen, vector, backgroundColor):    
        wordClearSurface = pygame.Surface(self.theColorText.get_size())
        wordClearSurface.fill((backgroundColor))
        screen.blit(wordClearSurface, self.position)

        if not(0 < self.position[0] < 260):
            vector[0] = -1*vector[0]    
        if not(40 < self.position[1] < 280):
            vector[1] = -1*vector[1]
                    
        self.position[0] += vector[0]
        self.position[1] += vector[1]
        screen.blit(self.theColorText, self.position)

def drawMenu(screen, background, playButton, highScoreButton, howToButton): #,backButton
    ### blit background and menu buttons to screen ###
    
    #makes the background grey
    #background.fill((240,255,255))
    background = background.convert()
    screen.blit(background, (0,0))
    #draws the menu buttons
    playButton.drawButton(screen)
    highScoreButton.drawButton(screen)
    howToButton.drawButton(screen)
    backButton.drawButton(screen)

def playGame():
    ### main game loop | draws colors to the screen in different colors 
    ### and check if the player click the correct button -> add thier score by 1 ###
    
    gameBackground = pygame.image.load("Background/NewGame3.png")
    screen.blit(background,(0,0))

    pygame.display.update()
    gameBackground.convert()
    
    #6 colors
    colors = (("Red",(238,0,0)),("Green",(0,205,0)),("Blue",(0,191,255)),
               ("Yellow",(255,215,0)),("Pink",(255,110,180)),("Purple",(142,56,142)))
    
    colorButtonRects = []
    drawGameButtons(colorButtonRects, colors)
    userScore = 0
    timer = 0.0
    timelimit = 30
    FPS = 40
    
    while timer<timelimit:
    
        clock = pygame.time.Clock() #updates clock
        milliseconds = clock.tick(FPS)
        timer += milliseconds /1000
        isMoving = False
        
        fontColorIndex = random.randrange(0,6)
        fontColor = colors[fontColorIndex][1]
        word = colors[random.randrange(0,6)][0]

        theColoredWord = coloredWord(fontColor, word)
        
        #if score more than 5, change bg
        #if more than 10, move the word
        #if userScore >= 5:
            
            #backGroundColorIndex = random.randrange(0,6)
            
            #while backGroundColorIndex == fontColorIndex:
                #backGroundColorIndex = random.randrange(0,6)
            #backgroundColor = colors[backGroundColorIndex][1]
            #gameBackground.fill(backgroundColor)
            
        #if userScore >= 10:
            #isMoving = True
            #movementVector = [random.randrange(-5,5),random.randrange(-5,5)]
    
        screen.blit(gameBackground, (0,0))
        
        #SCORE on top of screen
        displayHeaderInfo("Score: " + str(userScore), 1, (186, 212, 251))
        theColoredWord.drawWord(screen)
        pygame.display.flip() 

        #while loop runs until the user click the correct color
        userClicked = False
        while userClicked == False and timer<timelimit:

            if isMoving == True:
                theColoredWord.moveWord(screen)
                #theColoredWord.moveWord(screen,movementVector, backgroundColor)

            milliseconds = clock.tick(FPS)
            timer += milliseconds /1000
            
            displayHeaderInfo("Timer: " + str(round(timer)), 2, (255,255,255))
            pygame.display.flip()
            
            #close program                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(len(colorButtonRects)):
                        #check cursor position if its click on the right answer
                        if (colorButtonRects[i].collidepoint(pygame.mouse.get_pos())
                            and i == fontColorIndex):
                            userClicked = True
                            userScore +=1
                            screen.blit(gameBackground, (0,0)) 
    
    #gameBackground.fill((186, 212, 251))
    screen.blit(gameBackground,(0,0))

    highScoreCheck.updateHighScores(userScore, screen)
                                      
def drawGameButtons(buttonRects, colors):
    ### color buttons at bottom of the screen and creates rects
    ### around them -> displays color's name on the button ###
    buttonColor = (234,234,234)
    buttons = list()
    #six buttons for colors in game screen
    for i in range(len(colors)):
        
        if i <=2:
            #first 3
            buttonRects.append(pygame.Rect(i*220,380,250,50))
            
        else:
            #second 3
            buttonRects.append(pygame.Rect((i-3)*220,430,250,50))

        buttons.append(pygame.Surface(buttonRects[i].size))
        buttons[i].fill(buttonColor) #same size and color

        #same surface and position w/ rectangles
        screen.blit(buttons[i],(buttonRects[i].x,buttonRects[i].y))
        pygame.draw.rect(buttons[i],buttonColor,buttonRects[i],200)

        buttonFont = pygame.font.SysFont("Press Start 2P", 22)
        #text's color on the button
        buttonText = buttonFont.render(colors[i][0],True,(0,55,90,0))
        buttonText = buttonText.convert_alpha()
        screen.blit(buttonText,(buttonRects[i].x+50,buttonRects[i].y+5))
        
def displayHeaderInfo(text, position, color):
    ### score and timeer at top of the screen ###
    Font = pygame.font.SysFont("Press Start 2P", 20)
    Text = Font.render(text,True,(0,0,0),(144, 179, 216))
    Text = Text.convert()
    screen.blit(Text,(600-(200*position),10))

playButton= buttonStroop(screen,200,280,250,40,"                 START")
highScoreButton = buttonStroop(screen,200,330,250,40,"                 SCORE")
howToButton = buttonStroop(screen,200,380,250,40,"          HOW TO PLAY")
backButton = buttonStroop(screen,200,430,250,40,"                  BACK")

def stroop_home():

    drawMenu(screen, background, playButton, highScoreButton, howToButton)  #backButton

    while True:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONUP:
                
                if playButton.buttonRect.collidepoint(pygame.mouse.get_pos()):
                    
                    #play the game when the mouse button is released over the play button
                    playGame()
                    #go back to menu when finish playing
                    drawMenu(screen,background, playButton, highScoreButton, howToButton)
                    
                elif highScoreButton.buttonRect.collidepoint(pygame.mouse.get_pos()):
                    
                    #show highscore
                    highScoreCheck.displayHighScores(screen,background)
                    #go back to menu when finish playing
                    drawMenu(screen,background, playButton, highScoreButton, howToButton)
                    
                elif howToButton.buttonRect.collidepoint(pygame.mouse.get_pos()):
                    
                    #show hint
                    showHowTo.displayHowTo(screen,background)
                    #go back to menu when finish playing
                    drawMenu(screen,background, playButton, highScoreButton, howToButton)
                    
                elif backButton.buttonRect.collidepoint(pygame.mouse.get_pos()): ############### กลับไปเมนูหลัก
                    from main import homepage
                    homepage()

            #changes the color of the button when mouse put over button
            elif playButton.buttonRect.collidepoint(pygame.mouse.get_pos()):
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    playButton.buttonColor = (153,153,153) #grey
                    
                else:
                    playButton.buttonColor = (207,207,207) #pale grey
                playButton.drawButton(screen)
                pygame.display.flip()
                
            elif highScoreButton.buttonRect.collidepoint(pygame.mouse.get_pos()):
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    highScoreButton.buttonColor = (153,153,153) #grey
                    
                else:
                    highScoreButton.buttonColor = (207,207,207) #pale grey
                highScoreButton.drawButton(screen)
                pygame.display.flip()
                
            elif howToButton.buttonRect.collidepoint(pygame.mouse.get_pos()):
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    howToButton.buttonColor = (153,153,153) #grey
                    
                else:
                    howToButton.buttonColor = (207,207,207) #pale grey
                howToButton.drawButton(screen)
                pygame.display.flip()
                
            elif backButton.buttonRect.collidepoint(pygame.mouse.get_pos()):
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    backButton.buttonColor = (153,153,153) #grey
                    
                else:
                    backButton.buttonColor = (207,207,207) #pale grey
                backButton.drawButton(screen)
                pygame.display.flip()
                
            else:
                playButton.buttonColor = (217, 199, 178) #brown
                playButton.drawButton(screen)
                highScoreButton.buttonColor = (217, 199, 178)
                highScoreButton.drawButton(screen)
                howToButton.buttonColor = (217, 199, 178)
                howToButton.drawButton(screen)
                backButton.buttonColor = (217, 199, 178)
                backButton.drawButton(screen)
                
                pygame.display.flip()
                
    pygame.quit()
