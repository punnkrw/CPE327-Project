import pygame, sys

def updateHighScores(userScore, screen):
    ###get user's name and adds score to file###
    pygame.init()
    permittedLetters= "abcdefghijklmnopqrstuvwxyz"
    userName = ""

    #show score to the screen and ask for user's name
    endScreenFont = pygame.font.SysFont("Press Start 2P", 20)
    endScreenLine1 = endScreenFont.render("Your score is: "+str(userScore),True,(0,0,0),(217, 225, 232))
    endScreenLine2 = endScreenFont.render("Please enter your name: ",True, (0,0,0),(217, 225, 232))
    
    endScreenLine1 = endScreenLine1.convert()
    endScreenLine2 = endScreenLine2.convert()
    screen.blit(endScreenLine1,(160,70))
    screen.blit(endScreenLine2,(100,120))
    pygame.display.update()

    userIsEnteringName = True
    while userIsEnteringName:
        #loop until the user press enter key
        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:
                if pygame.key.name(event.key) in permittedLetters:
                    #adds the character from input
                    if pygame.key.get_mods() == 1:
                        #detects whether shift key is pressed for uppercase letters
                        userName += pygame.key.name(event.key).upper()
                    else:
                        userName += pygame.key.name(event.key)
                    #shows the input on the screen
                    displayUserInputOnScreen(userName, endScreenFont, screen)
                elif pygame.key.name(event.key)== "return":
                    #only allow the user to continue if they entered name
                    if not(userName==""):
                        userIsEnteringName = False
                elif pygame.key.name(event.key)== "backspace":
                    #removes the last character from user's name
                    userName = userName[:len(userName)-1]
                    displayUserInputOnScreen(userName, endScreenFont, screen)
            elif event.type == pygame.QUIT: #program closes when player closes window
                pygame.quit()
                sys.exit()

    addUserScoreToTextFile(userScore,userName)

def addUserScoreToTextFile(userScore, userName):
    ##adds the user's score to the text file###
    
    #opens ScoreStroop.txt
    highScoreFile = open("ScoreStroop.txt", "a+")
    #puts the user's name in text file
    highScoreFile.write(userName+"\n")
    #puts the user's score in text file
    highScoreFile.write(str(userScore)+"\n")
    highScoreFile.close()

def displayHighScores(screen, background):
    ##show the top scores from the text file on the screen###
    
    highScoresRaw = [] #storing raw output from the text file
    highScores =[] #storing the highscores in a 2d list
    #seperated into name and scores
    highScoreFile = open("ScoreStroop.txt", "r")
    for line in highScoreFile:
        #steps through the text file getting each of the lines, striping them
        #of the new line characters and adding them to highScoresRaw
        highScoresRaw.append(line.rstrip())
    for i in range(0,len(highScoresRaw),2):
        #gets every 2 items from highScoresRaw and puts them in highScores
        highScores.append((int(highScoresRaw[i+1]),highScoresRaw[i]))

    #sorts the high scores so highest are at the top    
    highScores.sort(reverse = True)
    
    background = pygame.image.load("Background/NewScore.png")
    screen.blit(background,(0,0))
    
    highScoreFont = pygame.font.SysFont("Press Start 2P", 20)
    scoreText = []
    userNamesText = []
    nameColour = (0,0,0)

    for j in range(0, len(highScores)):
        #write the name to the screen
        userNamesText.append(highScoreFont.render(highScores[j][1], True,nameColour))
        screen.blit(userNamesText[j],(200,130+j*50))
        #wrtie the score to the screen
        scoreText.append(highScoreFont.render(str(highScores[j][0]), True, nameColour))
        screen.blit(scoreText[j], (400, 130+j*50))

    pygame.display.update()

    #back to main menu
    userIsLookingAtScores = True
    while userIsLookingAtScores:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                userIsLookingAtScores = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                userIsLookingAtScores = False
    
def displayUserInputOnScreen(userName, font, screen):
    #display user's input
    #box creates a blank space for the user's name
    
    resetbox = pygame.Surface([640,480], pygame.SRCALPHA, 32)
    resetbox = resetbox.convert_alpha()
    
    screen.blit(resetbox,(0,200))
    
    userInputText = font.render(userName,True,(0,0,25),(217, 225, 232))
    userInputText.convert()
    #centered name
    screen.blit(userInputText,(round((600-userInputText.get_width())/2),200))
    pygame.display.update()
