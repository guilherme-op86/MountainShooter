import pygame

from code.level import Level
from code.menu import Menu
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION


#!/usr/bin/python
# -*- coding: utf-8 -*-

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):
        # laço que mantém a janela do jogo aberta
        while True:
            menu = Menu(self.window)
            # variável de retorno que captura o resultado da interação do jogador com o menu. Guarda qual o opção
            # o jogador escolheu ao pressionar a tecla enter
            menu_return = menu.run()

            # itera pelo menu. Como a fase inicialmente é a mesma, vai iterar por todas a opções para iniciar a fase
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0]  # Player1, Player2
                level = Level(self.window, 'Level1', menu_return, player_score)
                # começa a execução da fase
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    # começa a execução da fase
                    level_return = level.run(player_score)

            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
            else:
                pass
