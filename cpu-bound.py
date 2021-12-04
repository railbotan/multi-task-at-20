from hashlib import md5
from random import choice
import concurrent.futures
from time import time


def is_prime(n):
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            return s + ',' + h


def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=100) as executor:
        for answer in zip(executor.map(is_prime, range(3))):
            print(answer)


if __name__ == '__main__':
    time1 = time()
    main()
    time2 = time()
    print(time2 - time1)