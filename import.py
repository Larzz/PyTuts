# importing tutorial
import re


def regex(val):
    return re.sub('[A-Z]]', '', val)


print(regex('2l032 asd asd asd  ASD asd'))
