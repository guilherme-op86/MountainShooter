#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT
from code.entity import Entity


# herda os atributos da entidade
class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        # o método get_pressed() verifica se a tecla é pressionada de maneira constante
        pressed_key = pygame.key.get_pressed()
        # a posição 0,0 fica no canto superior esquerdo da tela, então o eixo y terá números negativos verificação com
        # and impede que a nave saia da tela. Ela continuará subindo enquanto a nave não chegar no topo
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            # o rect (retângulo) fo player 1 é que mexe a a imagem e o centery movimenta a posição no eixo y
            self.rect.centery -= ENTITY_SPEED[self.name]
            # movimenta a nave para baixo e a condição and faz com que a nave vá para baixo enquanto a movimentação
            # for menor que a altura da tela
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
            # movimenta a nave para a esquerda e a condição and estabelece o limite da tela que é a posição inicial
            # da nave no início do jogo (10p a partir da borda esqueda). O incremento é negativo porque decresce no
            # eixo x
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
            # movimenta a nave para a direita e a condição and estabelece o limite da tela que é o tamanho horizontal
            # o incremento aqui é positivo porque aumenta no eixo x
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
