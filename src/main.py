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
        self.rectangle_draging = False
        self.mouse_x = 100
        self.mouse_y = 100
        self.offset_y = 0
        self.offset_x = 0

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


    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
                self.running = False

            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                     sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:            
                    # if gameObject.Rectangle.get_draw().collidepoint(event.pos):
                    if self.objects[1].isIntersect(event):
                        self.rectangle_draging = True
                        self.mouse_x, self.mouse_y = event.pos
                        self.offset_x = self.objects[1].x - self.mouse_x
                        self.offset_y = self.objects[1].y - self.mouse_y

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:            
                    self.rectangle_draging = False

            if event.type == pygame.MOUSEMOTION:
                if self.rectangle_draging:
                    self.mouse_x, self.mouse_y = event.pos
                    gameObject.Rectangle.getObject.x = self.mouse_x + self.offset_x
                    gameObject.Rectangle.getObject.y = self.mouse_y + self.offset_y
                        

    def update(self):
        for o in self.objects:
            o.update()

    def draw(self):
        self.screen.fill(color=(0, 191, 235))
        self.screen.blit(self.ground, (0, (self.height - (self.height / 6))))
        # self.screen.blit(self.ground, (gameObject.Rectangle.get_draw()))

        for o in self.objects:
            o.draw(self.screen, self.mouse_x, self.mouse_y)

    def run(self):
        while not self.game_over:
            self.handleEvents()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)

game = Game("Physics Simulator", 800, 600, 60)
# game = Game("Physics Simulator", screen_rev.width, screen_rev.height, 60)
game.run()