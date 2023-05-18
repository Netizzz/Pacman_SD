import game_mech
from server_skeleton import SkeletonServer


def main():
    gm = game_mech.GameMech()
    skeleton = SkeletonServer(gm)
    skeleton.run()


main()