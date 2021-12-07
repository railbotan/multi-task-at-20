from hashlib import md5
from random import choice


def makeHashes():
    j = 0
    while j != 5:
        s = "".join([choice("0123456789") for _ in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            j += 1
            print(s, h)
