import pygame
from pprint import pprint

from generate_board import generate_board
from main import *
from prefix_tree import PrefixTree
from combinations import Combinations

screen_height = 800
screen_width = 1000
background_color = (0, 76, 153)
pygame.init()

        
class Start_Screen():
    def __init__(self):
        self.CurrentState = False
        
        #creating Start Screen
        screen_start = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption('Boggle!')
        pygame.display.flip()

        #creating buttons and text
        font = pygame.font.SysFont('Georgia', 40, bold = True)
        title_font = pygame.font.SysFont('Georgia', 60, bold = True)

        title_text = title_font.render('Boggle!', True, 'white')
        title_rect = pygame.Rect(375, 100, 200, 60)

        quit_text = font.render('Quit', True, 'white')
        quit_button = pygame.Rect(650, 315, 200, 60)

        bckgrd_rec1 = pygame.Rect(145, 205, 210, 305)
        bckgrd_rec2 = pygame.Rect(645, 205, 210, 175)

        one_plyr_txt = font.render('1-Player', True, 'white')
        one_plyr_btn = pygame.Rect(150, 210, 200, 100)

        easy_btn_txt = font.render('Easy', True, 'white')
        easy_button = pygame.Rect(150, 315, 200, 60)

        med_btn_txt = font.render('Medium', True, 'white')
        med_button = pygame.Rect(150, 380, 200, 60)

        hard_btn_txt = font.render('Hard', True, 'white')
        hard_button = pygame.Rect(150, 445, 200, 60)

        two_plyr_txt = font.render('2-Player', True, 'white')
        two_plyr_btn = pygame. Rect(650, 210, 200, 100)

        hourglass_img = pygame.image.load('hourglass.png')
        fits_hrgls_img = pygame.transform.scale(hourglass_img, (100, 225))

        #Setting easy to True for default 
        easy = True
        medium = False
        hard = False

        #main Start_Screen loop
        running1 = True
        while running1:
            screen_start.fill(background_color)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running1 = False
                    pygame.quit()
                #Checks for button clicks
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if quit_button.collidepoint(event.pos):
                        pygame.quit()
                    if one_plyr_btn.collidepoint(event.pos):
                        if easy:
                            pygame.display.quit()
                            pygame.display.init()
                            Board_Screen(False, 1)
                        if medium:
                            pygame.display.quit()
                            pygame.display.init()
                            Board_Screen(False, 2)
                        if hard:
                            pygame.display.quit()
                            pygame.display.init()
                            Board_Screen(False, 3)
                        
                    if two_plyr_btn.collidepoint(event.pos):
                        pygame.display.quit()
                        pygame.display.init()
                        Board_Screen(True, 1)

                    #Checking to see if easy, medium, or hard has been pressed.
                    if easy_button.collidepoint(event.pos):
                        easy = True
                        medium = False
                        hard = False
                        print('Easy')
                    if med_button.collidepoint(event.pos):
                        easy = False
                        medium = True
                        hard = False
                        print('Medium')
                    if hard_button.collidepoint(event.pos):
                        easy = False
                        medium = False
                        hard = True
                        print('Hard')


            #drawing buttons and text  
            a, b = pygame.mouse.get_pos()
            pygame.draw.rect(screen_start, (0, 0, 0), bckgrd_rec1)
            pygame.draw.rect(screen_start, (0, 0, 0), bckgrd_rec2)
            screen_start.blit(fits_hrgls_img, (450, 250))
            if quit_button.x <= a <= quit_button.x + 200 and quit_button.y <= b <= quit_button.y + 60:
                pygame.draw.rect(screen_start, (180, 180, 180), quit_button)
            else:
                pygame.draw.rect(screen_start, (110, 110, 110), quit_button)
            screen_start.blit(quit_text, (quit_button.x + 5, quit_button.y + 5))

            if one_plyr_btn.x <= a <= one_plyr_btn.x + 200 and one_plyr_btn.y <= b <= one_plyr_btn.y + 100:
                pygame.draw.rect(screen_start, (180, 180, 180), one_plyr_btn)
            else:
                pygame.draw.rect(screen_start, (110, 110, 110), one_plyr_btn)
            screen_start.blit(one_plyr_txt, (one_plyr_btn.x + 5, one_plyr_btn.y + 5))

            if two_plyr_btn.x <= a <= two_plyr_btn.x + 200 and two_plyr_btn.y <= b <= two_plyr_btn.y + 100:
                pygame.draw.rect(screen_start, (180, 180, 180), two_plyr_btn)
            else:
                pygame.draw.rect(screen_start, (110, 110, 110), two_plyr_btn)
            screen_start.blit(two_plyr_txt, (two_plyr_btn.x + 5, two_plyr_btn.y + 5))

            if easy_button.x <= a <= easy_button.x + 200 and easy_button.y <= b <= easy_button.y + 60:
                pygame.draw.rect(screen_start, (180, 180, 180), easy_button)
            else:
                pygame.draw.rect(screen_start, (110, 110, 110), easy_button)
            screen_start.blit(easy_btn_txt, (easy_button.x + 5, easy_button.y + 5))

            if med_button.x <= a <= med_button.x + 200 and med_button.y <= b <= med_button.y + 60:
                pygame.draw.rect(screen_start, (180, 180, 180), med_button)
            else:
                pygame.draw.rect(screen_start, (110, 110, 110), med_button)
            screen_start.blit(med_btn_txt, (med_button.x + 5, med_button.y + 5))

            if hard_button.x <= a <= hard_button.x + 200 and hard_button.y <= b <= hard_button.y + 60:
                pygame.draw.rect(screen_start, (180, 180, 180), hard_button)
            else:
                pygame.draw.rect(screen_start, (110, 110, 110), hard_button)
            screen_start.blit(hard_btn_txt, (hard_button.x + 5, hard_button.y + 5))


            pygame.draw.rect(screen_start, (background_color), title_rect)
            screen_start.blit(title_text, (title_rect.x + 5, title_rect.y + 5))


            pygame.display.update()

    def screenUpdate(self):
        if self.CurrentState:
            self.screen.fill(self.fill)
    


class Board_Screen():
    def __init__(self, players=False, setting=1, size=4):
        self.CurrentState = False
        boggle_game = Game()
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
                
        #"C:\\Users\\crmoo\\Documents\\GitHub\\Boggle\\build\\platformerGraphics_gui_text\\Individual\\Upper_A.png"
        #pygame.image.load(self.getLetterImage('a'))
        #"C:\\Users\\zackl\\Documents\\GitHub\\Boggle\\build\\platformerGraphics_gui_text\\Individual\\"
        board_images = []
        i=0
        for x in boggle_game.game_board:
            for k in x:
                board_images.append(pygame.transform.scale(pygame.image.load(Board_Screen.getLetterImage(self,k)),(67,56)))
                i+=1
        
        background_color = (0, 76, 153)

        screen_boggle = pygame.display.set_mode((screen_width, screen_height))
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

        running2 = True
        clock = pygame.time.Clock()
        secondTimer = 1000
        timeLimit = 1000*60*3
        pygame.time.set_timer(pygame.QUIT,timeLimit,1)


        while running2:
            screen_boggle.fill(background_color)
            #Clock prints time since start every second
            clock.tick(60)
            timeLimit -= clock.get_time()
            secondTimer+=clock.get_time()
            if(secondTimer>1000):
                secondTimer-=1000
                clock_text = font.render(str(timeLimit//60000)+":"+str((timeLimit//1000)%60),True,'White')
            screen_boggle.blit(clock_text,((screen_width*2/3)-40,30))

            pygame.draw.rect(screen_boggle,0,entry_box,2)
            pygame.draw.rect(screen_boggle,0,text_box,2)
            #pygame.draw.line(screen, 0, (screen_width/3,0), (screen_width/3,screen_height), 4)
            #pygame.draw.line(screen, 0, (0,(screen_height/4)*3), (screen_width/3,(screen_height/4)*3), 4)

            i=0
            for x in boggle_squares:
                pygame.draw.rect(screen_boggle, 0, x, 2)
                screen_boggle.blit(board_images[i],(x.x+40,x.y+40))
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
            screen_boggle.blit(words_text, (text_box.x+5, text_box.y+5))
            screen_boggle.blit(entry_text, (entry_box.x+5, entry_box.y+5))

            a, b = pygame.mouse.get_pos()
            pygame.display.update()
    
    def getLetterImage(self,cha):
        #pathToFile is just here so the files will display. I have no clue how to make the files display with specifying the whole filepath
        pathToFile="platformerGraphics_gui_text\\Individual\\"
        return pathToFile+"Upper_"+cha.upper()+".png"

done = False
while not done:
    Start_Screen().screenUpdate()
    for events in pygame.events.get():
        if events.type == pygame.MOUSEBUTTONDOWN:
            if quit_button.collidepoint(events.pos):
                pygame.quit()


                        
#Start_Screen()
#Board_Screen(True,1)
