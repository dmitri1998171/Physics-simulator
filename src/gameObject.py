class GameObject:
    def __init__(self, x, y, w, h, speed=(0, 0)):
        self.speed = speed
        self.density = 0 # Плотность
        self.mass = 0 # Масса
        self.friction = 0 # Трение
        self.air_resistance = 0 # сопортевление воздуха
        self.restitution = 0 # Упругость
        self.impulse = 0 # Импульс
        self.force = 0 # Сила


    def draw(self, screen):
        pass

    def move(self, dx, dy): 
        pass

    def update(self):
        if self.speed == [0, 0]:
            return

        self.move(self.speed)
    


