import random, pygame

class GameObject:
    def __init__(self, screen, x, y):
        self.speed = 0          # Скорость
        self.density = 0        # Плотность
        self.mass = 0           # Масса
        self.friction = 0       # Трение
        self.air_resistance = 0 # сопортевление воздуха
        self.restitution = 0    # Упругость
        self.impulse = 0        # Импульс
        self.force = 0          # Сила

        update(x, y)
        self.rotation = []
        self.color_r = 0
        self.color_g = 0
        self.color_b = 0


    def randomizeColor(self):
        self.color_r = random.randint(0, 256)
        self.color_g = random.randint(0, 256)
        self.color_b = random.randint(0, 256)

    def draw(self, screen, x, y):
        update(x, y)

    def update(self, x, y):
        self.x = x
        self.y = y
        
        if self.speed == [0, 0]:
            return

        # self.move(self.speed)
    

class Circle(GameObject):
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)
        super().randomizeColor()
        super().update()
        
        self.radius = 50

    def draw(self, screen):
        super().update(self.x, self.y)
        
        screen.lock()
        self.circle = pygame.draw.circle(screen, (self.color_r, self.color_g, self.color_b), (self.x, self.y), self.radius)
        screen.unlock()
        
    @property
    def getObject(self):
        return self.circle
        
    def isIntersect(self, event):
        if (self.circle.collidepoint(event.pos)):
            print("debug: isIntersect True")
            return True
        else:
            print("debug: isIntersect False")
            return False      
                    
    def move(self, event):
        pygame.Rect.move_ip(self.circle, event.rel, 0)

class Rectangle(GameObject):
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)
        super().randomizeColor()
        
        self.x = x
        self.y = y
        self.w = 100
        self.h = 100

    def draw(self, screen):
        self.rectangle = pygame.draw.rect(screen, (self.color_r, self.color_g, self.color_b), (self.x, self.y, self.w, self.h))
