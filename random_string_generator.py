import os
import math
import random

chars = (r"abcdefghijklmnopqrstuvwxyz"
         r"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
         r"0123456789"
         r"!@#$%&*()_+-={}[]^?~/,.;<>:\|'")


def random_generator(size=8):
    return ''.join(random.choice(chars) for x in range(size))


for i in range(8):
    if (i >= 3):
        number = int(math.pow(2, i))
        print(f"length {number}\n{random_generator(number)}\n")

os.system("pause")
