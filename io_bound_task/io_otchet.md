# Параллелизм и асинхронность


## ThreadPoolExecutor

```python
import concurrent.futures
import urllib.request

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']

# Retrieve a single page and report the URL and contents
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page is %d bytes' % (url, len(data)))
```
## Синхронная проверка ссылок
```python
from urllib.request import Request, urlopen
from urllib.parse import unquote
from bs4 import BeautifulSoup
from tqdm import tqdm
from datetime import datetime

url = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%A1%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'


start = datetime.now()

for i in range(100):
    s = urlopen(url)
    print(unquote(s.url))


res = open('../res.txt', 'w', encoding='utf8')

for i in tqdm(range(100)):
    html = urlopen(url).read().decode('utf8')
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a')

    for l in links:
        href = l.get('href')
        if href and href.startswith('http') and 'wiki' not in href:
            print(href, file=res)


links = open('../res.txt', encoding='utf8').read().split('\n')

for url in links:
    try:
        request = Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
        )
        resp = urlopen(request, timeout=5)
        code = resp.code
        print(code)
        resp.close()
    except Exception as e:
        print(url, e)

end = datetime.now()
print(f"Время выполнения синхронной проверки ссылок: {end - start}")
```

* Замерьте время синхронной проверки ссылок.
<img src="images/время синх.проверки ссылок.png"/>
* Перепишите код, используя `ThreadPoolExecutor`. 
```python
from datetime import datetime
import urllib.request

import concurrent.futures

start = datetime.now()


def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as resp:
        return resp.code


links = open('../res.txt', encoding='utf8').read().split('\n')


with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    future_to_url = {executor.submit(load_url, url, 5): url for url in links}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as e:
            print('%r exception: %s' % (url, e))
        else:
            print(data)
end = datetime.now()

print(f"время проверки ссылок с использованием ThreadPoolExecutor: {end - start}")
```
* Изменяйте количество воркеров: 5, 10, 100.
* Во время работы посмотрите с использованием стандартных утилит вашей OC загрузку памяти, процессора, сети, время работы. Зависят ли они от количества воркеров и как?

* время работы: 
** с 5 воркерами:
<img src="images/5 воркеров время.png.png"/>
** с 10 воркерами
<img src="images/10 воркеров время.png"/>
** с 100 воркерами
<img src="images/100 воркеров время.png"/>

* диспетчер задач: 
** с 5 воркерами:
<img src="images/5 воркеров диспетчер.png.png"/>
** с 10 воркерами
<img src="images/10 воркеров диспетчер.png.png"/>
** с 100 воркерами
<img src="images/100 воркеров диспетчер.png.png"/>


## CPU-bound. Генерируем монетки

Придумаем некоторый прототип криптовалюты, построенный на концепции [Proof of work](https://en.wikipedia.org/wiki/Proof_of_work). Монетой будет считаться некоторая строка длины 50 из последовательности цифр 0-9, у которой md5-hash заканчивается на `00000`. Так как md5 &mdash; односторонняя функция, мы не можем по ее результату судить об аргументе, найти монеты мы можем только одим способом &mdash; перебором.

```python
from hashlib import md5
from random import choice


while True:
    s = "".join([choice("0123456789") for i in range(50)])
    h = md5(s.encode('utf8')).hexdigest()

    if h.endswith("00000"):
        print(s, h)
```

Я нашел несколько монет:

```
91625571520935147263403534421427761877088219542499 8adaf58d5c51fc1216820c1201100000
49262841446921579383645162499800846153508846372671 974d52bc5430d4c8ed96963648e00000
34359601233782192016006582448729953029075086207271 0209b01867080f7eaf20f6c674000000
02809251779741159345845523287375801745436182367614 2fd27ad5f1d1efe1f000c3ee66f00000
```

У нас отсутсвует Блокчейн, то есть мы не можем доказать, что монета была сгенерирована именно нами или принадлежит нам: если мы кому-то ее покажем, ее тут же украдут. Эту часть мы оставим за рамками задания.

* Замерьте скорость герации на 1 ядре у вас на компьютере.
* Ускорьтесь за счет использования `ProcessPoolExecutor`.
* Изменяйте количество воркеров: 2, 4, 5, 10, 100.
* Во время работы посмотрите с использованием стандартных утилит вашей OC загрузку памяти, процессора, сети, время работы. Зависят ли они от количества воркеров и как?
* Убедитесь в том, что так как задача CPU bound, наращивать количество воркеров, большее количества ядер, бесполезно.

