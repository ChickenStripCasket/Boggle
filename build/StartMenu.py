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

bckgrd_rec1 = pygame.Rect(150, 210, 200, 235)
bckgrd_rec2 = pygame.Rect(650, 210, 200, 235)

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

one_min_txt = font.render('1 min(s)', True, 'white')
one_min_btn = pygame.Rect(650, 315, 200, 60)

two_min_txt = font.render('2 min(s)', True, 'white')
two_min_btn = pygame.Rect(650, 380, 200, 60)

three_min_txt = font.render('3 min(s)', True, 'white')
three_min_btn = pygame.Rect(650, 445, 200, 60)

hourglass_img = pygame.image.load('hourglass.png')
fits_hrgls_img = pygame.transform.scale(hourglass_img, (100, 225))

running = True
while running:
    screen.fill(background_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if quit_button.collidepoint(event.pos):
                pygame.quit()
    a, b = pygame.mouse.get_pos()
    pygame.draw.rect(screen, (0, 0, 0), bckgrd_rec1)
    pygame.draw.rect(screen, (0, 0, 0), bckgrd_rec2)
    screen.blit(fits_hrgls_img, (450, 250))
    if quit_button.x <= a <= quit_button.x + 200 and quit_button.y <= b <= quit_button.y + 60:
        pygame.draw.rect(screen, (180, 180, 180), quit_button)
    else:
        pygame.draw.rect(screen, (110, 110, 110), quit_button)
    screen.blit(quit_text, (quit_button.x + 5, quit_button.y + 5))

    if easy_button.x <= a <= easy_button.x + 200 and easy_button.y <= b <= easy_button.y + 60:
        pygame.draw.rect(screen, (180, 180, 180), easy_button)
    else:
        pygame.draw.rect(screen, (110, 110, 110), easy_button)
    screen.blit(easy_btn_txt, (easy_button.x + 5, easy_button.y + 5))

    if med_button.x <= a <= med_button.x + 200 and med_button.y <= b <= med_button.y + 60:
        pygame.draw.rect(screen, (180, 180, 180), med_button)
    else:
        pygame.draw.rect(screen, (110, 110, 110), med_button)
    screen.blit(med_btn_txt, (med_button.x + 5, med_button.y + 5))

    if hard_button.x <= a <= hard_button.x + 200 and hard_button.y <= b <= hard_button.y + 60:
        pygame.draw.rect(screen, (180, 180, 180), hard_button)
    else:
        pygame.draw.rect(screen, (110, 110, 110), hard_button)
    screen.blit(hard_btn_txt, (hard_button.x + 5, hard_button.y + 5))

    if one_min_btn.x <= a <= one_min_btn.x + 200 and one_min_btn.y <= b <= one_min_btn.y + 60:
        pygame.draw.rect(screen, (180, 180, 180), one_min_btn)
    else:
        pygame.draw.rect(screen, (110, 110, 110), one_min_btn)
    screen.blit(one_min_txt, (one_min_btn.x + 5, one_min_btn.y + 5))

    if two_min_btn.x <= a <= two_min_btn.x + 200 and two_min_btn.y <= b <= two_min_btn.y + 60:
        pygame.draw.rect(screen, (180, 180, 180), two_min_btn)
    else:
        pygame.draw.rect(screen, (110, 110, 110), two_min_btn)
    screen.blit(two_min_txt, (two_min_btn.x + 5, two_min_btn.y + 5))

    if three_min_btn.x <= a <= three_min_btn.x + 200 and three_min_btn.y <= b <= three_min_btn.y + 60:
        pygame.draw.rect(screen, (180, 180, 180), three_min_btn)
    else:
        pygame.draw.rect(screen, (110, 110, 110), three_min_btn)
    screen.blit(three_min_txt, (three_min_btn.x + 5, three_min_btn.y + 5))

    pygame.draw.rect(screen, (background_color), title_rect)
    screen.blit(title_text, (title_rect.x + 5, title_rect.y + 5))
    pygame.draw.rect(screen, (110, 110, 110), one_plyr_btn)
    screen.blit(one_plyr_txt, (one_plyr_btn.x + 5, one_plyr_btn.y + 5))
    pygame.draw.rect(screen, (110, 110, 110), two_plyr_btn)
    screen.blit(two_plyr_txt, (two_plyr_btn.x + 5, two_plyr_btn.y + 5))
    
    pygame.display.update()        
