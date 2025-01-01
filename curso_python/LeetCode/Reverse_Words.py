# https://leetcode.com/problems/reverse-words-in-a-string-iii/
# Hello World!
# olleH !dlroW

string = 'Hello World!'


def inverte_string(string: str) -> str:
    return " ".join([palavra[::-1] for palavra in string.split(" ")])


print(inverte_string(string))
