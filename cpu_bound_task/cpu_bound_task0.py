from hashlib import md5
from random import choice
from datetime import datetime
start = datetime.now()

for j in range(13000000):
    s = "".join([choice("0123456789") for i in range(50)])
    h = md5(s.encode('utf8')).hexdigest()

    if h.endswith("00000"):
        print(s, h)

end = datetime.now()
print(f"{end - start}")