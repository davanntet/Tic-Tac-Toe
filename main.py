import sys
import time
import pygame

class GameWindow:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tic Tac Toe")
        self.width = 600
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.font_h1 = pygame.font.Font("assets/Roboto-Bold.ttf", 60)
        self.font_h2 = pygame.font.Font("assets/Roboto-Bold.ttf", 50)
        self.font_h3 = pygame.font.Font("assets/Roboto-Bold.ttf", 40)
        self.font_h4 = pygame.font.Font("assets/Roboto-Bold.ttf", 30)
        self.font_h5 = pygame.font.Font("assets/Roboto-Bold.ttf", 20)
        self.font_h6 = pygame.font.Font("assets/Roboto-Bold.ttf", 10)
        self.state = "slash_screen"
        self.choice = None

    def draw_slash_screen(self):
        self.screen.fill((128, 170, 156))
        self.screen.blit(pygame.image.load("assets/img.png"),
                         (self.screen.get_width() / 2 - 342 / 2, self.screen.get_height() / 2 - 336 / 2),
                         (0, 0, 800, 600), 0)
        title_text = self.font_h1.render("Tic Tac Toe", True, (66, 66, 66))
        self.screen.blit(title_text, (self.screen.get_width() / 2 + 342 / 2 - title_text.get_width() - 25, 50))
        title_text = self.font_h5.render("Version 1.0.0", True, (66, 66, 66))
        self.screen.blit(title_text, (
        self.screen.get_width() / 2 + 342 / 2 - title_text.get_width() - title_text.get_width(),
        self.screen.get_height() - 50))
        pygame.display.update()
        time.sleep(2.5)
        self.state = "choose_player"

    def draw_choose_player(self):
        self.screen.fill((66, 66, 66))
        self.screen.blit(pygame.image.load("assets/img_3.png"), (0, 0), (0, 0, 800, 800), 0)
        # Title
        title_text = self.font_h4.render("Choose Player", True, (66, 66, 66))
        self.screen.blit(title_text, (self.screen.get_width() / 2 - title_text.get_width() / 2, 50))
        # Button X
        button_x_rect = pygame.Rect(self.screen.get_width() / 2 - 75, 150, 150, 50)
        pygame.draw.rect(self.screen, (255, 255, 255), button_x_rect)
        button_text = self.font_h3.render("X", True, (66, 66, 66))
        self.screen.blit(button_text, (self.screen.get_width() / 2 - button_text.get_width() / 2, 150))
        # Button O
        button_o_rect = pygame.Rect(self.screen.get_width() / 2 - 75, 300, 150, 50)
        pygame.draw.rect(self.screen, (255, 255, 255), button_o_rect)
        button_text = self.font_h3.render("O", True, (66, 66, 66))
        self.screen.blit(button_text, (self.screen.get_width() / 2 - button_text.get_width() / 2, 300))

        # fun text "Good Luck!"
        title_text = self.font_h5.render("Good Luck!", True, (66, 66, 66))
        self.screen.blit(title_text, (self.screen.get_width() / 2 - title_text.get_width() / 2, self.screen.get_height() - 50))
        pygame.display.update()
        return button_x_rect, button_o_rect

    def battle_game(self):
        # Draw Tic Tac Toe Game
        self.screen.fill((66, 66, 66))
        background = pygame.image.load("assets/img_4.png")
        self.screen.blit(background, (0, 0), (0, 0, 800, 800), 0)
        game_board = pygame.image.load("assets/game_board.png")
        self.screen.blit(game_board, ((600 - 400) / 2, 150), (0, 0, 400, 400), 0)
        # Text: The winner is:
        title_text = self.font_h4.render("The winner is:", True, (66, 66, 66))
        self.screen.blit(title_text, (self.screen.get_width() / 2 - title_text.get_width() / 2, 50))

        pygame.display.update()

    def draw_game(self):
        pass

    def draw_game_over(self):
        pass

    def start(self):
        button_x_rect = None
        button_o_rect = None
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if self.state == "slash_screen":
                        self.draw_slash_screen()
                    elif self.state == "choose_player":
                        if button_x_rect is None or button_o_rect is None:
                            button_x_rect, button_o_rect = self.draw_choose_player()
                        if button_x_rect.collidepoint(mouse_pos):
                            self.screen.fill((0, 0, 0))
                            self.choice = 'X'
                            self.state = "battle_game"
                        elif button_o_rect.collidepoint(mouse_pos):
                            self.screen.fill((0, 0, 0))
                            self.choice = 'O'
                            self.state = "battle_game"

            if self.state == "slash_screen":
                self.draw_slash_screen()

            if self.state == "choose_player":
                button_x_rect, button_o_rect = self.draw_choose_player()

            if self.state == "battle_game":
                self.battle_game()

            pygame.display.update()
            pygame.display.flip()

game = GameWindow()
game.start()