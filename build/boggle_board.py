import pygame
pygame.init()

screen_height = 800
screen_width = 1000

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
while(count<16):
    left = (count%4)*square_side_length+(2*screen_width/3)-(2*square_side_length)
    top = (count//4)*square_side_length+(screen_height/2)-(2*square_side_length)
    boggle_squares.append(pygame.Rect(left,top,square_side_length,square_side_length))
    count+=1

running = True
while running:
    screen.fill(background_color)
    screen_divider1 = pygame.draw.line(screen, 0, (screen_width/3,0), (screen_width/3,screen_height), 4)
    screen_divider2 = pygame.draw.line(screen, 0, (0,(screen_height/4)*3), (screen_width/3,(screen_height/4)*3), 4)
    for x in boggle_squares:
        pygame.draw.rect(screen, 0, x, 2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if quit_button.collidepoint(event.pos):
                pygame.quit()
    a, b = pygame.mouse.get_pos()
    pygame.display.update()