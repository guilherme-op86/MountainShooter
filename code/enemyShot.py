from code.const import ENTITY_SPEED
from code.entity import Entity


class EnemyShot(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        # o tiro do inimigo bem da direita para a esquerda, diminuindo o valor de x
        self.rect.centerx -= ENTITY_SPEED[self.name]