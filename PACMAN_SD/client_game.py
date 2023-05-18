import pygame
import player_client, obstacles_client, client_stub
from map import walls, dots, portals, air
import game_mech


class GameUI(object):
    def __init__(self,stub: client_stub.StubClient, grid_size):
        self.stub = stub
        dim = stub.dimensions_size()
        self.x_max = dim[0]
        self.y_max = dim[1]
        self.width, self.height = self.x_max * grid_size, self.y_max * grid_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pacman")
        self.clock = pygame.time.Clock()
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.grid_size = 30
        grid_colour = self.black
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill(self.black)
        self.screen.blit(self.background,(0,0))
        pygame.display.update()

    def create_players(self,size:int) -> None:
        self.pl = self.stub.get_players()
        self.players = pygame.sprite.Group()
        self.players = pygame.sprite.LayeredDirty()
        # self, number, name, pos_x, pos_y, sq_size, groups
        self.playerA = player_client.Player(1, "pacman", 9, 16, size, self.players)
        self.playerB = player_client.Player(2, "ghost", 9, 10, size, self.players)

        self.players.add(self.playerA)
        self.players.add(self.playerB)


    def read_map(self, map_file):
        with open(str(map_file)) as data:
            mapa = data.read()
            mapa = mapa.split("\n")
            for i in range(len(mapa)):
                mapa[i] = mapa[i].split(",")
            return mapa

    def create_map(self, size:int):
        self.wl = self.stub.get_obstacles()
        self.obstacles = pygame.sprite.Group()
        for i in walls:
            obs = obstacles_client.Obstacle(i[0], i[1], size, "wall")
            self.obstacles.add(obs)
        for i in dots:
            obs = obstacles_client.Obstacle(i[0], i[1], size, "dot")
            self.obstacles.add(obs)
        for i in portals:
            obs = obstacles_client.Obstacle(i[0], i[1], size, "portal")
            self.obstacles.add(obs)
        for i in air:
            obs = obstacles_client.Obstacle(i[0], i[1], size, "air")
            self.obstacles.add(obs)


    def run(self):
        self.create_map(self.grid_size)
        self.obstacles.draw(self.screen)
        self.create_players(self.grid_size)

        end = False
        while end == False:
            dt = self.clock.tick(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    end = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                    self.playerB.moveto(1,1)
            self.players.update(self.stub)
            rects = self.players.draw(self.screen)
            pygame.display.update(rects)
            self.players.clear(self.screen,self.background)

        return True
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pygame.init()
    gm = GameUI(19, 22, 20)
    gm.run()