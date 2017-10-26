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
    num_of_walks = 20000
    walkable_block = 5
    max_block = 71
    cost_of_lyft = 10

    last_val_more_than_50 = walkable_block
    cost_by_walk = []

    for walk_len in range(1, max_block):
        no_lyft_needed = 0
        for j in range(num_of_walks):
            walk = random_walk(walk_len)
            total_distance_walked = abs(walk[0]) + abs(walk[1])

            if total_distance_walked <= walkable_block:
                no_lyft_needed += 1

        no_lyft_percent = 100 * float(no_lyft_needed) / num_of_walks
        lyft_needed = num_of_walks - no_lyft_needed
        lyft_cost = lyft_needed * cost_of_lyft

        cost_per_block = float(lyft_cost) / walk_len

        cost_by_walk.append((cost_per_block, walk_len))

        if no_lyft_percent > 50:
            last_val_more_than_50 = max(last_val_more_than_50, walk_len)

        print ("Total walk Length: ", walk_len,
                "No lyft required %", no_lyft_percent,
                "left needed for ", lyft_needed,
                "cost per block ", cost_per_block)

    print ("Last walk that had more chance of walking back than taking lyft ",
            last_val_more_than_50)

    print "An array of cost per block and the len of walk: "
    print (sorted(cost_by_walk)[:10])

main()
