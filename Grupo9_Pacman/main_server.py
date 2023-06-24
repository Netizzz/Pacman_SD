from game_mech import GameMech
from server_skeleton import SkeletonServer


def main():
    gmech = GameMech(19,22)
    skeleton = SkeletonServer(gmech)
    skeleton.run()


main()