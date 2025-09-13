#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.const import WIN_WIDTH, ENTITY_SPEED
from code.entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        pass

    def move(self, ):
        # cria o movimento parallax
        self.rect.centerx -= ENTITY_SPEED[self.name]
        # faz as imagens de fundo se movimentarem de forma contínua
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
