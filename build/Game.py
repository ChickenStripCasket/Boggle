import pygame
from pprint import pprint

from random import Random
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
    def __init__(self, players=False, setting=1, size=4, boggle_game = Game(), second_turn = False):
        self.CurrentState = False
        boggle_game.print_solution()
        #AI and Two Players
        rand = Random()
        if(players):
            print("2P")
        else:
            ai_words = ""
            if(setting==1):
                print("1P E")
                ai_words_count=(rand.randint(5,15)*len(boggle_game.valid_combinations)//100)
                while ai_words_count>0:
                    possible_word = boggle_game.valid_combinations[rand.randint(0,len(boggle_game.valid_combinations)-1)]
                    if(not self.wordInString(ai_words,possible_word)):
                        ai_words+= " "+possible_word
                        ai_words_count-=1
                print(ai_words)
            if(setting==2):
                print("1P M")
                ai_words_count=(rand.randint(15,25)*len(boggle_game.valid_combinations)//100)
                while ai_words_count>0:
                    possible_word = boggle_game.valid_combinations[rand.randint(0,len(boggle_game.valid_combinations)-1)]
                    if(not self.wordInString(ai_words,possible_word)):
                        ai_words+= " "+possible_word
                        ai_words_count-=1
                print(ai_words)
            if(setting==3):
                print("1P H")
                ai_words_count=(rand.randint(25,45)*len(boggle_game.valid_combinations)//100)
                while ai_words_count>0:
                    possible_word = boggle_game.valid_combinations[rand.randint(0,len(boggle_game.valid_combinations)-1)]
                    if(not self.wordInString(ai_words,possible_word)):
                        ai_words+= " "+possible_word
                        ai_words_count-=1
                print(ai_words)
                
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

        font = pygame.font.SysFont('Georgia', 24, bold = True)

        user_text = ''
        score = 0

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
        SCREENEVENT = pygame.USEREVENT + 1
        
        clock = pygame.time.Clock()
        secondTimer = 1000
        timeLimit = 1000*60*3
        done = False
        pygame.time.set_timer(SCREENEVENT,timeLimit, 1)


        while running2:
            screen_boggle.fill(background_color)
            #Clock prints time since start every second
            clock.tick(60)
            timeLimit -= clock.get_time()
            secondTimer+=clock.get_time()
            if(secondTimer>1000 and timeLimit>=0):
                secondTimer-=1000
                clock_text = font.render(str(timeLimit//60000)+":"+str((timeLimit//1000)%60),True,'White')
            screen_boggle.blit(clock_text,((screen_width*2/3)-40,30))

            pygame.draw.rect(screen_boggle,0,entry_box,2)
            pygame.draw.rect(screen_boggle,0,text_box,2)

            i=0
            for x in boggle_squares:
                pygame.draw.rect(screen_boggle, 0, x, 2)
                screen_boggle.blit(board_images[i],(x.x+40,x.y+40))
                i+=1
            if timeLimit<0 and not done and not players:
                correct_words="You have a score of "+str(score)+" with the words: "+correct_words+". The computer has a score of "+str(len(ai_words.split()))+" with the words: "+ai_words
                done = True
            elif timeLimit<0 and not done and players:

                done = True
            for event in pygame.event.get():
                if pygame.event.get(SCREENEVENT) and not second_turn:
                    Intermin_Screen(boggle_game)
                    
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                #Got how to do text entry from https://www.geeksforgeeks.org/how-to-create-a-text-input-box-with-pygame/#
                if event.type == pygame.KEYDOWN:
                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:
                        # get text input from 0 to -1 i.e. end.
                        user_text = user_text[:-1]
                    elif event.key ==pygame.K_RETURN and timeLimit>0:
                        print(boggle_game.check_word(user_text.upper()))
                        if(boggle_game.check_word(user_text.upper()) and not self.wordInString(correct_words,user_text.upper())):
                            correct_words=correct_words+" "+user_text.upper()
                            if len(user_text) <=4:
                                score += 1
                            elif len(user_text) == 5:
                                score += 2
                            elif len(user_text) == 6:
                                score += 3
                            elif len(user_text) == 7:
                                score += 5
                            else:
                                score += 11
                            user_text=""
                    elif event.key == pygame.K_RETURN and timeLimit<0 and players and not second_turn:
                        Intermin_Screen(boggle_game)
                    # Unicode standard is used for string
                    # formation
                    else:
                        user_text += event.unicode
            # render at position stated in arguments
            self.drawText(screen_boggle,user_text,'White',entry_box,font)
            self.drawText(screen_boggle,correct_words,'White',text_box,font)

            a, b = pygame.mouse.get_pos()
            pygame.display.update()
    
    def getLetterImage(self,cha):
        #pathToFile is just here so the files will display. I have no clue how to make the files display with specifying the whole filepath
        pathToFile="platformerGraphics_gui_text\\Individual\\"
        return pathToFile+"Upper_"+cha.upper()+".png"

    def wordInString(self,checkString,word):
        stringArray = []
        stringArray = checkString.split()
        var = False
        for x in stringArray:
            if x == word:
                var = True
        return var
    
    #method taken from https://www.pygame.org/wiki/TextWrap
    def drawText(self, surface, text, color, rect, font, aa=False, bkg=None):
        rect = pygame.Rect(rect)
        y = rect.top
        lineSpacing = -2

        # get the height of the font
        fontHeight = font.size("Tg")[1]

        while text:
            i = 1

            # determine if the row of text will be outside our area
            if y + fontHeight > rect.bottom:
                break

            # determine maximum width of line
            while font.size(text[:i])[0] < rect.width and i < len(text):
                i += 1

            # if we've wrapped the text, then adjust the wrap to the last word      
            if i < len(text): 
                i = text.rfind(" ", 0, i) + 1

            # render the line and blit it to the surface
            if bkg:
                image = font.render(text[:i], 1, color, bkg)
                image.set_colorkey(bkg)
            else:
                image = font.render(text[:i], aa, color)

            surface.blit(image, (rect.left, y))
            y += fontHeight + lineSpacing

            # remove the text we just blitted
            text = text[i:]

        return text
    
class Intermin_Screen():
    def __init__(self,boggle_game):
        self.boggle_game = boggle_game
        pygame.display.quit()
        pygame.display.init()
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption('Player 2 prompt')
        pygame.display.flip()

        font = pygame.font.SysFont('Georgia', 50, bold = True)
        prompt_text1 = font.render('Player 2', True, 'white')
        prompt_text2 = font.render('Press Enter when ready', True, 'white')

        title_rec = pygame.Rect(375, 100, 200, 60)

        running3 = True
        while running3:
            screen.fill(background_color)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running3 = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.display.quit()
                        pygame.display.init()
                        Board_Screen(True, 1, 4, self.boggle_game, True)

            pygame.draw.rect(screen, (background_color), title_rec)
            screen.blit(prompt_text1, (title_rec.x + 5, title_rec.y + 5))
            screen.blit(prompt_text2, (title_rec.x - 175, title_rec.y + 50))
            
            pygame.display.update()
        


done = False
while not done:
    #Intermin_Screen()
    Start_Screen().screenUpdate()
    for events in pygame.events.get():
        if events.type == pygame.MOUSEBUTTONDOWN:
            if quit_button.collidepoint(events.pos):
                pygame.quit()


                        
#Start_Screen()
#Board_Screen(True,1)
