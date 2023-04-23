import pygame
from pprint import pprint
import tkinter

from generate_board import generate_board
from prefix_tree import PrefixTree
from combinations import Combinations

class Board_Screen():
    def __init__(self,players=False,setting=1,size=4):
        pygame.init()
        if(players):
            print("2P")
        else:
            if(setting==1):
                print("1P E")
            if(setting==2):
                print("1P M")
            if(setting==3):
                print("1P H")
        screen_height = 800
        screen_width = 1000
        self.game_board=generate_board(size)
        #"C:\\Users\\crmoo\\Documents\\GitHub\\Boggle\\build\\platformerGraphics_gui_text\\Individual\\Upper_A.png"
        #pygame.image.load(self.getLetterImage('a'))
        #"C:\\Users\\zackl\\Documents\\GitHub\\Boggle\\build\\platformerGraphics_gui_text\\Individual\\"
        board_images = []
        i=0
        for x in self.game_board:
            for k in x:
                board_images.append(pygame.transform.scale(pygame.image.load(Board_Screen.getLetterImage(self,k)),(67,56)))
                i+=1

        entryBox = tkinter.Entry()

        pprint(self.game_board)
        background_color = (0, 76, 153)

        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption('Boggle!')
        pygame.display.flip()

        font = pygame.font.SysFont('Georgia', 40, bold = True)
        title_font = pygame.font.SysFont('Georgia', 60, bold = True)

        title_text = title_font.render('Boggle!', True, 'white')
        title_rect = pygame.Rect(375, 100, 200, 60)

        quit_text = font.render('Quit', True, 'white')
        quit_button = pygame.Rect(150, 600, 200, 60)

        boggle_squares = []
        square_side_length = 150
        count = 0
        while(count<size*size):
            left = (count%4)*square_side_length+(2*screen_width/3)-(2*square_side_length)
            top = (count//4)*square_side_length+(screen_height/2)-(2*square_side_length)
            boggle_squares.append(pygame.Rect(left,top,square_side_length,square_side_length))
            count+=1

        running = True
        clock = pygame.time.Clock()
        secondTimer = 1000
        timeLimit = 1000*60*3
        pygame.time.set_timer(pygame.QUIT,timeLimit,1)
        while running:
            screen.fill(background_color)
            #Clock prints time since start every second
            clock.tick(60)
            timeLimit -= clock.get_time()
            secondTimer+=clock.get_time()
            if(secondTimer>1000):
                secondTimer-=1000
                print(timeLimit//1000)
                clock_text = font.render(str(timeLimit//60000)+":"+str((timeLimit//1000)%60),True,'White')
            screen.blit(clock_text,((screen_width*2/3)-40,30))

            pygame.draw.line(screen, 0, (screen_width/3,0), (screen_width/3,screen_height), 4)
            pygame.draw.line(screen, 0, (0,(screen_height/4)*3), (screen_width/3,(screen_height/4)*3), 4)

            i=0
            for x in boggle_squares:
                pygame.draw.rect(screen, 0, x, 2)
                screen.blit(board_images[i],(x.x+40,x.y+40))
                i+=1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if quit_button.collidepoint(event.pos):
                        pygame.quit()
            a, b = pygame.mouse.get_pos()
            pygame.display.update()
    
    def getLetterImage(self,cha):
        #pathToFile is just here so the files will display. I have no clue how to make the files display with specifying the whole filepath
        pathToFile="C:\\Users\\zackl\\Documents\\GitHub\\Boggle\\build\\platformerGraphics_gui_text\\Individual\\"
        return pathToFile+"Upper_"+cha.upper()+".png"

            
#This is just here to open the screen when this program is called
Board_Screen(True,1)
