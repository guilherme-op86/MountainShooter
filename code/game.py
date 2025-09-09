import pygame
from code.menu import Menu


#!/usr/bin/python
# -*- coding: utf-8 -*-

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self, ):
        # laço que mantém a janela do jogo aberta
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
            # check for all events
            # for event in pygame.event.get():
            #    if event.type == pygame.QUIT:
            #        print('Quiting...')
            #        pygame.quit()  # close window
            #        quit()  # end game
