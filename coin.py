from concurrent.futures import ProcessPoolExecutor
import time
from hashlib import md5
from random import choice

def get_coins(n):
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            return s, h

def main():
    with ProcessPoolExecutor(max_workers=61) as executor:
        for coin in zip(executor.map(get_coins, range(4))):
            print(coin)

if __name__ == '__main__':
    s = time.time()
    main()
    f = time.time()
    print(f - s)