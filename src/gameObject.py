import random, pygame, math
import Box2D 
from Box2D.b2 import (world, polygonShape, circleShape, staticBody, dynamicBody)
from screeninfo import get_monitors # Получение разрешение экрана @eto-ban

for screen_rev in get_monitors():
    print(screen_rev)

class GameObject:
    def __init__(self, screen, world, x, y):
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
        self.rotation = []

        self.object = pygame.rect
        self.canDragging = True # Для работы фиксатора
        self.color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))

    def draw(self, screen, screen_rev):
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
        super().__init__(screen, world, x, y)

        self.world = world
        self.radius = 50
        self.body = world.CreateDynamicBody(position=(self.x, self.y))
        self.circle = self.body.CreateCircleFixture(radius=self.radius, density=1, friction=0.3)

    def my_draw_circle(self, circle, body, screen):
            position = body.transform * self.world.bodies[0].position
            position = (position[0], screen_rev.height - position[1])
            pygame.draw.circle(self.screen, (255, 255, 255), (position[0], position[1]), int(circle.radius))


    def draw(self, screen, screen_rev):
        # circleShape.draw = self.my_draw_circle(self.circle, self.body, screen)
        # position = self.body.transform * self.body.position
        # position = (position[0], screen_rev.height - position[1])
        # pygame.draw.circle(screen, (255, 255, 255), (position[0], position[1]), int(self.radius))

        # for body in self.world.bodies:
        #     for fixture in self.body.fixtures:
        #         fixture.shape.draw(self.body, fixture)
        # self.body.fixtures[0].shape.draw(self.body, self.body.fixtures[0])

        for fixture in self.body.fixtures:
                fixture.shape.draw(self.body, fixture)

class Rectangle(GameObject):
    def __init__(self, screen, world, x, y):
        super().__init__(screen, world, x, y)

        self.w = 100
        self.h = 100
        self.world = world
        self.body = world.CreateDynamicBody(position=(300, 300))
        self.box = self.body.CreatePolygonFixture(box=(50, 50), density=1, friction=0.3)

    def draw(self, screen, screen_rev):
        # self.object = pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))     
        for fixture in self.body.fixtures:
            fixture.shape.draw(self.body, fixture)

class Gear(GameObject):
    def __init__(self, screen, world, x, y):
        super().__init__(screen, world, x, y)

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

