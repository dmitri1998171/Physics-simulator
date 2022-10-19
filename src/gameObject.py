class GameObject:
    def __init__(self, x, y, w, h, speed=(0, 0)):
        self.speed = speed

    def draw(self, screen):
        pass

    def move(self, dx, dy):
        pass

    def update(self):
        if self.speed == [0, 0]:
            return

        self.move(self.speed)
