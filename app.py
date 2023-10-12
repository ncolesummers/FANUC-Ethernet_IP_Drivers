# Imports
from src.robot_controller import robot
from netcode import get_remote_position, send_position

def part1(robot):


def main():
    robert = "172.29.208.119"
    # Create robot object
    crx10 = robot(robert)
    for i in range(0, 2):
        part1(crx10)

    for i in range(0, 2):
        part2(crx10)


if __name__ == "__main__":
    main()
