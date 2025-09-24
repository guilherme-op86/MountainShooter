#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.const import ENTITY_SPEED, WIN_WIDTH, ENTITY_SHOT_DELAY
from code.enemyShot import EnemyShot
from code.entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self, ):
        # código que destrói a naa inimiga quando ela chega no final do lado esquerdo da tela
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        # mesma estratégia para controle da cadência de tiros do player1 e player2. O código doi simplesmente copiado
        # da classe player
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))