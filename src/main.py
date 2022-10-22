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

        # pygame_gui buttons
        self.manager = pygame_gui.UIManager((screen_rev.width, screen_rev.height))
        #menu buttons
        self.reset_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (70, 35)),
                                             text='Reset',
                                             manager=self.manager)
        self.settings_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((75, 0), (70, 35)),
                                             text='Settings',
                                             manager=self.manager)
        self.help_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((145, 0), (70, 35)),
                                             text='Help',
                                             manager=self.manager)
        # simulation button
        self.arrow_left_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 0), (70, 35)),
                                             text='Arr LEFT',
                                             manager=self.manager)
        self.start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((375, 0), (70, 35)),
                                             text='START',
                                             manager=self.manager)
        self.arrow_right_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((455, 0), (70, 35)),
                                             text='Aee RIGHT',
                                             manager=self.manager)
        # Crete/delete buttons
        self.create_circle_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 600), (80, 80)),
                                             text='circle',
                                             manager=self.manager)
        self.create_rectangle_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 700), (80, 80)),
                                             text='rectangle',
                                             manager=self.manager)
        self.create_gear_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 800), (80, 80)),
                                             text='gear',
                                             manager=self.manager)
        self.create_nail_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 900), (80, 80)),
                                             text='Nail',
                                             manager=self.manager)
        # Toolbar buttons
        self.toolbar_move_with_inert_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 100), (200, 80)),
                                             text='move_with_inert',
                                             manager=self.manager)
        self.toolbar_move_without_inert_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 200), (200, 80)),
                                             text='move_without_inert',
                                             manager=self.manager)
        self.toolbar_rotate_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 300), (80, 80)),
                                             text='rotare',
                                             manager=self.manager)
        self.toolbar_size_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 400), (80, 80)),
                                             text='size',
                                             manager=self.manager)
        # scale buttons
        self.scale_plus_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 980), (100, 70)),
                                             text='Scale +',
                                             manager=self.manager)
        self.scale_minus_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 980), (100, 70)),
                                             text='Scale -',
                                             manager=self.manager)
        # physics button
        self.physics_gravity_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((400, 980), (100, 70)),
                                             text='Gravity',
                                             manager=self.manager)
        self.physics_air_resistance_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500, 980), (100, 70)),
                                             text='Air resistance',
                                             manager=self.manager)
        self.physics_grid_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((600, 980), (100, 70)),
                                             text='Grid',
                                             manager=self.manager)
        # informations buttons
        self.information_object_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1000, 200), (100, 70)),
                                             text='obj INFO',
                                             manager=self.manager)
        self.information_edit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1000, 300), (200, 70)),
                                             text='obj INGO Edit',
                                             manager=self.manager)

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
                        

            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                # menu button
                if event.ui_element == self.settings_button:
                    print('settings_button pressed')
                elif event.ui_element == self.reset_button:
                    print('reset_button pressed')
                elif event.ui_element == self.help_button:
                    print('help_button pressed')
                # simulation button
                elif event.ui_element == self.arrow_left_button:
                    print('arrow_left_button pressed')
                elif event.ui_element == self.start_button:
                    print('start_button pressed')
                elif event.ui_element == self.arrow_right_button:
                    print('arrow_right_button pressed')
                # Crete/delete buttons
                elif event.ui_element == self.create_circle_button:
                    print('create_circle_button pressed')
                elif event.ui_element == self.create_rectangle_button:
                    print('create_rectangle_button pressed')
                elif event.ui_element == self.create_gear_button:
                    print('create_gear_button pressed')
                elif event.ui_element == self.create_nail_button:
                    print('create_nail_button pressed')
                # Toolbar buttons
                elif event.ui_element == self.toolbar_move_with_inert_button:
                    print('toolbar_move_with_inert_button pressed')
                elif event.ui_element == self.toolbar_move_without_inert_button:
                    print('toolbar_move_without_inert_button pressed')
                elif event.ui_element == self.toolbar_rotate_button:
                    print('toolbar_rotate_button pressed')
                elif event.ui_element == self.toolbar_size_button:
                    print('toolbar_size_button pressed')
                # scale buttons
                elif event.ui_element == self.scale_plus_button:
                    print('scale_plus_button pressed')
                elif event.ui_element == self.scale_minus_button:
                    print('scale_minus_button pressed')
                # physics button
                elif event.ui_element == self.physics_gravity_button:
                    print('physics_gravity_button pressed')
                elif event.ui_element == self.physics_air_resistance_button:
                    print('physics_air_resistance_button pressed')
                elif event.ui_element == self.physics_grid_button:
                    print('physics_grid_button pressed')
                # informations buttons
                elif event.ui_element == self.information_object_button:
                    print('information_object_button pressed')
                elif event.ui_element == self.information_edit_button:
                    print('information_edit_button pressed')


            self.manager.process_events(event)

    def update(self):
        for o in self.objects:
            o.update()
        
            

    def draw(self):
        self.screen.fill(color=(0, 191, 235))
        self.screen.blit(self.ground, (0, (self.height - (self.height / 6))))
        pygame.draw.rect(self.screen, (66, 204, 210), (0, 0, 500, 35))
        pygame.draw.rect(self.screen, (0, 0, 0, 100), (0, 35, 500, 2))

        for o in self.objects:
            o.draw(self.screen)
        
        self.manager.draw_ui(self.screen)


    def run(self):
        self.clock = self.clock.tick(60)/1000.0
        while not self.game_over:
            self.handleEvents()
            self.update()
            self.draw()

            self.manager.update(self.clock)
            pygame.display.update()
        self.clock.tick(self.frame_rate)

game = Game("Physics Simulator", 800, 600, 60)
# game = Game("Physics Simulator", screen_rev.width, screen_rev.height, 60)
game.run()