#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.background import Background
from code.const import WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                # cria uma lista vazia para adicionar as imagens na lista. Foi criado o match/case com 'LevelBg'
                # genérico para não se criar vários match/case.
                list_bg=[]
                for i in range(7):
                    # cria 14 imagens. Depois que as 7 primeiras passarem, eslas são jogadas para o final da tela
                    # dando a impressão de constância do movimento
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg


