import pygame, sys
import pygame.mixer
import random

from src.component.button import Button
from src.component.game import Game
from src.util.constants import BACKGROUND_MENU, SCREEN, ICON, TITLE
from src.util.text import FONT_STYLE

pygame.init()

pygame.display.set_icon(ICON)
pygame.display.set_caption("The Adventurer's Journey")


def get_font(size): 
    return pygame.font.Font(FONT_STYLE, size)

def wrap_text(text, font, max_width):
    words = text.split(" ")
    lines = []
    current_line = ""

    for word in words:
        if font.size(current_line + " " + word)[0] <= max_width:
            current_line += " " + word
        else:
            lines.append(current_line.lstrip())
            current_line = word
    
    lines.append(current_line.lstrip())
    return lines

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        game = Game()
        game.execute()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BACKGROUND_MENU, (0, 0))
        

        OPTIONS_TEXT = "Na floresta mais perigosa do reino, um aventureiro destemido inicia uma jornada de coragem e determinação. Armado com sua poderosa espada, ele enfrenta uma infinidade de desafios mortais. A cada passo, ele se depara com slimes venenosos, morcegos mutantes e criaturas desconhecidas que habitam as sombras. A floresta é densa e imprevisível, cheia de armadilhas traiçoeiras e caminhos ocultos. Somente com sua habilidade e astúcia, ele conseguirá sobreviver a essa jornada épica e desafiadora. A cada vitória sobre os perigos da floresta, o aventureiro se aproxima cada vez mais de desvendar os segredos sombrios que assolam esse reino encantado, mas não se engane, quanto mais perto do coração da floresta, mais difícil será!"

        OPTIONS_LINES = wrap_text(OPTIONS_TEXT, get_font(13), 800)
        OPTIONS_Y = 80
        for line in OPTIONS_LINES:
            OPTIONS_LINE_TEXT = get_font(15).render(line, True, "White")
            OPTIONS_LINE_RECT = OPTIONS_LINE_TEXT.get_rect(center=(SCREEN.get_width() // 2, OPTIONS_Y))
            SCREEN.blit(OPTIONS_LINE_TEXT, OPTIONS_LINE_RECT)
            OPTIONS_Y += OPTIONS_LINE_TEXT.get_height() + 5

        OPTIONS_BACK = Button(image=None, pos=(463, 400), 
                            text_input="BACK", font=get_font(20), base_color="White", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BACKGROUND_MENU, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(35).render("THE ADVENTURER'S JOURNEY", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(463, 70))

        PLAY_BUTTON = Button(image=pygame.image.load("src/assets/Options Rect.png"), pos=(463, 150), 
                            text_input="PLAY", font=get_font(25), base_color="#d7fcd4", hovering_color="Green")
        OPTIONS_BUTTON = Button(image=pygame.image.load("src/assets/Options Rect.png"), pos=(463, 230), 
                                text_input="History", font=get_font(25), base_color="#d7fcd4", hovering_color="Green")
        QUIT_BUTTON = Button(image=pygame.image.load("src/assets/Options Rect.png"), pos=(463, 310), 
                            text_input="QUIT", font=get_font(25), base_color="#d7fcd4", hovering_color="Green")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
