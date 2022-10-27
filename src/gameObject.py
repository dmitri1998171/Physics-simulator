import random, pygame, math, enum

from Box2D import (b2_staticBody, b2_dynamicBody)

class ModifyStates(enum.Enum):
    move = 1
    rotate = 2
    scale = 3

class GameObject:
    def __init__(self, screen, world, x, y, w, h):
        self.speed = 0          # Скорость
        self.density = 0        # Плотность
        self.mass = 0           # Масса
        self.friction = 0       # Трение
        self.air_resistance = 0 # сопортевление воздуха
        self.restitution = 0    # Упругость
        self.impulse = 0        # Импульс
        self.force = 0          # Сила

        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rotation = 0

        self.body = world.CreateDynamicBody(position=(self.x, self.y))

        self.IsPhysicOn = False
        self.screen = screen
        self.object = pygame.rect
        self.IsScaleing = False
        self.IsScaleingPressed = False
        self.canDragging = True # Для работы фиксатора
        self.color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))

    def draw(self):
        pass

    def move(self, dx, dy): 
        pass

    def update(self):
        if self.speed == [0, 0]:
            return

    def isIntersect(self, event):
        if (self.object.collidepoint(event.pos)):
            return True
        else:
            return False  
    
class Circle(GameObject):
    def __init__(self, screen, world, x, y):
        super().__init__(screen, world, x, y, 0, 0)

        self.radius = 50
        self.circle = self.body.CreateCircleFixture(radius=self.radius, density=1, friction=0.3)

    def draw(self, pos, vert):
        if self.IsPhysicOn == True:
            self.body.type = b2_dynamicBody
        else:
            self.body.type = b2_staticBody
        if(pos != []):
            self.x = float(pos[0])
            self.y = float(pos[1])

        self.object = pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

        if self.canDragging == False:
            pygame.draw.circle(self.screen, (0,0,0), (self.x, self.y), 24)
            pygame.draw.line(self.screen, (255,255,255), [self.x-10, self.y-10], [self.x+10, self.y+10], 3)
            pygame.draw.line(self.screen, (255,255,255), [self.x+10, self.y-10], [self.x-10, self.y+10], 3)
        if self.IsScaleing:
            if self.IsScaleingPressed:
                pygame.draw.line(self.screen, (255,255,255), [self.x + self.radius - 23 ,self.y + self.radius - 5], [self.x + self.radius - 5 ,self.y + self.radius - 5], 5)
                pygame.draw.line(self.screen, (255,255,255), [self.x + self.radius - 5, self.y + self.radius - 23], [self.x + self.radius - 5, self.y + self.radius - 5], 5)
            else:
                pygame.draw.line(self.screen, (255,255,255), [self.x + self.radius - 13 ,self.y + self.radius - 3], [self.x + self.radius - 3 ,self.y + self.radius - 3], 3)
                pygame.draw.line(self.screen, (255,255,255), [self.x + self.radius - 3, self.y + self.radius - 13], [self.x + self.radius - 3, self.y + self.radius - 3], 3)

        for fixture in self.body.fixtures:
            fixture.shape.draw(self.body, fixture)

class Rectangle(GameObject):
    def __init__(self, screen, world, x, y, w, h):
        super().__init__(screen, world, x, y, w, h)

        self.box = self.body.CreatePolygonFixture(box=(self.w, self.h), density=1, friction=0.3)

    def draw(self, pos, vert):
        if self.IsPhysicOn == True:
            self.body.type = b2_dynamicBody
        else:
            self.body.type = b2_staticBody
        
        if(vert != []):
            self.object = pygame.draw.polygon(self.screen, self.color, vert)

            # self.object = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.w, self.h))

        if self.canDragging == False:
            pygame.draw.circle(self.screen, (0,0,0), (self.x + self.w / 2, self.y + self.h / 2), 24)
            pygame.draw.line(self.screen, (255,255,255), [self.x + self.w / 2 -10, self.y + self.h / 2 -10], [self.x + self.h / 2 +10, self.y + self.h / 2 +10], 3)
            pygame.draw.line(self.screen, (255,255,255), [self.x + self.w / 2 +10, self.y + self.h / 2 -10], [self.x + self.h / 2 -10, self.y + self.h / 2 +10], 3)
            #self.scaleing = pygame.draw.line(self.screen, (255,255,255), [self.x + self.radius - 13 ,self.y + self.radius - 3], [self.x + self.radius - 3 ,self.y + self.radius - 3], 3)
        if self.IsScaleing:
            if self.IsScaleingPressed:
                pygame.draw.line(self.screen, (255,255,255), [self.x + self.w - 5, self.y + self.h - 23], [self.x + self.w - 5, self.y + self.h - 5], 5)
                pygame.draw.line(self.screen, (255,255,255), [self.x + self.w - 23 ,self.y + self.h - 5], [self.x + self.w - 5 ,self.y + self.h - 5], 5)
            else:
                pygame.draw.line(self.screen, (255,255,255), [self.x + self.w - 3, self.y + self.h - 13], [self.x + self.w - 3, self.y + self.h - 3], 3)
                pygame.draw.line(self.screen, (255,255,255), [self.x + self.w - 13 ,self.y + self.h - 3], [self.x + self.w - 3 ,self.y + self.h - 3], 3)
        for fixture in self.body.fixtures:
            fixture.shape.draw(self.body, fixture)
            
class Gear(GameObject):
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y, 0, 0)

    def draw(self, screen, screen_rev):
        inner_radius = 0
        outer_radius = 100
        tooth_depth = 15
        teeth = 36
        angle = 0

        r0 = inner_radius
        r1 = 100 - tooth_depth / 2.0 
        r2 = outer_radius + tooth_depth / 2.0
        da = 2.0 * math.pi / teeth / 4.0

        vertexes = []
        vertex = []

        for i in range(teeth):
            angle = i * 2.0 * math.pi / teeth

            vertex = (self.x + (r1 * math.cos(angle)), self.y + (r1 * math.sin(angle)))
            vertexes.append(vertex)
            vertex = (self.x + (r2 * math.cos(angle + da)), self.y + (r2 * math.sin(angle)))
            vertexes.append(vertex)
            vertex = (self.x + (r2 * math.cos(angle + (da * 2))), self.y + (r2 * math.sin(angle + (da * 2))))
            vertexes.append(vertex)
            vertex = (self.x + (r1 * math.cos(angle + (da * 3))), self.y + (r1 * math.sin(angle + (da * 3))))
            vertexes.append(vertex)

        self.object = pygame.draw.polygon(screen, self.color, vertexes)
        if self.canDragging == False:
            pygame.draw.circle(screen, (0,0,0), (self.x, self.y), 24)
            pygame.draw.line(screen, (255,255,255), [self.x-10, self.y-10], [self.x+10, self.y+10], 3)
            pygame.draw.line(screen, (255,255,255), [self.x+10, self.y-10], [self.x-10, self.y+10], 3)
        if self.IsScaleing == True:
            self.scaleing = pygame.draw.line(screen, (255,255,255), [self.x + outer_radius - 13 ,self.y + outer_radius - 3], [self.x + outer_radius - 3 ,self.y + outer_radius - 3], 3)
            pygame.draw.line(screen, (255,255,255), [self.x + outer_radius - 3, self.y + outer_radius - 13], [self.x + outer_radius - 3, self.y + outer_radius - 3], 3)
