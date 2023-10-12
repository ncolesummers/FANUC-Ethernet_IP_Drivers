import sys
import random
from os.path import dirname

from robot_controller import robot

sys.path.append(dirname(__file__) + "/FANUC-Ethernet_IP_Drivers")

my_coords = [526, -589, 260, -93, 62, 177]


bunsen = "172.29.208.123"

coords = [526, -589, 260, -93, 62, 177]
# randomize the first 3 coords within 10 of the original
coords[0] = random.randint(coords[0] - 10, coords[0] + 10)
coords[1] = random.randint(coords[1] - 10, coords[1] + 10)
coords[2] = random.randint(coords[2] - 10, coords[2] + 10)

print(coords)

robert_home_coords = [493, 842, 260, 93, -59, 177]


def main():
    crx10 = robot(bunsen)
    print("Starting robot")

    crx10.set_speed(100)

    # crx10.set_joints_to_home_position()
    # crx10.start_robot()

    crx10.write_cartesian_position()
    # randomize the first

    crx10.start_robot()


if __name__ == "__main__":
    main()
