from os.path import isfile, exists


def is_integer(num: str) -> bool:
    is_valid = False
    try:
        num = num.strip()
        num2 = int(num)
        if 0 < len(str(num2)) == len(num):
            is_valid = True
    except Exception as e:
        print(e)
    finally:
        return is_valid


def file_exists(path: str) -> bool:
    return exists(path) and isfile(path)
