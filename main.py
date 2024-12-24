import pygame
import os
import sys

print('hello')
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Nigger')
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    running = True

    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image('arrow.png')
    sprite.rect = sprite.image.get_rect()
    all_sprites.add(sprite)
    pygame.mouse.set_visible(False)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_focused():
                    if (0 <= event.pos[0] <= width) and (0 <= event.pos[1] <= height):
                        sprite.rect.x = event.pos[0]
                        sprite.rect.y = event.pos[1]
                        all_sprites.draw(screen)
        all_sprites.draw(screen)
        pygame.display.flip()
        screen.fill((0, 0, 0))
    pygame.display.flip()