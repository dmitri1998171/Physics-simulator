import pygame, sys
import pygame_gui

from math import pi
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

        # Buttons
        img = pygame.image.load('access/icons/1.png')
        self.manager = pygame_gui.UIManager((screen_rev.width, screen_rev.height))
        

        self.reset_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (70, 35)),
                                            text='reset',
                                            #normal_bg=img,
                                            manager=self.manager)
        self.settings_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((75, 0), (70, 35)),
                                            text='SETIN',
                                            manager=self.manager)
        self.help_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 0), (70, 35)),
                                            text='HELP',
                                            manager=self.manager)


    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()

            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    sys.exit()

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.reset_button:
                    print('reset')
            # pygame_gui
            self.manager.process_events(event)

    def update(self):
        for o in self.objects:
            o.update()
        # pygame_gui
        time_delta = self.clock.tick(60)/1000.0
        self.manager.update(time_delta)

    def draw(self):
        self.screen.fill(color=(0, 191, 235))
        self.screen.blit(self.ground, (0, (self.height - (self.height / 6))))
        
        for o in self.objects:
            o.draw(self.screen)
        # pygame_gui
        pygame.draw.rect(self.screen, (1,83,103), (0, 0, 500, 35))
        self.manager.draw_ui(self.screen)


    def run(self):
        while not self.game_over:
            self.handleEvents()
            self.update()
            self.draw()
            # pygame_gui
            pygame.display.update()
            self.clock.tick(self.frame_rate)

game = Game("Physics Simulator", screen_rev.width, screen_rev.height, 60)
game.run()