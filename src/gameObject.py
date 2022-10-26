import random, pygame, math, pygame_gui
import enum

class ModifyStates(enum.Enum):
    move = 1
    rotate = 2
    scale = 3


class GameObject:
    def __init__(self, screen, x, y, w, h):
        self.speed = 0          # Скорость
        self.density = 0        # Плотность
        self.mass = 0           # Масса
        self.friction = 0       # Трение
        self.air_resistance = 0 # сопортевление воздуха
        self.restitution = 0    # Упругость
        self.impulse = 0        # Импульс
        self.force = 0          # Сила

        self.h = h
        self.w = w

        self.x = x
        self.y = y
        self.rotation = []

        self.object = pygame.rect
        self.scaleing = pygame.rect
        self.canDragging = True # Для работы фиксатора
        self.color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))

    def draw(self, screen):
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
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y, 0, 0)

        self.radius = 50

    def draw(self, screen):
        self.object = pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        if self.canDragging == False:
            pygame.draw.circle(screen, (0,0,0), (self.x, self.y), 24)
            pygame.draw.line(screen, (255,255,255), [self.x-10, self.y-10], [self.x+10, self.y+10], 3)
            pygame.draw.line(screen, (255,255,255), [self.x+10, self.y-10], [self.x-10, self.y+10], 3)
        if self.modifyState == ModifyStates.scale:
            self.scaleing = pygame.draw.line(screen, (255,255,255), [self.x + self.radius - 13 ,self.y + self.radius - 3], [self.x + self.radius - 3 ,self.y + self.radius - 3], 3)
            pygame.draw.line(screen, (255,255,255), [self.x + self.radius - 3, self.y + self.radius - 13], [self.x + self.radius - 3, self.y + self.radius - 3], 3)

class Rectangle(GameObject):
    def __init__(self, screen, x, y, w, h):
        super().__init__(screen, x, y, w, h)


    def draw(self, screen):
        self.object = pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))  



class Gear(GameObject):
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y, 0, 0)

    def draw(self, screen):
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
