import re

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')


def isNumOrDot(string: str) -> bool:
    return bool(NUM_OR_DOT_REGEX.search(string))


def isValidNumber(string: str):
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False

    return valid


def isEmpty(string: str) -> int:
    return len(string) == 0