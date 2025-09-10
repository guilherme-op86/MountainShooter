#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        # define a imagem de fundo do menu
        self.surf = pygame.image.load('./assets/MenuBg.png')
        # cria o retângulo onde vai ser inserida a imagem (iniciando pelo topo esquerdo - regra geral)
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        # método que carrega o arquivo de música que irá tocar no menu (apenas carregar, não toca)
        pygame.mixer_music.load('./assets/Menu.mp3')
        # método que efetivamente faz a música tocar. O parâmetro loops, se for definido em -1, toca a música
        # indefinidamente
        pygame.mixer_music.play(-1)
        while True:
            # coloca a imagem dentro do retângulo. A ordem aqui é importante. Essa primeira instrução cria a imagem e
            # a instrução a seguir escreve o texto por cima desta imagem
            self.window.blit(source=self.surf, dest=self.rect)
            # instrução que determina os argumentos para a criação do texto (escreve o texto por cima da imagem
            self.menu_text(50, 'Mountain', COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            # a altura (eixo y) 120 deixa o texto mais baixo porque a posição inicial 00 começa no canto superior
            # direito
            self.menu_text(50, 'Shooter', COLOR_ORANGE, ((WIN_WIDTH / 2), 120))

            # laco do menu iterativo
            for i in range(len(MENU_OPTION)):
                # impressão do texto do menu iterativo importando as constantes MENU_OPTION e COLOR_WHITE. A
                # centralização na tela inicia com o primeiro texto em 200. Após cada iteração vai distanciando  + 30
                # * i. Sem essa distanciação o texto fica sobreposto
                self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()

            # faz a checagem de todos os eventos (vai corrigir o bug da janela que não fecha)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # fecha a janela
                    quit()  # ecerra o jogo

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
