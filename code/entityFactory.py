#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.background import Background
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.enemy import Enemy
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                # cria uma lista vazia para adicionar as imagens na lista. Foi criado o match/case com 'LevelBg'
                # genérico para não se criar vários match/case.
                list_bg = []
                for i in range(7):
                    # cria 14 imagens. Depois que as 7 primeiras passarem, eslas são jogadas para o final da tela
                    # dando a impressão de constância do movimento
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                # corrigindo a posição de início. Player1 vai começar um pouco mais pra cima na tela (lembrar que a po
                # sição 0, 0 fica no canto superior esquerdo. Por isso é negativo para movimentar para cima)
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))
            case 'Player2':
                # corrigindo a posição player 2 vai começar um pouco mais pra baixo
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
            # cria os inimigos inciando-os fora do tela
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
