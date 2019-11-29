# Ali Meshkat, Bill Liu
# Big Bug's Mania


#importing required modules 
import pygame
import math
import time
import timeit
import os
pygame.init()#initiates pygame

#defining colours using RGB / constants 
black = (0,0,0)
white =(255,255,255)
red = (200,0,0)
blue = (0,0,180)
green = (0,200,0)

bright_green = (0,255,0)
bright_red = (255,0,0)
bright_Blue= (0,0,255)

brightRed = (255, 50, 50)
brightBrightRed = (255, 100, 100)

brightGreen = (50, 255, 50)
brightBrightGreen = (100, 255, 100)

brightBlue = (50, 50, 255)
brightBrightBlue = (100, 100, 255)

purple = (145,58,154)
bright_purple = (175,74,187)

pink = (231,73,235)

orange = (226,102,41)

dark_grey = (91,85,108)
light_grey = (130,121,151)

bright_brown = (122,49,7)
brown = (87,45,9)

#setting the display
display_width = 800     
display_height = 600
gameDisplay = pygame.display.set_mode( ( display_width,display_height ) )  

#name of the display window 
pygame.display.set_caption("Big Bug's Mania") 

#setting up the clock to time
#will continue to count for the entire game
clock = pygame.time.Clock() 
start = timeit.default_timer()

# global variables 
gameWave = 0 
pause = False 
selectedSlot = 1
money = 300
flowersLeft = 50

###importing sounds and plays the music(sound track) in a different window
os.system ("start C:/Users/Ali/Desktop/BigBug'sMania/Code/music.mp4")

#importing images 
tower1Img = pygame.image.load("tower1.png")
tower1Lvl2Img = pygame.image.load("tower1lvl2.png")
tower1Lvl3Img = pygame.image.load("tower1lvl3.png")
tower2Img = pygame.image.load ("tower2.png")
spiderImg = pygame.image.load("spider.png")
introBackground = pygame.image.load("intro background.png")
setUpBackground  = pygame.image.load("during background3.png")
duringBackground = pygame.image.load("during background3.png")
introductionsBackground = pygame.image.load("instructions background.png")
endScreen = pygame.image.load("end screen.png")
loseScreenBackground = pygame.image.load("lose screen.png")
#makes displaying shapes shorter and easier 
def display(img,x,y): 
    gameDisplay.blit(img,(x,y))

#makes the texts into obejects that can be shown 
def text_objects(text, font): 
    textSurface = font.render(text,True, black)
    return textSurface, textSurface.get_rect()

#displays text on the specified part on the screen with the chosen font size 
def message_display(text,x,y,fontSize):
    largeText = pygame.font.Font("freesansbold.ttf", fontSize) #defining the font and size 
    TextSurf, TextRect = text_objects(text, largeText) #makes the text into objects first
    TextRect.center = ((x), (y))#centres the text in an imaginary rectangle 
    gameDisplay.blit(TextSurf, TextRect)#displays screen 

#allows quitting the game using only one command (the X at the top right would work for the game window as well as the program window)
def quitGame():  
    pygame.quit()#ends pygame 
    quit()#closes the window 

#button function to make a button
def button (msg, x, y, w, h, ic, ac, font, action=None):
    mouse = pygame.mouse.get_pos()#gets position of the mouse 
    click = pygame.mouse.get_pressed()#position of cclick 
    if x+w > mouse[0] > x and y+h > mouse[1] > y:#if mouse is on top of button 
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))#changes to active 
        if click[0] == 1 and action != None:#if clicked 
            action()#runs the action 
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))#inactive colour 
    smallText = pygame.font.SysFont("comicsansms", font)
    textSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = ((x+w/2), (y+h/2))
    gameDisplay.blit(textSurf, TextRect)

def instructions():#instructions page 
    introduction = True 
    while introduction:
         for event in pygame.event.get(): #quit function
            if event.type == pygame.QUIT:
                quitGame()
            gameDisplay.fill(white) #clears the screen first
            display (introductionsBackground, 0 , 0) #displays the instructions
            button("Back", 10, 10, 50,50, purple, pink, 15, end) #takes the user back to the main menu
            pygame.display.update()

#function to go to the game
def endDuring():
    introductions = False
    during()

#function to go from the instructions page to the main menu
def end():
    introduction = False
    introScreen()


###################################################################intro screen ##########################################################################
gameStart = False
def introScreen():
     # to avoid pressing on the sharp shooter before setUP begins 
    #declaring global variables
    
    global gameStart
    introduction = False 
    while gameStart == False and gameWave != 21 and flowersLeft > 0:#while game has not begun 
        for event in pygame.event.get():#if user wants to quit using the X button
            if event.type == pygame.QUIT:
                quitGame()
        gameDisplay.fill(white) # fills screen with white so changes can take place 
        display(introBackground, 0 , 0) #background 
        button("Play Game", 525, 100, 250, 65, bright_purple, pink, 45, waves)
        button("How to Play", 585, 170, 125, 30, red, bright_red, 20, instructions)
        pygame.display.update()#updates the screen, changes appear
##########################################################################################################################################################
#path coordinates
left_turn1Y = 330#
left_turn1X = -14 + 40

left_turn2Y = 330#
left_turn2X = 110+ 40##

right_turn1Y = 210###
right_turn1X = 110+ 40##

right_turn2Y = 210###
right_turn2X = 240+ 40####

left_turn3Y = 400#####5
left_turn3X = 240+ 40####

left_turn4Y = 400#####5
left_turn4X = 560+ 40######6

left_turn5Y = 190#######7
left_turn5X = 560+ 40######6

right_turn3Y = 40#######7
right_turn3X = 320+ 40########8

right_turn4Y = 40
right_turn4X = 320+ 40########8

flowersX = 410+ 40
speed = 2#speed of the pests pixels per(s/60)

#code to move the bugs to the course, without collision detection
def moooooooooove():
    global flowersLeft
    for i in range (0,19): 
        if health[i] > 0:
            if pestY[i] != left_turn1Y and pestX[i] == left_turn1X: #each comment at the end of each boolean shows where the pest will be  
                pestY[i] += speed #the first time statement is true
            elif pestY[i] == left_turn1Y and pestX[i] != left_turn2X and pestX[i] != right_turn2X and pestX[i] != left_turn4X and pestX[i] != left_turn5X:#left_turn1
                pestX[i] += speed #changes the moving direction
            elif pestY[i] != right_turn1Y and pestX[i] == right_turn1X:#left_turn2
                pestY[i] -= speed 
            elif pestY[i] == right_turn1Y and pestX[i] != right_turn2X and pestX[i] != right_turn4X and pestX[i] != left_turn4X:#rightTrn1
                pestX[i] += speed 
            elif pestY[i] != left_turn3Y and pestX[i] == right_turn2X :#rightTurn2
                pestY[i] += speed
            elif pestY[i] == left_turn3Y and pestX[i] != left_turn4X:#leftTurn3
                pestX[i] += speed
            elif pestY[i] != left_turn5Y and pestX[i] == left_turn4X and pestY[i] != right_turn4Y:#leftTurn4
                pestY[i] -= speed
            elif pestY[i] == left_turn5Y and pestX[i] != right_turn3X:#leftTurn5
                pestX[i] -= speed 
            elif pestY[i] != right_turn4Y and pestX[i] == right_turn3X and pestY[i] != left_turn3Y :#rightTrn3
                pestY[i] -= speed
            elif pestY[i] == right_turn4Y and pestX[i] != flowersX:#rightTurn4
                pestX[i] += speed
            if pestX[i] != flowersX or pestY[i] != right_turn4Y:
                display(spiderImg, pestX[i],pestY[i])
            else:
                flowersLeft -= 1
                health[i] = 0

#slots coordinates and number(values)
slot = [0,0,0,0,0,0,0,0] #slot array
slotX = [98,220,345,345,545,545,305,425]
slotY = [260,286,265,330,330,265,125,115]
slotXW = [127,250,375,375,580,580,333,450] #X coordinate of slot + width 
slotYH = [300,330,310,375,375,310,170,155] #Y coordinate of slot + Height

#Sharpshooter
ssRangeLvl1 = 120   
ssRangeLvl2 = 150   
ssRangeLvl3 = 205   
ssDamageLvl1 = 1    
ssDamageLvl2 = 2    
ssDamageLvl3 = 3    
#curtainSpayer
csRangeLvl1 = 100   
csRangeLvl2 = 125   
csRangeLvl3 = 135   
csDamageLvl1 = 3    
csDamageLvl2 = 5    
csDamageLvl3 = 9    

#function used to decrease pests' health and award money for any pest put to sleep 
def shoooooooooot():
    global money
    moneyPerPest = gameWave
    for i in range (0,8): #used to go through all slots 
        for p in range (0,19):#used to go through all pests  
            if health[p] > 0:# if not already put to sleep
                if pestX[p] > 0 and pestY[p] > 0:                        
                    sqX = (slotX[i] - (pestX[p] + 23))** 2#using pythagorean theorem to find distance 
                    sqY = (slotY[i] - (pestY[p] + 23)) ** 2#using pythagorean theorem to find distance 
                    if slot[i] == 1:# if slot's value is 1 (first tower)
                        if math.sqrt(sqX + sqY) <= ssRangeLvl1 :#using pytagorean theorem to find distance 
                            if health[p] - ssDamageLvl1 > 0: 
                                health[p] -= ssDamageLvl1#decreases health based on damage of first tower
                            else:#if pest dies
                                money += moneyPerPest# money awarded 
                                health[p] = 0 
                    if slot[i] == 2:#for slot 2 
                        if math.sqrt(sqX + sqY) <= ssRangeLvl2 :
                            if health[p] - ssDamageLvl2 > 0:
                                health[p] -= ssDamageLvl2
                            else:
                                health[p] = 0
                                money += moneyPerPest
                                
                    if slot[i] == 3:
                        if math.sqrt(sqX + sqY) <= ssRangeLvl3 :
                            if health[p] - ssDamageLvl3 > 0:
                                health[p] -= ssDamageLvl3
                            else:
                                health[p] = 0
                                money += moneyPerPest
                    if slot[i] == 4:
                        if math.sqrt(sqX + sqY) <= csRangeLvl1 :
                            if health[p] - csDamageLvl1 > 0:
                                health[p] -= csDamageLvl1
                            else:
                                health[p] = 0
                                money += moneyPerPest
                    if slot[i] == 5:
                        if math.sqrt(sqX + sqY) <= csRangeLvl2 :
                            if health[p] - csDamageLvl2 > 0:
                                health[p] -= csDamageLvl2
                            else:
                                health[p] = 0
                                money += moneyPerPest
                    if slot[i] == 6:
                        if math.sqrt(sqX + sqY) <= csRangeLvl3 :
                            if health[p] - csDamageLvl3 > 0:
                                health[p] -= csDamageLvl3
                            else:
                                health[p] = 0
                                money += moneyPerPest
  
#########################main game loop#################################
healthSum = 100 # used to get out of during when all pests are dead
def during():
    #declaring global variables used in this function 
    global healthSum
    global selectedSlot 
    global health
    global pestX
    global pestY
    global startX
    global gameStart
    global flowersLeft
    gameStart = True ##game has begun 
    while healthSum != 0 and gameWave != 21 and gameStart and flowersLeft > 0: #second wave not going into this loop 
        healthSum = 100
        for event in pygame.event.get():    #if the user wants to quit using the x button 
            if event.type == pygame.QUIT:
                outOfLives = True
                quitGame()

        #running functions 
        selectedSlotGet()
        gameDisplay.fill(white) # fills the screen with white colour
        display(duringBackground, 0,0)
        moooooooooove()
        shoooooooooot()
        towerDisplay()
        selectedSlotGet()
        selectTower()
        buyTower()
        moneyDisplay()
        displayLife()
        healthBars()
        message_display("Wave " + str(gameWave), 735,465,30) #displays number of wave 
        for i in range (0,19): # adds health of all bugs 
            healthSum += health [i]
        healthSum -= 100
        pygame.display.update() #updates the screen 
        clock.tick(60) #frames/second
##############################################################################

#################################################################Setup########################################################################

#setup page (getting ready for during )
def setup():
    time.sleep(0.15)
    #declaring global variables used in this function
    global money
    global gameStart
    gameStart = False #game is no longer going on
    while not gameStart and gameWave != 21 and flowersLeft > 0: 
        for event in pygame.event.get():    #if the user wants to quit using the x button 
            if event.type == pygame.QUIT:
                outOfLives = True
                quitGame()
        display (duringBackground, 0,0)
        button("Start Wave",685,490,100,100,red,bright_red, 18, during)#when user wants to start next wave 
        #running functions 
        towerDisplay()
        selectedSlotGet()
        selectTower()
        buyTower()
        moneyDisplay()
        displayLife()
        
        message_display("Wave " + str(gameWave), 735,465,30)#displays number of wave 
        pygame.display.update()
        clock.tick(60)
################################################################################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#transition function between during and setup and end screens
def waves():
    #declaring global variables used in this function
    global healthIncrease1
    global healthIncrease2
    global healthSum
    global set1
    global set2
    global health 
    global gameWave
    global startX
    global pestX
    global pestY
    global money
    global flowersLeft
    moneyPerWave = 150 #money awarded for completing each wave
    if gameWave != 1:#makes wave 1 easier by  not increasing health of pests 
        healthIncrease1 = 150 + gameWave * 120 #used to increasingly increase health of pests each wave (first set)
        healthIncrease2 = 200 + gameWave * 150 #used to increasingly increase health of pests each wave (second set)
    while gameWave != 21 and flowersLeft > 0:
        gameWave +=1
        set1 = gameWave * healthIncrease1 #increases health of pests first set 
        set2 = gameWave * healthIncrease2 #increases health of pests second set 
        if gameWave != 1:
            money += moneyPerWave 
        health= [set1,set1,set1,set1,set1,set1,set1,set1,set1,set1,set2,set2,set2,set2,set2,set2,set2,set2,set2,set2]#resetting health 
        pestX= [startX,startX,startX,startX,startX,startX,startX,startX,startX,startX,startX,startX,startX,startX,startX,startX,startX,startX,startX,startX]#resetting positions
        pestY= [-10,-40,-70,-100,-130,-160,-190,-220,-250,-280,-310,-340,-370,-400,-430,-460,-490,-520,-550,-580]#resetting positions 
        healthSum = 1
        setup()#runs setup after changes
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##defined veriables for the bugs
#adding health each round makes them stronger
healthIncrease1 = 150
healthIncrease2 = 200
#variation of bug health creates more suspense
set1 = 1000
set2 = 100
#variables for the bugs to hold and run, including positioning and health
startX = -14 + 40 
health= [set1,set1,set1,set1,set1,set1,set1,set1,set1,set1,set2,set2,set2,set2,set2,set2,set2,set2,set2,set2]
pestX= [startX,startX,startX,startX,startX,startX,startX,startX,startX,startX,startX,startX,startX,startX,startX,startX,startX,startX,startX,startX]
pestY= [-10,-40,-70,-100,-130,-160,-190,-220,-250,-280,-310,-340,-370,-400,-430,-460,-490,-520,-550,-580]

#function used to show the health bars of the pests 
def healthBars():
    #how big the bars will be with outline
    healthBarL = 26
    healthBarW = 5
    healthBarLineWidth = 1
    #shows the health of the first set of pests
    for i in range (0,10):
        if health[i] != 0:
            healthBarFill = (health[i] / (gameWave * healthIncrease1)) * healthBarL   
            pygame.draw.rect(gameDisplay,green,(pestX[i]+10,pestY[i], healthBarL,healthBarW),healthBarLineWidth)
            pygame.draw.rect(gameDisplay,green,(pestX[i]+10,pestY[i], healthBarFill,healthBarW))
    #shows the health of the second set of pests
    for i in range (10,19):
        if health [i] != 0:
            healthBarFill = (health[i] / (gameWave * healthIncrease2)) * healthBarL   
            pygame.draw.rect(gameDisplay,green,(pestX[i]+10,pestY[i], healthBarL,healthBarW),healthBarLineWidth)
            pygame.draw.rect(gameDisplay,green,(pestX[i]+10,pestY[i], healthBarFill,healthBarW))

#displays the flowers or "lives" the user has left
def displayLife():
    message_display(str(flowersLeft),755,90,30)

#displays the current money amount the user has at their disposal    
def moneyDisplay():
    message_display(str(round(money)), 755,30,30)

#after clicking a slot, runs this function to display two buttons to buy the towers
def buyTower():   
    if slot[selectedSlot] == 0:
        pygame.draw.circle(gameDisplay, pink, (slotX[selectedSlot]+14, slotY[selectedSlot]+21), 35,3)
        button("Sharp Shooter  200", 670, 115, 120,95,purple,bright_purple,12,towerPlace1)
        button("Curtain Sprayer  500", 670, 250, 120,95,purple,bright_purple,10,towerPlace2)

#function to buy the sharpshooter tower
def towerPlace1():
    global money
    global ssPrice
    #subtracts the price of the sharpshooter tower
    if money >= ssPrice:
        slot[selectedSlot] = 1
        money -= ssPrice
    else:
        #tells the user they dont have enough money
        #is a click and hold function so the user can read it for as long as they want
        message_display("Insufficient Funds", 400, 300,45)

#function to buy the curtain sprayer tower
def towerPlace2():
    global money
    global csPrice
    #subtracts the price of the curtain sprayer tower
    if money >= csPrice :
        slot[selectedSlot] = 4
        money -= csPrice
    else:
        #again, tells the user they do not have enough money
        message_display("Insufficient Funds", 400, 300,45)

# used to determine which tower slot the user clicks on
def selectedSlotGet():
    global selectedSlot
    buyingTower = False 
    for i in range (0,8):
        mouse = pygame.mouse.get_pos()   #gets position of mouse 
        click = pygame.mouse.get_pressed() #gets position of click 
        if slotXW[i] > mouse[0] > slotX[i] and slotYH[i] > mouse[1] > slotY[i]: #if mouse is in the box of slot
            if click[0] == 1: #if clicked
                selectedSlot = i #selectedslot becomes i (click)

#displays the level tower at the slot it is placed
def towerDisplay():
    for i in range (0,8):
        if slot[i] == 1:
            display(tower1Img, slotX[i], slotY[i]-3)
        elif slot[i] == 2:
            display(tower1Lvl2Img, slotX[i]-6, slotY[i]-5)
        elif slot[i] == 3:
            display(tower1Lvl3Img, slotX[i]-5, slotY[i]-5)
        elif slot[i] == 4:
            display(tower2Img, slotX[i]-8, slotY[i]-3)
        elif slot[i] == 5:
            display(tower2Img, slotX[i]-8, slotY[i]-3)
        elif slot[i] == 6:
            display(tower2Img, slotX[i]-8, slotY[i]-3)



#variabels for select tower, sell tower functions
ssPrice = 200
csPrice = 500
sellPrice1 = ssPrice/2
sellPrice2 = ssPrice
sellPrice3 = ssPrice + ssPrice/2
sellPrice4 = csPrice/2
sellPrice5 = csPrice
sellPrice6 = csPrice + csPrice/2
sellPrice = [100, 200, 300, 250,500, 750]

#function to select the tower and highlight it
def selectTower():
    towerRange = 0

    #draws what range to draw based on the tower  
    if slot[selectedSlot] != 0:
        if slot[selectedSlot] == 1:
            towerRange = ssRangeLvl1
        elif slot[selectedSlot] == 2:
            towerRange = ssRangeLvl2
        elif slot[selectedSlot] == 3:
            towerRange = ssRangeLvl3
        elif slot[selectedSlot] == 4:
            towerRange = csRangeLvl1
        elif slot[selectedSlot] == 5:
            towerRange = csRangeLvl2
        elif slot[selectedSlot] == 6:
            towerRange = csRangeLvl3

        #draws the range of the tower
        pygame.draw.circle(gameDisplay, pink, (slotX[selectedSlot]+16, slotY[selectedSlot]+21), towerRange,4)#draws range to show user which tower is selected 
        message_display("Sell Price: "+str(sellPrice[slot[selectedSlot]-1]), 375, 530,25) #shows sell price
        if slot [selectedSlot] != 3 and slot [selectedSlot] != 6:#if not max upgrade
            message_display("Upgrade Price: " + str(upgradeCost[slot[selectedSlot]-1]),390, 510,25) #shows upgrade price
        else:
            message_display(upgradeCost[slot[selectedSlot]-1],375, 510,25)
        button("Upgrade Tower", 5, 490, 250, 105, green, brightBrightGreen, 35, upgrade_tower) #upgrade tower button
        button("Sell Tower", 350, 545, 60, 50, red, brightBrightRed, 11, sell_tower) #sell tower button


upgradeCost = [ssPrice * 1.5, ssPrice*2, "Max Upgrade", csPrice*1.5 , csPrice * 2, "Max Upgrade"]
###uses selected slot to determine the current tower and if sufficient money available, allows upgrading of towers
def upgrade_tower(): 
    time.sleep(0.5)
    global money
    if money < ssPrice: #checks if the user has enough money for an upgrade
        message_display("Insufficient Funds", 400, 300,45)#diplays at the centre of the screen 
        time.sleep(0.3)
        clock.tick(1)#prevents upgrading twice (click registring twice )
    elif slot[selectedSlot] == 1:
        if money >= upgradeCost [0]:
                slot[selectedSlot] = 2
                money -= upgradeCost [0]
    elif slot[selectedSlot] == 2:
        if money >= upgradeCost [1]:
                slot[selectedSlot] = 3
                money -= upgradeCost [1]
    elif slot[selectedSlot] == 3:
        message_display("Max Upgrade Reached", 400, 300,45)
        time.sleep(0.3)
    elif slot[selectedSlot] == 4:
        if money >= upgradeCost [3]:
                slot[selectedSlot] = 5
                money -= upgradeCost [3]
    elif slot[selectedSlot] == 5:
        if money >= upgradeCost [4]:
                slot[selectedSlot] = 6
                money -= upgradeCost [4]
    elif slot[selectedSlot] == 6:
        message_display("Max Upgrade Reached", 400, 300,45)
        time.sleep(0.3)
    else:
        message_display("No Upgrade Available", 400, 300,45)
        time.sleep(0.3)

def sell_tower():####uses selectedSlot to determine which slot is seleceted and what the tower placed there is, and allows selling of that tower
    global money 
    if slot[selectedSlot] == 1: #adds half ofthe money spent on tower back to the user
        money += sellPrice1
    elif slot[selectedSlot] == 2:
        money += sellPrice2
    elif slot[selectedSlot] == 3:
        money += sellPrice3
    elif slot[selectedSlot] == 4:
        money += sellPrice4
    elif slot[selectedSlot] == 5:
        money += sellPrice5
    elif slot[selectedSlot] == 6:
        money += sellPrice6
    slot[selectedSlot] = 0#changes the value of that slot to 0 after it is sold

def endScreen():
    #starts counting a second timer
    stop = timeit.default_timer()
    timeSpent = round(-(start - stop))
    
    global money
    money = money*1000000 #for the 1000000 times richard will give to the user
    while gameWave != 22:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
        gameDisplay.fill(white)
        display(pygame.image.load("end screen.png"), 0, 0) #displays the background image

        #the quit game button
        button ("quit", 200, 525, 100, 50, blue, bright_Blue, 20, quitGame)
        message_display(str(flowersLeft), 575, 415, 30)#displays time spent on the game 
        message_display(str(money), 575, 365, 30)#displays time spent on the game 

        message_display(str(timeSpent) + " seconds", 575, 465, 30)#displays time spent on the game 

        pygame.display.update()
def loseScreen():
    global money 
    #starts counting a second timer
    stop = timeit.default_timer()
    timeSpent = round(-(start - stop))

    money = money*1000000 #for the 1000000 times richard will give to the user
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitGame()
        gameDisplay.fill(white)
        display(pygame.image.load("lose screen.png"), 0, 0) #displays the background image
        #the quit game button
        button ("quit", 200, 525, 100, 50, blue, bright_Blue, 20, quitGame)
        message_display(str(flowersLeft), 575, 415, 30)#displays time spent on the game 
        message_display(str(money), 575, 365, 30)#displays time spent on the game 
        message_display(str(timeSpent) + " seconds", 575, 465, 30)#displays time spent on the game 
        pygame.display.update()
   
    
#######################################################


#Ruuuuuuuuuns the gameee      
introScreen() 

if flowersLeft <= 0: #checks whether the user won or lost to show which screen
    loseScreen()
else:
    endScreen()
quitGame() #ends the game

