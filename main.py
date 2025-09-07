import pygame

# primeiro importa a biblioteca pygame e inicializa com pygame.init()

pygame.init()

# comando que cria uma janela para o jogo e define o seu tamanho
print('Setup Start')
window = pygame.display.set_mode(size=(600, 480))
print('Setup End')

# laço que mantém a janela do jogo aberta
print('Loop Start')
while True:
    # check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # close window
            quit()  # end game
