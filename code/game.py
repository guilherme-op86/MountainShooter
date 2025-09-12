import pygame
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

            if menu_return == MENU_OPTION[0]:
                pass
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
            else:
                pass


