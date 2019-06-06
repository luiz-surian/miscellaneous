# A group of Jewish soldiers are surrounded by Roman soldiers.
# To avoid being captured, the Jewish soldiers decide to commit suicide.
# So they arrange themselves in a circle, and each soldier should kill the one closest to his left.
# So the first soldier kill the second, the third one kill de fourth, and then so on and so forth.
# After the circle ends, the action is repeated until only one soldier is left, and then he should kill himself.
#
# But Josephus don't want to die, he prefers to surrender.
# So in which position should he stand to be the last man alive?
# The original story states 41 soldiers, but what would be a solution to calculate n soldiers?
#
# Numberphile has a great video about it: [https://youtu.be/uCsD3ZGzMgE]


import csv
from timeit import timeit


# O(n)
def josephus_v1(soldiers: int):
    soldiers = [i for i in range(1, soldiers + 1)]
    kill = 0
    while len(soldiers) > 1:
        kill = (kill + 1) % len(soldiers)
        soldiers.pop(kill)
    return soldiers[0]


# O(logN)
def josephus_v2(soldiers: int):
    # Winning Formula:
    # W(N) = 2L + 1

    # {soldiers}: N = Total number of soldiers.

    # (last_step}: L = N - P
    # {biggest_power}: P = Biggest power of 2 inside the total number of soldiers.

    # Find P
    biggest_power = 1
    while biggest_power*2 < soldiers:
        biggest_power = biggest_power*2

    # Calculate L
    last_step = soldiers - biggest_power

    # If N is a power of 2, should return 1, let's check it by seeing if:
    # L < P
    if last_step >= biggest_power:
        return 1

    return (2*last_step)+1


# O(1)
def josephus_v3(soldiers: int):
    # Convert to binary.
    binary = bin(soldiers)
    # Get the first digit and put it as last.
    shift = '0b' + binary[3::] + binary[2:3:]
    # Convert to decimal.
    return int(shift, 2)


# Testing:
josephus_results = {
    1: 1,
    2: 1,
    3: 3,
    4: 1,
    5: 3,
    6: 5,
    7: 7,
    8: 1,
    9: 3,
    10: 5,
    11: 7,
    12: 9,
    13: 11,
    16: 1,
    41: 19,
    100: 73,
    1000: 977
}


def test_josephus():
    for soldiers, expected_winner in josephus_results.items():
        # v1
        solution = josephus_v1(soldiers=soldiers)
        try:
            assert solution == expected_winner
        except AssertionError:
            print(f'josephus_v1(soldiers={soldiers}) expected {expected_winner}, but returned {solution}')

        # v2
        solution = josephus_v2(soldiers=soldiers)
        try:
            assert solution == expected_winner
        except AssertionError:
            print(f'josephus_v2(soldiers={soldiers}) expected {expected_winner}, but returned {solution}')

        # v3
        solution = josephus_v3(soldiers=soldiers)
        try:
            assert solution == expected_winner
        except AssertionError:
            print(f'josephus_v3(soldiers={soldiers}) expected {expected_winner}, but returned {solution}')


def csv_handle(info, mode='a'):
    with open('josephus.csv', mode, newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(info)


def benchmark(times=100):
    header = ['soldiers', 'v1 O(n)', 'v2 O(log n)', 'v3 O(1)']
    print(header)
    csv_handle(info=header, mode='w')
    for soldiers in range(1, times + 1):
        test = [soldiers,
                round(timeit(f'josephus_v1(soldiers={soldiers})', setup='from __main__ import josephus_v1'), 4),
                round(timeit(f'josephus_v2(soldiers={soldiers})', setup='from __main__ import josephus_v2'), 4),
                round(timeit(f'josephus_v3(soldiers={soldiers})', setup='from __main__ import josephus_v3'), 4)]
        print(test)
        csv_handle(info=test)
