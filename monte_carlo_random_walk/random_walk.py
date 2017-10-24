import random

def random_walk(n):
    """ Return coordinates after n blocks random walk"""
    x, y = 0, 0

    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy

    return x, y


def main():
    """ First function that runs on running this module"""
    num_of_simulation = 25
    num_of_blocks = 6

    for i in range(num_of_simulation):
        walk = random_walk(num_of_blocks)
        total_distance_back = abs(walk[0] + walk[1])

        print "The distance from home is ", abs(walk[0] + walk[1])

main()
