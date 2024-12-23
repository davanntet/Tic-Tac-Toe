import sys
import time
import pygame
from ai_v1 import AI as AI_VERSION_1
from utilities import Utilities
from random import randint
class GameWindow:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tic Tac Toe")
        utilities = Utilities()
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
        self.slash_screen = "slash_screen"
        self.agent = None
        self.state = utilities.generate_board(3, 3)
        self.coordinates = {
            ((100,100+400),(105+(400 / 3) * 0,105+(400 / 3) * 1)):[
                ((100+(400 / 3) * 0, 100 + (400 / 3) * 1), (105+(400 / 3) * 0, 105 + (400 / 3) * 1)),
                ((100+(400 / 3) * 1, 100 + (400 / 3) * 2), (105+(400 / 3) * 0, 105 + (400 / 3) * 1)),
                ((100+(400 / 3) * 2, 100 + (400 / 3) * 3), (105+(400 / 3) * 0, 105 + (400 / 3) * 1))
            ],
            ((100,100+400),(105+(400 / 3) * 1,105+(400 / 3) * 2)):[
                ((100+(400 / 3) * 0, 100 + (400 / 3) * 1), (105+(400 / 3) * 1, 105 + (400 / 3) * 2)),
                ((100+(400 / 3) * 1, 100 + (400 / 3) * 2), (105+(400 / 3) * 1, 105 + (400 / 3) * 2)),
                ((100+(400 / 3) * 2, 100 + (400 / 3) * 3), (105+(400 / 3) * 1, 105 + (400 / 3) * 2))
            ],
            ((100,100+400),(105+(400 / 3) * 2,105+(400 / 3) * 3)):[
                ((100+(400 / 3) * 0, 100 + (400 / 3) * 1), (105+(400 / 3) * 2, 105 + (400 / 3) * 3)),
                ((100+(400 / 3) * 1, 100 + (400 / 3) * 2), (105+(400 / 3) * 2, 105 + (400 / 3) * 3)),
                ((100+(400 / 3) * 2, 100 + (400 / 3) * 3), (105+(400 / 3) * 2, 105 + (400 / 3) * 3))
            ],
        }
        self.AI_V1 = AI_VERSION_1(['X', 'O'])

    def generate_board(self,n_row, n_col):
        board = []
        for i in range(n_row):
            row = []
            for j in range(n_col):
                row.append(None)
            board.append(row)
        return board

    def find_position(self, x, y):
        row = None
        row_key = None
        for idx,key in enumerate(self.coordinates.keys()):
            if key[0][0] <= x <= key[0][1] and key[1][0] <= y <= key[1][1]:
                row = idx
                row_key = key
        if row is not None:
            for idx,key in enumerate(self.coordinates[row_key]):
                if key[0][0] <= x <= key[0][1] and key[1][0] <= y <= key[1][1]:
                    return row, idx
        return None, None
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
        self.slash_screen = "choose_player"

    def draw_choose_player(self):
        self.screen.fill((66, 66, 66))
        self.screen.blit(pygame.image.load("assets/img_3.png"), (0, 0), (0, 0, 800, 800), 0)
        # Title
        title_text = self.font_h4.render("Choose Player", True, (66, 66, 66))
        self.screen.blit(title_text, (self.screen.get_width() / 2 - title_text.get_width() / 2, 50))
        # Button X
        button_x_rect = pygame.Rect(self.screen.get_width() / 2 - 75-100, 150, 150, 50)
        pygame.draw.rect(self.screen, (255, 255, 255), button_x_rect)
        button_text = self.font_h3.render("X", True, (66, 66, 66))
        self.screen.blit(button_text, (self.screen.get_width() / 2 - button_text.get_width() / 2 - 100, 150))
        # Button O
        button_o_rect = pygame.Rect(self.screen.get_width() / 2 - 75+100, 150, 150, 50)
        pygame.draw.rect(self.screen, (255, 255, 255), button_o_rect)
        button_text = self.font_h3.render("O", True, (66, 66, 66))
        self.screen.blit(button_text, (self.screen.get_width() / 2 - button_text.get_width() / 2+100, 150))

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
        self.screen.blit(game_board, ((600 - 400) / 2, 105), (0, 0, 400, 400), 0)
        # Text: The winner is:
        title_text = self.font_h4.render("The winner is:", True, (66, 66, 66))
        self.screen.blit(title_text, (self.screen.get_width() / 2 - title_text.get_width() / 2, 50))
        pygame.display.update()
        if self.agent == 'O':
            self.agent = self.AI_V1.player(self.agent)
            col_rand = randint(0, 2)
            row_rand = randint(0, 2)
            text_1 = self.font_h3.render(self.agent, True, (66, 66, 66))
            self.screen.blit(text_1, (100 + 55 + 133 * col_rand, 105 + 45 + 133 * row_rand))
            pygame.display.update()
            self.state = self.AI_V1.result(self.state, (row_rand, col_rand))
            print(self.agent)
            self.agent = self.AI_V1.player(self.agent)
            print(self.agent)

        while self.slash_screen == "battle_game":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    x,y = mouse_pos
                    row, col = self.find_position(x, y)

                    if (row,col) in self.AI_V1.actions(self.state) and self.AI_V1.terminal(self.state)[0] is False:
                        text_1 = self.font_h3.render(self.agent, True, (66, 66, 66))
                        self.screen.blit(text_1, (100+55+133*col,105+45+133*row))
                        pygame.display.update()
                        self.state = self.AI_V1.result(self.state, (row, col))
                        terminate = self.AI_V1.terminal(self.state)
                        if terminate[0]:
                            title_text = None
                            if terminate[1] != 0:
                                title_text = self.font_h4.render(self.agent, True, (255, 0, 0))
                            else:
                                title_text = self.font_h4.render("None", True, (0, 255, 0))
                            self.screen.blit(title_text, (self.screen.get_width() / 2 + 100, 50))
                            pygame.display.update()
                        else:
                            self.agent = self.AI_V1.player(self.agent)
                            v,(row,col) = self.AI_V1.minimax_decision(self.state)
                            # if (row,col) in self.AI_V1.actions(self.state):
                            text_2 = self.font_h3.render(self.agent, True, (66, 66, 66))
                            self.screen.blit(text_2, (100 + 55 + 133 * col, 105 + 45 + 133 * row))
                            pygame.display.update()
                            self.state = self.AI_V1.result(self.state, (row, col))
                            terminate = self.AI_V1.terminal(self.state)
                            if terminate[0]:
                                title_text = None
                                if terminate[1] != 0:
                                    title_text = self.font_h4.render(self.agent, True, (0, 0, 255))
                                else:
                                    title_text = self.font_h4.render("None", True, (0, 255, 0))
                                self.screen.blit(title_text, (self.screen.get_width() / 2 + 100, 50))
                                pygame.display.update()
                            self.agent = self.AI_V1.player(self.agent)

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
                    if self.slash_screen == "slash_screen":
                        self.draw_slash_screen()
                    elif self.slash_screen == "choose_player":
                        if button_x_rect is None or button_o_rect is None:
                            button_x_rect, button_o_rect = self.draw_choose_player()
                        if button_x_rect.collidepoint(mouse_pos):
                            self.screen.fill((0, 0, 0))
                            self.agent = 'X'
                            self.slash_screen = "battle_game"
                        elif button_o_rect.collidepoint(mouse_pos):
                            self.screen.fill((0, 0, 0))
                            self.agent = 'O'
                            self.slash_screen = "battle_game"
                    elif self.slash_screen == "battle_game":
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_pos = event.pos
                            text_ = self.font_h3.render("X", True, (66, 66, 66))
                            self.screen.blit(text_, (mouse_pos[0], mouse_pos[1]))

            if self.slash_screen == "slash_screen":
                self.draw_slash_screen()

            if self.slash_screen == "choose_player":
                button_x_rect, button_o_rect = self.draw_choose_player()

            if self.slash_screen == "battle_game":
                self.battle_game()
            pygame.display.update()
            pygame.display.flip()

