from hashlib import md5
from random import choice
import concurrent.futures
import time


def miner(n):
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()
        if h.endswith("00000"):
            return s + ' ' + h


def main():
    with concurrent.futures.ProcessPoolExecutor(10) as executor:
        for chain in zip(executor.map(miner, range(4))):
            print(chain)


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(end_time - start_time)