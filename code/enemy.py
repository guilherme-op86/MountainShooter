#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.const import ENTITY_SPEED, WIN_WIDTH
from code.entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        # código que destrói a naa inimiga quando ela chega no final do lado esquerdo da tela
        self.rect.centerx -= ENTITY_SPEED[self.name]