import random


def generate_random_numbers_string() -> str:
    """
    Function build string of 5-digit random number when each digit from 1 to 6.
    :return: str - calculated digits.
    """
    return "".join([str(random.randint(1, 6)) for x in range(5)])



