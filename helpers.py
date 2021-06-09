import random


def generate_random_numbers_string():
    return "".join([str(random.randint(1, 6)) for x in range(5)])



