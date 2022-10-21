import pygame, sys
import pygame_gui

from pygame.locals import *
from screeninfo import get_monitors # Получение разрешение экрана @eto-ban

import gameObject
'''
Получение разрешения экрана @eto-ban
'''
for screen_rev in get_monitors():
    print(screen_rev)
# close @eto-ban

class Game:
    def __init__(self, caption, width, height, frame_rate):
        self.frame_rate = frame_rate
        self.game_over = False
        self.objects = []
        self.width = width
        self.height = height
        self.ground = None
        self.groundRect = None
        self.running = True
        self.moving = False

        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(caption)
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

        self.ground = pygame.Surface(size=(self.width, self.height / 6))
        self.ground.fill((0, 200, 0))
        self.groundRect = self.ground.get_rect()

        self.objects.append(gameObject.Circle(self.screen, 100, 100))
        self.objects.append(gameObject.Rectangle(self.screen, 200, 200))

        manager = pygame_gui.UIManager((800, 600))

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()

            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    sys.exit()
                    
            elif event.type == MOUSEBUTTONDOWN:
                if self.objects[0].isIntersect(event):
                    self.moving = True
                    print('debug: isIntersect True(ok1)')

            elif event.type == MOUSEBUTTONUP:
                self.moving = False
                print('debug: isIntersect True(ok2)')

            elif event.type == MOUSEMOTION and self.moving == True:
                #self.objects[0].getObject().move_ip(event.rel)
                
                self.update(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                
                self.objects[0].move(event)
                
                print('debug: isIntersect True(ok3)')

    def update(self):
        for o in self.objects:
            o.update()

    def draw(self):
        self.screen.fill(color=(0, 191, 235))
        self.screen.blit(self.ground, (0, (self.height - (self.height / 6))))

        for o in self.objects:
            o.draw(self.screen, )

    def run(self):
        while not self.game_over:
            self.handleEvents()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)

game = Game("Physics Simulator", screen_rev.width, screen_rev.height, 60)
game.run()