import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600,600))

#Title
pygame.display.set_caption("Minesweeper")
icon = pygame.image.load("bomb.png")
pygame.display.set_icon(icon)

# Win/Lose boolean variables
win = False
lose = False

turns_to_win = 20

# Format to place an image
# randomImg = pygame.image.load("smallMine.png")
# imgX = 400
# imgY = 300

# def img():
#     #Use this to draw images
#     screen.blit(randomImg, (imgX, imgY))

#The Class
class Box:

    bomb_count = 5
    gemCount = 0
    rando = 1

    def __init__(self, xcoord=0, ycoord=0):
        self.xcoord = xcoord
        self.ycoord = ycoord

        Box.gemCount+=1

        self.gemNumber = self.gemCount
        self.bomb = True

        number = random.randint(0,self.bomb_count)
        if (number==0):
            Box.bomb_count-=1

            if (self.bomb_count==0):
                Box.bomb_count=999

        else:
            self.bomb = False

    def printDetails(self):
        print(f"Gem Number: {self.gemNumber}, X.Coord: {self.xcoord}, Y.Coord: {self.ycoord}, Bomb: {self.bomb}")



def reveal(array, row, col):

    if (array[row][col].bomb == False):

        bombs_around = 0

        # Central Areas
        if (row>0 and row < 4 and col>0 and col<4):
            for i in range(row-1, row+2):
                for j in range(col-1, col+2):

                    if (i==row and j==col):
                        continue

                    else:
                        if (array[i][j].bomb == True):
                            bombs_around += 1

        # Corners
            # Top Left
        elif (row == 0 and col == 0):
            for i in range (0,2):
                for j in range(0,2):
                    
                    if (i==0 and j==0):
                        continue
                    
                    else:
                        if (array[i][j].bomb == True):
                            bombs_around += 1

            # Top right
        elif (row == 0 and col == 4):
            for i in range(0,2):
                for j in range(3,5):

                    if (i==0 and j==4):
                        continue

                    else:
                        if (array[i][j].bomb == True):
                            bombs_around += 1

            # Bottom Left
        elif (row == 4 and col == 0):
            for i in range(3,5):
                for j in range(0,2):

                    if (i==4 and col==0):
                        continue

                    else:
                        if (array[i][j].bomb == True):
                            bombs_around += 1

            # Bottom Right
        elif (row == 4 and col == 4):
            for i in range(3,5):
                for j in range(3,5):

                    if (i==4 and j==4):
                        continue
                    
                    else:
                        if (array[i][j].bomb == True):
                            bombs_around += 1


        # Edge rows/columns

            #Top Horizontal row
        elif (row == 0):
            for i in range(0,2):
                for j in range(col-1, col+2):

                    if (i==0 and j==col):
                        continue

                    else:
                        if (array[i][j].bomb == True):
                            bombs_around += 1

            #Bottom Horizontal Row
        elif (row == 4):
            for i in range(3,5):
                for j in range(col-1, col+2):

                    if (i==4 and j==col):
                        continue
                
                    else:
                        if (array[i][j].bomb == True):
                            bombs_around += 1

            #Left Vertical Column
        elif (col == 0):
            for i in range(row-1, row+2):
                for j in range(0,2):

                    if (i==row and j==0):
                        continue

                    else:
                        if (array[i][j].bomb == True):
                            bombs_around += 1

        elif (col == 4):
            for i in range(row-1, row+2):
                for j in range(3,5):

                    if (i==row and j==4):
                        continue

                    else:
                        if (array[i][j].bomb == True):
                            bombs_around += 1

        
        return str(bombs_around)

    else:
        return ("Bomb")


# To Draw the stuff on the screen
def drawText(revealed_array):

    myfont = pygame.font.SysFont("monospace", 32)

    
    y1 = 50

    for i in range(0,5):

        x1=50

        for j in range(0,5):

        
            label = myfont.render(revealed_array[i][j], 1, (0,0,0))

            screen.blit(label, (x1+20, y1+25))

            x1+=100

        y1+=100

def drawWinLose(mystr):

    myfont = pygame.font.SysFont("monospace", 32)

    label = myfont.render(mystr, 1, (0,0,0))

    screen.blit(label, (220, 20))

#Initializing the 2D-Array of Objects
array = [[Box() for j in range(0,5)] for i in range(0,5)]

x,y = 50,50
for i in range(0,5):

    for j in range(0,5):

        array[i][j].xcoord = x
        array[i][j].ycoord = y

        x+=100
    
    y+=100
    x=50

for i in range(0,5):
    for j in range(0,5):
        array[i][j].printDetails()

# This array used to print the revealed thingy's
revealed_array = [['' for i in range(5)] for j in range(0,5)] 

#The Game Loop
running = True
while running:

    #Background color, dont draw anything before this
    screen.fill((135,206,250))

    #Mouse coordinates
    x,y = pygame.mouse.get_pos()

    #Drawing the grid
    red = (255,0,0)
    white = (255,255,255)
    pygame.draw.rect(screen, red, (50,50,500,500))
    pygame.draw.rect(screen, white, (55,55,490,490))
    #pygame.draw.line(screen, red, start_pos, end_pos, width=1)
    for i in range(150, 550, 100):
        pygame.draw.line(screen, red, (50,i), (550,i), 5)

    for i in range(150,550,100):
        pygame.draw.line(screen, red, (i, 50), (i, 550), 5)

    # Font of the text
    font = pygame.font.Font('freesansbold.ttf', 16)

    # For the when clicked thingy
    row,col = 0,0

    for event in pygame.event.get():

        #To close after pressing the top-right "cross" button   
        if (event.type == pygame.QUIT):
            pygame.quit()

        #Print mouse coordinates when mouse pressed
        if (event.type == pygame.MOUSEBUTTONDOWN):
            #print(f"X: {x}, Y: {y}")s

            for number in range(50,551,100):
                if (y/number>1):
                    row+=1

                if (x/number>1):
                    col+=1

            row-=1 
            col-=1

            print (f"You clicked Row: {row}, Col: {col}")
            revealed_array[row][col] = reveal(array, row, col)

            if (revealed_array[row][col] == 'Bomb'):
                lose = True

            else:
                turns_to_win-=1

            print("Following are elements of Revealed Array: ")
            for i in range(0,5):
                for j in range (0,5):

                    print (revealed_array[i][j], end=" ")

            print("")


    drawText(revealed_array)

    if (turns_to_win == 0):
        win = True

    # To move on afterr win/lose
    if (win==True or lose==True):
        running = False
        
    
    #Updates everything in every iteration  
    pygame.display.update()


while not running:

    #Background color, dont draw anything before this
    screen.fill((135,206,250))

    #Mouse coordinates
    x,y = pygame.mouse.get_pos()

    #Drawing the grid
    red = (255,0,0)
    white = (255,255,255)
    pygame.draw.rect(screen, red, (50,50,500,500))
    pygame.draw.rect(screen, white, (55,55,490,490))
    #pygame.draw.line(screen, red, start_pos, end_pos, width=1)
    for i in range(150, 550, 100):
        pygame.draw.line(screen, red, (50,i), (550,i), 5)

    for i in range(150,550,100):
        pygame.draw.line(screen, red, (i, 50), (i, 550), 5)

    drawText(revealed_array)

    for event in pygame.event.get():

        if (event.type == pygame.QUIT):
            pygame.quit()

    if (win == True):
        drawWinLose("You Win!")

    else:
        drawWinLose("You Lose!")

 

    pygame.display.update()