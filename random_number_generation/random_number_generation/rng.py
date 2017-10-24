"""
Done by: Samman Bikram Thapa of Howard University as part of an assignment for
CSCI 410 Modeling and Simulation class in fall 2017 taught by Dr. Gloria 
Washington. The program uses python 2.7
"""

"""
User stories:
    - Asks users for their choice of distribution:
        - Exponential distribution
        - Uniform distribution
    - Ask users for ther choice of technique:
        - LCG
        - Additive
        - Quadratic
    - The distribution generated must be output in a comma separated file
    - The distribution generated must be between one and zero.
"""

import math
import csv

def main():
    distr_type = 0
    technique = 0

    while True:
        # ask user for the type fo distribution of random number they want
        prompt = "Type of distribution of random number?\n"
        options = """Choose
                     0 for exponential,
                     1 for uniform,
                     and -1 to exit the program\n"""
        distr_type = raw_input(prompt + options)

        valid_options = ['0', '1', '-1']
        if not distr_type in valid_options:
            print ("No such option, please reselect")
            continue

        if distr_type == '-1':
            return

        distr_type = int(distr_type)
        break

    while True:
        # ask user for the technique to generate the random numbers with
        prompt = "What technique do you want to generate random numbers with?\n"
        options = """Choose
                     0 for LCG,
                     1 for Additive,
                     2 for Quadratic,
                     -1 to quit.\n"""
        technique = raw_input(prompt +  options)

        valid_options = ['0', '1', '2', '-1']
        if not technique in valid_options:
            print ("No such option, please reselect")
            continue

        if technique == '-1':
            return

        technique = int(technique)
        break

    # till here we have distr_type and technique
    if technique == 0:
        random_nums = rng_lcg(1000, 249513)
    elif technique == 1:
        random_nums = rng_additive(1000, 249513)
    elif technique == 2:
        random_nums = rng_quadratic(1000, 249513)

    # for exponential distribution, it follows uniform distribution by default
    if distr_type == 0:
        lmd = 0.5
        for i in range(len(random_nums)):
            exp_rnd = -lmd * math.log(1 - random_nums[i])
            random_nums[i] = exp_rnd

        with open('thapa_samman_exponential.csv', 'wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for num in random_nums:
                writer.writerow([num])

    elif distr_type == 1:
        with open('thapa_samman_uniform.csv', 'wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for num in random_nums:
                writer.writerow([num])


# using Xn+1 = (a*Xn + c) mod m
def rng_lcg(num_of_val, start_val):
    m = 2147483647
    a = 16807
    c = 2
    am_mil = 1.0 / m
    random_num = []

    counter = 0
    curr_val = start_val
    while counter < num_of_val:
        next_val = (a * curr_val + c) % m
        random_num.append(next_val * am_mil)
        counter += 1
        curr_val = next_val
    return random_num

# using Xn+1 = (dXn**2 + aXn + c) mod m
def rng_quadratic(num_of_val, start_val):
    m = 2 ** math.e
    am_mil = 1.0 / m
    random_num = []

    counter = 0
    curr_val = start_val
    while counter < num_of_val:
        next_val = (curr_val * (curr_val + 1)) % m
        random_num.append(next_val * am_mil)
        counter += 1
        curr_val = next_val
    return random_num

# Xn = (Xn-24 + Xn-55) mod m for n >= 55
def rng_additive(num_of_val, start_val):
    m = 2 ** math.e
    am_mil = 1.0 / m
    random_nums = []
    y = [x for x in range(56)]
    j = 24
    k = 55
    n = 55

    counter = 0
    while counter < num_of_val:
        # set y[k] = y[k] + y[j]
        y[k] = (y[k] + y[j]) % m
        random_nums.append(y[k] * am_mil)
        j -= 1
        k -= 1

        if j == 0:
            j = 55
        if k == 0:
            k = 55

        counter += 1

    return random_nums



main()
print ("Random Numbers Generation Program exiting.")
