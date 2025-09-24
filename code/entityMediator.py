from code import entity
from code.const import WIN_WIDTH
from code.enemy import Enemy
from code.enemyShot import EnemyShot
from code.player_shot import PlayerShot


class EntityMediator:

    @staticmethod
    # o __ faz com que o método seja privado da classe
    # este método verfica se o inimigo atingiu o limite da tela a vida será definida em 0
    def __verify_collision_window(ent: entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0


    @staticmethod
    def verify_collision(entity_list: list[entity]):
        # verifica cada uma das entidades para ver se ela bateu na borda esquerda da tela. Se bater ela precisa desaparecer
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)

    @staticmethod
    # métdodo que destrói a entidade que chegar a 0 de vida
    def verify_health(entity_list: list[entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)


