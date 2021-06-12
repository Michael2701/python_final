from os.path import isfile, exists


def is_integer(num: str) -> bool:
    """
    Check if given string is integer representation
    :param num: string number
    :return: true if string is a number otherwise false
    """
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
    """
    Check if file exists in given path and it is file.
    :param path: file path in machine
    :return: true if this file otherwise false
    """
    return exists(path) and isfile(path)
