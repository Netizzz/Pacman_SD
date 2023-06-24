import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self,pos_x:int, pos_y:int, w_size:int, name:str, *groups ):
        super().__init__(*groups)
        self.image = pygame.image.load("./images/" + str(name) + ".png")
        initial_size = self.image.get_size()
        size_rate = w_size / initial_size[0]
        self.new_size = (int(self.image.get_size()[0] * size_rate), int(self.image.get_size()[1] * size_rate))
        self.image = pygame.transform.scale(self.image, self.new_size)
        self.rect = pygame.rect.Rect((pos_x * w_size, pos_y * w_size), self.image.get_size())
        self.pos = [pos_x, pos_y]


    def get_size(self):
        self.dirty = 1
        return self.new_size


    def update(self):
        self.dirty = 1

    def get_pos(self):
        return self.pos