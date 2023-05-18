import pygame
from client_stub import StubClient
from client_game import GameUI


def main():
    pygame.init()
    stub = StubClient()
    ui = GameUI(stub, 32)
    ui.run()


main()