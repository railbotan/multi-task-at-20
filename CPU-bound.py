from hashlib import md5
from random import choice
import concurrent.futures


def find_coin(n):
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            return f"{s}, {h}"


def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=100) as executor:
        for answer in zip(executor.map(find_coin, range(3))):
            print(answer)


if __name__ == '__main__':
    main()