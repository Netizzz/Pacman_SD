import pygame

class Movement():
    def __init__(self, rect, sq_size):
        self.rect = rect
        self.move = "left"
        self.sq_size = sq_size

    def get_move(self):
        return str(self.move)

    def set_rect(self, rect):
        self.rect = rect

    def key_input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.move = "left"
        if key[pygame.K_RIGHT]:
            self.move = "right"
        if key[pygame.K_UP]:
            self.move = "up"
        if key[pygame.K_DOWN]:
            self.move = "down"

    def update(self, game:object):
        last = self.rect.copy()
        if self.move == "left":
            self.rect.x -= 1 * self.sq_size
            print("l")
        if self.move == "right":
            self.rect.x += 1 * self.sq_size
            print("r")
        if self.move == "up":
            self.rect.y -= 1 * self.sq_size
            print("u")
        if self.move == "down":
            self.rect.y += 1 * self.sq_size
            print("d")

        new = self.rect
        for cell in pygame.sprite.spritecollide(self, game.walls, False):
            self.rect = last
            cell = cell.rect
            if last.right <= cell.left and new.right > cell.left:
                new.right = cell.left
            if last.left >= cell.right and new.left < cell.right:
                new.left = cell.right
            if last.bottom <= cell.top and new.bottom > cell.top:
                new.bottom = cell.top
            if last.top >= cell.bottom and new.top < cell.bottom:
                new.top = cell.bottom
        self.dirty = 1

    """def update(self, game:object):
        last = self.rect.copy()
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 1 * self.sq_size
        if key[pygame.K_RIGHT]:
            self.rect.x += 1 * self.sq_size
        if key[pygame.K_UP]:
            self.rect.y -= 1 * self.sq_size
        if key[pygame.K_DOWN]:
            self.rect.y +=  1 * self.sq_size
        new = self.rect
        for cell in pygame.sprite.spritecollide(self, game.walls, False):
            self.rect = last
            cell = cell.rect
            if last.right <= cell.left and new.right > cell.left:
                new.right = cell.left
            if last.left >= cell.right and new.left < cell.right:
                new.left = cell.right
            if last.bottom <= cell.top and new.bottom > cell.top:
                new.bottom = cell.top
            if last.top >= cell.bottom and new.top < cell.bottom:
                new.top = cell.bottom
        self.dirty = 1"""