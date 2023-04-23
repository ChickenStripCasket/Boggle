import pygame
from pprint import pprint

from generate_board import generate_board
from main import *
from prefix_tree import PrefixTree
from combinations import Combinations

class Board_Screen():
    def __init__(self,players=False,setting=1,size=4):
        pygame.init()
        boggle_game = Game(size)
        boggle_game.print_solution()
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
        #"C:\\Users\\crmoo\\Documents\\GitHub\\Boggle\\build\\platformerGraphics_gui_text\\Individual\\Upper_A.png"
        #pygame.image.load(self.getLetterImage('a'))
        board_images = []
        i=0
        for x in boggle_game.game_board:
            for k in x:
                board_images.append(pygame.transform.scale(pygame.image.load(Board_Screen.getLetterImage(self,k)),(67,56)))
                i+=1
        
        background_color = (0, 76, 153)

        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption('Boggle!')
        pygame.display.flip()

        font = pygame.font.SysFont('Georgia', 40, bold = True)

        user_text = ''

        boggle_squares = []
        square_side_length = 150
        count = 0
        while(count<size*size):
            left = (count%4)*square_side_length+(2*screen_width/3)-(2*square_side_length)
            top = (count//4)*square_side_length+(screen_height/2)-(2*square_side_length)
            boggle_squares.append(pygame.Rect(left,top,square_side_length,square_side_length))
            count+=1
        
        correct_words = ''
        entry_box = pygame.Rect(0,screen_height*3/4,screen_width/3,screen_height/4)
        text_box = pygame.Rect(0,0,screen_width/3,screen_height*3/4)

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
                clock_text = font.render(str(timeLimit//60000)+":"+str((timeLimit//1000)%60),True,'White')
            screen.blit(clock_text,((screen_width*2/3)-40,30))

            pygame.draw.rect(screen,0,entry_box,2)
            pygame.draw.rect(screen,0,text_box,2)
            #pygame.draw.line(screen, 0, (screen_width/3,0), (screen_width/3,screen_height), 4)
            #pygame.draw.line(screen, 0, (0,(screen_height/4)*3), (screen_width/3,(screen_height/4)*3), 4)

            i=0
            for x in boggle_squares:
                pygame.draw.rect(screen, 0, x, 2)
                screen.blit(board_images[i],(x.x+40,x.y+40))
                i+=1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                #Got how to do text entry from https://www.geeksforgeeks.org/how-to-create-a-text-input-box-with-pygame/#
                if event.type == pygame.KEYDOWN:
                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:
                        # get text input from 0 to -1 i.e. end.
                        user_text = user_text[:-1]
                    elif event.key ==pygame.K_RETURN:
                        print(boggle_game.check_word(user_text.upper()))
                        if(boggle_game.check_word(user_text.upper())):
                            correct_words=correct_words+" "+user_text.upper()
                            user_text=""
                    # Unicode standard is used for string
                    # formation
                    else:
                        user_text += event.unicode
            entry_text = font.render(user_text, True, (255, 255, 255))
            words_text = font.render(correct_words, True, (255, 255, 255))
            # render at position stated in arguments
            screen.blit(words_text, (text_box.x+5, text_box.y+5))
            screen.blit(entry_text, (entry_box.x+5, entry_box.y+5))

            a, b = pygame.mouse.get_pos()
            pygame.display.update()
    
    def getLetterImage(self,cha):
        #pathToFile is just here so the files will display. I have no clue how to make the files display with specifying the whole filepath
        pathToFile="C:\\Users\\crmoo\\Documents\\GitHub\\Boggle\\build\\platformerGraphics_gui_text\\Individual\\"
        return pathToFile+"Upper_"+cha.upper()+".png"

            
#This is just here to open the screen when this program is called
Board_Screen(True,1)