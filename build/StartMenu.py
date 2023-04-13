import pygame
pygame.init()

screen_height = 800
screen_width = 1000

background_color = (0, 76, 153)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Boggle!')
pygame.display.flip()

font = pygame.font.SysFont('Georgia', 40, bold = True)

quit_text = font.render('Quit', True, 'white')
quit_button = pygame.Rect(200, 400, 200, 60)

one_plyr_txt = font.render('1-Player', True, 'white')
one_plyr_btn = pygame.Rect(200, 325, 200, 60)

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
    if quit_button.x <= a <= quit_button.x + 200 and quit_button.y <= b <= quit_button.y + 60:
        pygame.draw.rect(screen, (180, 180, 180), quit_button)
    else:
        pygame.draw.rect(screen, (110, 110, 110), quit_button)
    screen.blit(quit_text, (quit_button.x + 5, quit_button.y + 5))

    if one_plyr_btn.x <= a <= one_plyr_btn.x + 200 and one_plyr_btn.y <= b <= one_plyr_btn.y + 60:
        pygame.draw.rect(screen, (180, 180, 180), one_plyr_btn)
    else:
        pygame.draw.rect(screen, (110, 110, 110), one_plyr_btn)
    screen.blit(one_plyr_txt, (one_plyr_btn.x + 5, one_plyr_btn.y + 5))
    
    pygame.display.update()        
