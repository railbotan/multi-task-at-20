## CPU-bound. Генерируем монетки
с использованием ProcessPoolExecutor:
```python
from hashlib import md5
from random import choice
import concurrent.futures
from datetime import datetime


def generate_hash(n):
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            return s + ',' + h


def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=100) as executor:
        for s in executor.map(generate_hash, range(10)):
            print(s)


if __name__ == '__main__':
    start = datetime.now()
    main()
    end = datetime.now()
    print(end - start)
```

* Замерьте скорость герации на 1 ядре у вас на компьютере
<img src="images/время синх..png"/> 

* Ускорьтесь за счет использования ProcessPoolExecutor
* Изменяйте количество воркеров: 2, 4, 5, 10, 100.
* Во время работы посмотрите с использованием стандартных утилит вашей OC загрузку памяти, процессора, сети, время работы. Зависят ли они от количества воркеров и как?

## время работы 
* с 2 воркерами: 
<img src="images/2 воркера время.png"/>
с 4 воркерами
<img src="images/4 воркера время.png"/>
с 5 воркерами
<img src="images/5 воркеров время.png"/>
с 10 воркерами
<img src="images/10 воркеров время.png"/>


## диспетчер задач
* с 2 воркерами: 
<img src="images/2 воркера диспетчер.png" width="700"/>
с 4 воркерами
<img src="images/4 воркера диспетчер.png" width="700"/>
с 5 воркерами
<img src="images/5 воркеров диспетчер.png" width="700"/>
с 10 воркерами
<img src="images/10 воркеров диспетчер.png" width="700"/>
с 100 воркерами
<img src="images/100 воркеров.png" width="700"/>

# Вывод
* так как задача CPU bound, наращивать количество воркеров, большее количества ядер, бесполезно.

