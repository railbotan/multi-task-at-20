import concurrent.futures
from datetime import datetime
from hashlib import md5
from random import choice


def make_hash(i):
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()
        if h.endswith("00000"):
            return s, h


def makeMultiProcessHashes():
    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
        for s in executor.map(make_hash, range(10)):
            print(s)


def makeMultiThreadHashes():
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        for s in executor.map(make_hash, range(10)):
            print(s)


if __name__ == '__main__':
    start_time = datetime.now()
    makeMultiProcessHashes()
    end_time = datetime.now()
    print(end_time - start_time)
