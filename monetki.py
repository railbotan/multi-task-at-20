from hashlib import md5
from random import choice
import cProfile
import concurrent.futures


def generate_coins(c):
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()
        if h.endswith("00000"):
            c = "{} {}".format(s, h)
            break
    return c


def main_generate_coins():
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        for coin in zip(executor.map(generate_coins, [0,0,0,0,0,0,0,0])):
            print(coin)


if __name__ == '__main__':
    main_generate_coins()
    cProfile.run('main_generate_coins()')