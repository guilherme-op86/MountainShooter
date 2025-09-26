from code import entity
from code.const import WIN_WIDTH
from code.enemy import Enemy
from code.enemyShot import EnemyShot
from code.entity import Entity
from code.player import Player
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
    def verify_colision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True
        # mesma coisa que: if valid_interaction == True
        # bloco de código que verifica as colisões para avaliar se houve ou não o dano
        if valid_interaction:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                # aplica o dano se houver colisões
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod
    # método que cria o sistema de score que soma pontos ao matar os inimigos
    def __giv_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'Player1Shot':
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.score += enemy.score
        elif enemy.last_dmg == 'Player2Shot':
            for ent in entity_list:
                if ent.name == 'Player2':
                    ent.score += enemy.score

    @staticmethod
    def verify_collision(entity_list: list[entity]):
        # verifica cada uma das entidades para ver se ela bateu na borda esquerda da tela. Se bater ela precisa
        # desaparecer
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            # laço que faz a comparação de colisão de todas as entidades. O i+ 1 impede comparações reduntantes
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.verify_colision_entity(entity1, entity2)

    @staticmethod
    # métdodo que destrói a entidade que chegar a 0 de vida
    def verify_health(entity_list: list[entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__giv_score(ent, entity_list)
                entity_list.remove(ent)
