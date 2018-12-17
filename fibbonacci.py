# Challenge from: https://skillupper.com/fibonacci/naive

import pickle
import random

def load_list():
    try:
        with open('fibonacci.pydata', 'rb') as file:
            fib = pickle.load(file)
    except Exception:
        fib = [1, 1]
    return fib

def save_list(fib):
    try:
        with open('fibonacci.pydata', 'wb') as file:
            pickle.dump(fib, file)
    except Exception as e:
        print('Couldn\'t save data', e)


def fibonacci(n):
    fib = load_list()
    if n < len(fib):
        return fib[n]
    else:
        step = fib[-1]
        for _ in range(len(fib), n-2):
            step = fib[-1] + fib[-2]
            fib.append(step)
        save_list(fib)
        return step

def test(starts=10, steps=10, rand_min=1, rand_max=50):
    n = starts
    for step in range(steps):
        n += random.randint(rand_min, rand_max)
        result = fibonacci(n)
        print(f'Test {step+1}: fibonacci({n}) = {result}')


result = fibonacci(100)
print(result)
