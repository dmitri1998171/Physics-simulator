import pygame, sys
import pygame_gui
import math

from pygame.locals import *
from screeninfo import get_monitors # Получение разрешение экрана @eto-ban

import gameObject

# Получение разрешения экрана @eto-ban
for screen_rev in get_monitors():
    print(screen_rev)

class Game:
    def __init__(self, caption, width, height, frame_rate):
        self.frame_rate = frame_rate
        self.game_over = False
        self.objects = []
        self.selectedObject = gameObject.GameObject(0, 0, 0)
        self.width = width
        self.height = height
        self.ground = None
        self.groundRect = None
        self.isDragging = False
        self.mouse_x = screen_rev.width / 2
        self.mouse_y = screen_rev.height / 2
        self.cursorObjectDelta = [0, 0]

        self.IsGridShow = False
        self.grid_step = 100
        self.grid_color = (255, 255, 0)
        self.grid_x = math.ceil(screen_rev.width / self.grid_step)
        self.grid_y = math.ceil(screen_rev.height / self.grid_step)

        self.grid_x = math.ceil(screen_rev.width / 100)
        self.grid_y = math.ceil(screen_rev.height / 100)
        print(f'x {self.grid_x}')
        print(f'y {self.grid_y}')

        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(caption)
        self.screen = pygame.display.set_mode((width, height), FULLSCREEN)
        self.clock = pygame.time.Clock()

        self.ground = pygame.Surface(size=(self.width, self.height / 6))
        self.ground.fill((0, 200, 0))
        self.groundRect = self.ground.get_rect()

        # pygame_gui buttons
        self.propertiesWindowsCount = 0
        self.isPropertiesClose = False

        self.manager = pygame_gui.UIManager((screen_rev.width, screen_rev.height), '../ext/theme.json')
        #self.manager_properties = pygame_gui.UIManager((screen_rev.width, screen_rev.height), '../ext/theme_properties.json')
        #self.manager_object_info = pygame_gui.UIManager((screen_rev.width, screen_rev.height), '../ext/theme_object.json')
        ###
        print('=============================')
        self.button_size_x_menu = 70
        self.button_size_y_menu = 35

        if 1024 >= screen_rev.width:
            print(f'IF 1000 > {screen_rev.width}')
            self.button_size_x_menu = 50
            self.button_size_y_menu = 25
            self.properties_size_x_button = 100
            self.properties_size_y_button = 30
            self.button_size_x_tools = 50
            self.button_size_y_tools = 50
            self.button_size_x_bottom_tool = 50
            self.button_size_y_bottom_tool = 50
            self.button_pos_x_tools = 0
            self.button_pos_y_tools = screen_rev.height/15
        elif 1366 >= screen_rev.width:
            print(f'IF 1366 > {screen_rev.width}')
            self.button_size_x_menu = 70
            self.button_size_y_menu = 35
            self.properties_size_x_button = 100
            self.properties_size_y_button = 30
            self.button_size_x_tools = 55
            self.button_size_y_tools = 55
            self.button_size_x_bottom_tool = 50
            self.button_size_y_bottom_tool = 50
            self.button_pos_x_tools = 0
            self.button_pos_y_tools = screen_rev.height/6
        elif 2560 >= screen_rev.width:
            print(f'IF 2560 > {screen_rev.width}')
            self.button_size_x_menu = 90
            self.button_size_y_menu = 45
            self.properties_size_x_button = 150
            self.properties_size_y_button = 40
            self.button_size_x_tools = 65
            self.button_size_y_tools = 65
            self.button_size_x_bottom_tool = 65
            self.button_size_y_bottom_tool = 65
            self.button_pos_x_tools = 0
            self.button_pos_y_tools = screen_rev.height/5
        elif 3840 >= screen_rev.width:
            print(f'IF 3840 > {screen_rev.width}')
            self.button_size_x_menu = 150
            self.button_size_y_menu = 75
            self.properties_size_x_button = 200
            self.properties_size_y_button = 50
            self.button_size_x_tools = 85
            self.button_size_y_tools = 85
            self.button_size_x_bottom_tool = 85
            self.button_size_y_bottom_tool = 85
            self.button_pos_x_tools = 0
            self.button_pos_y_tools = screen_rev.height/5  
        else:
            print(f'else > {screen_rev.width}')
            self.button_size_x_menu = 70
            self.button_size_y_menu = 35
            self.properties_size_x_button = 150
            self.properties_size_y_button = 40
            self.button_size_x_tools = 65
            self.button_size_y_tools = 65
            self.button_size_x_bottom_tool = 65
            self.button_size_y_bottom_tool = 65
            self.button_pos_x_tools = 0
            self.button_pos_y_tools = screen_rev.height/5

        print('=============================')
        
        self.menuButtons()
        
    def menuButtons(self):
        #menu buttons
        self.reset_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.button_size_x_menu * 0, 0), (self.button_size_x_menu, self.button_size_y_menu)),
                                            text='',
                                            tool_tip_text = 'Reset',
                                            object_id=f"#reset_button",
                                            manager=self.manager)
        self.settings_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.button_size_x_menu * 1, 0), (self.button_size_x_menu, self.button_size_y_menu)),
                                            text='',
                                            tool_tip_text = 'Settings',
                                            object_id=f"#settings_button",
                                            manager=self.manager)
        self.help_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.button_size_x_menu * 2, 0), (self.button_size_x_menu, self.button_size_y_menu)),
                                            text='',
                                            tool_tip_text = 'Help',
                                            object_id=f"#help_button",
                                            manager=self.manager)
        # simulation button
        self.arrow_left_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.button_size_x_menu * 3.5, 0), (self.button_size_x_menu, self.button_size_y_menu)),
                                            text='',
                                            tool_tip_text = 'Arrow left',
                                            object_id=f"#arrow_left_button",
                                            manager=self.manager)
        self.start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.button_size_x_menu * 4.5, 0), (self.button_size_x_menu, self.button_size_y_menu)),
                                            text='',
                                            tool_tip_text = 'Start',
                                            object_id=f"#start_button",
                                            manager=self.manager)
        self.arrow_right_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.button_size_x_menu * 5.5, 0), (self.button_size_x_menu, self.button_size_y_menu)),
                                            text='',
                                            tool_tip_text = 'Arrow right',
                                            object_id=f"#arrow_right_button",
                                            manager=self.manager)
        # Crete/delete buttons
        self.create_circle_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.button_pos_x_tools, self.button_pos_y_tools + self.button_size_y_tools * 6 ), (self.button_size_x_tools, self.button_size_y_tools)),
                                            text='',
                                            tool_tip_text = 'Create circle',
                                            object_id=f"#create_circle_button",
                                            manager=self.manager)
        self.create_rectangle_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.button_pos_x_tools, self.button_pos_y_tools + self.button_size_y_tools * 7 ), (self.button_size_x_tools, self.button_size_y_tools)),
                                            text='',
                                            tool_tip_text = 'Create rectangle',
                                            object_id=f"#create_rectangle_button",
                                            manager=self.manager)
        self.create_gear_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.button_pos_x_tools, self.button_pos_y_tools + self.button_size_y_tools * 8), (self.button_size_x_tools, self.button_size_y_tools)),
                                            text='',
                                            tool_tip_text = 'Create gear',
                                            object_id=f"#create_gear_button",
                                            manager=self.manager)
        '''
            ## ??? Create nail # гвозди или пин ???
        '''
        self.create_nail_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.button_pos_x_tools, self.button_pos_y_tools + self.button_size_y_tools * 9), (self.button_size_x_tools, self.button_size_y_tools)),
                                            text='',
                                            tool_tip_text = '## ??? Create nail',
                                            object_id=f"#create_nail_button",
                                            manager=self.manager)
        # Toolbar buttons
        self.toolbar_move_with_inert_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.button_pos_x_tools, self.button_pos_y_tools + self.button_size_y_tools * 1), (self.button_size_x_tools, self.button_size_y_tools)),
                                            text='',
                                            tool_tip_text = 'Ьove an object with inertia',
                                            object_id=f"#toolbar_move_with_inert_button",
                                            manager=self.manager)
        self.toolbar_move_without_inert_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.button_pos_x_tools, self.button_pos_y_tools + self.button_size_y_tools * 2), (self.button_size_x_tools, self.button_size_y_tools)),
                                            text='',
                                            tool_tip_text = 'Movement of an object without inertia',
                                            object_id=f"#toolbar_move_without_inert_button",
                                            manager=self.manager)
        self.toolbar_rotate_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.button_pos_x_tools, self.button_pos_y_tools + self.button_size_y_tools * 3), (self.button_size_x_tools, self.button_size_y_tools)),
                                            text='',
                                            tool_tip_text = 'Rotate object',
                                            object_id=f"#toolbar_rotate_button",
                                            manager=self.manager)
        self.toolbar_size_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.button_pos_x_tools, self.button_pos_y_tools + self.button_size_y_tools * 4), (self.button_size_x_tools, self.button_size_y_tools)),
                                            text='',
                                            tool_tip_text = 'Size object',
                                            object_id=f"#toolbar_size_button",
                                            manager=self.manager)
        # scale buttons
        self.scale_plus_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.button_size_x_bottom_tool * 2, screen_rev.height - self.button_size_y_bottom_tool), (self.button_size_x_bottom_tool, self.button_size_y_bottom_tool)),
                                            text='',
                                            tool_tip_text = 'Scale in',
                                            object_id=f"#scale_plus_button",
                                            manager=self.manager)
        self.scale_minus_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.button_size_x_bottom_tool * 3, screen_rev.height - self.button_size_y_bottom_tool), (self.button_size_x_bottom_tool, self.button_size_y_bottom_tool)),
                                            text='',
                                            tool_tip_text = 'Scale out',
                                            object_id=f"#scale_minus_button",
                                            manager=self.manager)
        # physics button
        '''
            ДОБАВИТЬ ОПИСАННИЕ К КНОПКАМ в tool_tip_text
        '''
        self.physics_gravity_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.button_size_x_bottom_tool * 6, screen_rev.height - self.button_size_y_bottom_tool), (self.button_size_x_bottom_tool, self.button_size_y_bottom_tool)),
                                            text='',
                                            tool_tip_text = 'gravity',
                                            object_id=f"#physics_gravity_button",
                                            manager=self.manager)
        self.physics_air_resistance_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.button_size_x_bottom_tool * 7, screen_rev.height - self.button_size_y_bottom_tool), (self.button_size_x_bottom_tool, self.button_size_y_bottom_tool)),
                                            text='',
                                            tool_tip_text = 'airr',
                                            object_id=f"#physics_air_resistance_button",
                                            manager=self.manager)
        self.physics_grid_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.button_size_x_bottom_tool * 8, screen_rev.height - self.button_size_y_bottom_tool), (self.button_size_x_bottom_tool, self.button_size_y_bottom_tool)),
                                            text='',
                                            tool_tip_text = 'grid',
                                            object_id=f"#physics_grid_button",
                                            manager=self.manager)
        # informations buttons
        self.information_object_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((screen_rev.width - self.button_size_x_bottom_tool, screen_rev.height / 6), (self.button_size_x_bottom_tool, self.button_size_y_bottom_tool)),
                                            text='',
                                            tool_tip_text = 'Object information',
                                            object_id=f"#information_object_button",
                                            manager=self.manager)
        self.information_edit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((screen_rev.width - self.button_size_x_bottom_tool, screen_rev.height / 6 + self.button_size_y_bottom_tool), (self.button_size_x_bottom_tool, self.button_size_y_bottom_tool)),
                                                text='',
                                                tool_tip_text = 'Object information edit',
                                                object_id=f"#information_edit_button",
                                                manager=self.manager)
        self.exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((screen_rev.width - self.button_size_x_bottom_tool,0), (self.button_size_x_bottom_tool, self.button_size_y_bottom_tool)),
                                                text='Q',
                                                tool_tip_text = 'Exit',
                                                object_id=f"#exit_button",
                                                manager=self.manager)

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.running = False
                sys.exit()

            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                     sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(self.objects)):            
                    if self.objects[i].isIntersect(event):
                        if event.button == 1:
                            self.selectedObject = self.objects[i]
                            self.isDragging = True
                            if(self.selectedObject.canDragging and self.isDragging):
                                self.mouse_x, self.mouse_y = event.pos
                                self.cursorObjectDelta[0] = self.selectedObject.x - self.mouse_x
                                self.cursorObjectDelta[1] = self.selectedObject.y - self.mouse_y   
                        # MENU RBM
                        if event.button == 3:
                            self.propertiesWindowsCount = self.propertiesWindowsCount + 1
                            if self.propertiesWindowsCount >= 2:
                                self.propertiesWindowsCount = self.propertiesWindowsCount - 1
                                self.properties.kill()
                                self.isPropertiesClose = False
                                print(f'self.propertiesWindowsCount  :{self.propertiesWindowsCount}\n self.isPropertiesClose = False')
                            if self.isPropertiesClose == False:
                                self.isPropertiesClose = True
                                self.selectedObject = self.objects[i]
                                self.properties = pygame_gui.elements.UIWindow(pygame.Rect(self.selectedObject.x,self.selectedObject.y ,self.properties_size_x_button ,self.properties_size_y_button * 3),
                                                        window_display_title = 'Properties',
                                                        visible=True,
                                                        object_id=f"#properties_menu",
                                                        manager=self.manager)
                                self.properties_delete_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0,0), (self.properties_size_x_button,self.properties_size_y_button)),
                                                    text='Delete',
                                                    container=self.properties,
                                                    tool_tip_text = 'Delete obj',
                                                    object_id=f"#properties_button",
                                                    manager=self.manager)
                                self.properties_fix_object_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0,self.properties_size_y_button * 1), (self.properties_size_x_button,self.properties_size_y_button)),
                                                    text='Fix object',
                                                    container=self.properties,
                                                    tool_tip_text = 'Fix object1',
                                                    object_id=f"#properties_button",
                                                    manager=self.manager)
                                self.properties_edit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0,self.properties_size_y_button * 2), (self.properties_size_x_button,self.properties_size_y_button)),
                                                    text='Info see',
                                                    container=self.properties,
                                                    tool_tip_text = 'OBJ Info see',
                                                    object_id=f"#properties_button",
                                                    manager=self.manager)
                                print('Debug: RMB menu is open')        
                        break

            '''
            Error:
            File "D:\WORKS\PS2\Physics-simulator\src\main.py", line 294, in handleEvents
                if event.ui_element == self.properties:
            AttributeError: 'Game' object has no attribute 'properties'

            !!!!!!!!! При нажатии на self.information_edit_window


            if event.type == pygame_gui.UI_WINDOW_CLOSE:
                if event.ui_element == self.properties:
                    self.propertiesWindowsCount = self.propertiesWindowsCount - 1
                    print("Manual Window closed 1")
                if event.ui_element == self.information_edit_window:
                    print("Manual Window closed 2")
                else:
                    pass
            '''
            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:            
                    self.isDragging = False
                    if self.isPropertiesClose == True:
                        self.properties.kill()
                        print("Window closed by isPropertiesClose == True to False!")
                        self.isPropertiesClose = False

            if event.type == pygame.MOUSEMOTION:
                if(self.selectedObject.canDragging and self.isDragging):
                    self.mouse_x, self.mouse_y = event.pos
                    self.selectedObject.x = self.mouse_x + self.cursorObjectDelta[0]
                    self.selectedObject.y = self.mouse_y + self.cursorObjectDelta[1]

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                self.UIHandleEvents(event)
            # pygame_gui event
            self.manager.process_events(event)
            #self.manager_properties.process_events(event)
            

    def UIHandleEvents(self, event):
        # menu button
        if event.ui_element == self.settings_button:
            self.settingst_window= pygame_gui.elements.UIWindow(pygame.Rect(screen_rev.width / 2 - 200, screen_rev.height / 2 - 150, 400 , 300),
                                                        window_display_title = 'Settings',
                                                        visible=True,
                                                        object_id=f"#settings_window",
                                                        manager=self.manager)
            print('settings_button pressed')
        if event.ui_element == self.reset_button:
            print('reset_button pressed')
        if event.ui_element == self.help_button:
            self.help_window= pygame_gui.elements.UIWindow(pygame.Rect(self.button_size_x_menu * 2, self.button_size_y_menu + 10, 400 , 300),
                                                        window_display_title = 'Help',
                                                        visible=True,
                                                        object_id=f"#help_window",
                                                        manager=self.manager)
            print('help_button pressed')
        # simulation button
        if event.ui_element == self.arrow_left_button:
            print('arrow_left_button pressed')
        if event.ui_element == self.start_button:
            print('start_button pressed')
        if event.ui_element == self.arrow_right_button:
            print('arrow_right_button pressed')
        # Crete/delete buttons
        if event.ui_element == self.create_circle_button:
            self.objects.append(gameObject.Circle(self.screen, screen_rev.width / 2, screen_rev.height / 2))
            print('create_circle_button pressed')
        if event.ui_element == self.create_rectangle_button:
            self.objects.append(gameObject.Rectangle(self.screen, screen_rev.width / 2, screen_rev.height / 2))
            print('create_rectangle_button pressed')
        if event.ui_element == self.create_gear_button:
            self.objects.append(gameObject.Gear(self.screen, screen_rev.width / 2, screen_rev.height / 2))
            print('create_gear_button pressed')
        if event.ui_element == self.create_nail_button:
            if(self.selectedObject.canDragging == False):
                self.selectedObject.canDragging = True
            else:
                self.selectedObject.canDragging = False   
            print('create_nail_button pressed')

        # Toolbar buttons
        if event.ui_element == self.toolbar_move_with_inert_button:
            print('toolbar_move_with_inert_button pressed')
        if event.ui_element == self.toolbar_move_without_inert_button:
            print('toolbar_move_without_inert_button pressed')
        if event.ui_element == self.toolbar_rotate_button:
            print('toolbar_rotate_button pressed')
        if event.ui_element == self.toolbar_size_button:
            print('toolbar_size_button pressed')
        # scale buttons
        if event.ui_element == self.scale_plus_button:
            print('scale_plus_button pressed')
        if event.ui_element == self.scale_minus_button:
            print('scale_minus_button pressed')
        # physics button
        if event.ui_element == self.physics_gravity_button:
            print('physics_gravity_button pressed')
        if event.ui_element == self.physics_air_resistance_button:
            print('physics_air_resistance_button pressed')
        if event.ui_element == self.physics_grid_button:
            if self.IsGridShow == True:
                self.IsGridShow = False
                print('self.IsGridShow = False')
            elif self.IsGridShow == False:
                self.IsGridShow = True
            print('self.IsGridShow = True')
        # informations buttons
        if event.ui_element == self.information_object_button:
            self.information_object_window= pygame_gui.elements.UIWindow(pygame.Rect(screen_rev.width - self.properties_size_x_button - 200,self.properties_size_y_button * 1 ,250 ,300),
                                                        window_display_title = 'information object',
                                                        visible=True,
                                                        object_id=f"#information_edit_window",
                                                        manager=self.manager)
            print('information_object_button pressed')
        if event.ui_element == self.information_edit_button:
            self.information_edit_window= pygame_gui.elements.UIWindow(pygame.Rect(screen_rev.width - self.properties_size_x_button - 200,self.properties_size_y_button * 9 ,250 ,300),
                                                        window_display_title = 'Properties edit',
                                                        visible=True,
                                                        object_id=f"#information_edit_window",
                                                        manager=self.manager)
            print('information_edit_button pressed')
        if event.ui_element == self.exit_button:
            pygame.kill() # Кривой выход
        #if event.ui_element == self.properties_delete_button:
        #    print('MENU properties_delete_button pressed')

    def update(self):
        for o in self.objects:
            o.update()    

    def draw(self):
        self.screen.fill(color=(0, 191, 235))
        self.screen.blit(self.ground, (0, (self.height - (self.height / 6))))
        # Draw rectangle with a borders
        def create_rect(surf, width, height, border, color, border_color):
            pygame.draw.rect(surf, color, (border, border, width, height), 0)
            #for i in range(1, border):
            #    pygame.draw.rect(surf, border_color, (border-i, border-i, width, height), 1)
        if self.IsGridShow == True:
            for i in range(self.grid_x): pygame.draw.aaline(self.screen, self.grid_color,[i * self.grid_step, 0], [i * self.grid_step, screen_rev.height])
            for i in range(self.grid_y): pygame.draw.aaline(self.screen, self.grid_color,[0, i * self.grid_step], [screen_rev.width, i * self.grid_step])

        create_rect(self.screen, self.button_size_x_menu * 6.5, self.button_size_y_menu, 2, (66, 204, 210), (0, 0, 0))

        for o in self.objects:
            o.draw(self.screen)
        
        self.manager.draw_ui(self.screen)
        #self.manager_properties.draw_ui(self.screen)

    def run(self):
        self.clock = self.clock.tick(60)/1000.0
        while not self.game_over:
            self.handleEvents()
            self.update()
            self.draw()

            self.manager.update(self.clock)
            #self.manager_properties.update(self.clock)
            pygame.display.update()
        self.clock.tick(self.frame_rate)
        


game = Game("Physics Simulator", screen_rev.width, screen_rev.height, 60)
game.run()