# Параллелизм и асинхронность

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

## Переписанный код, с использованием ThreadPoolExecutor

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

## время работы 
с 5 воркерами: 
<img src="images/5 воркеров время.png"/>
с 10 воркерами
<img src="images/10 воркеров время.png"/>
с 100 воркерами
<img src="images/100 воркеров время.png"/>

## диспетчер задач
* с 5 воркерами:
<img src="images/5 воркеров диспетчер.png" width="700"/>
с 10 воркерами
<img src="images/10 воркеров диспетчер.png" width="700"/>
с 100 воркерами
<img src="images/100 воркеров диспетчер.png" width="700"/>

# Вывод
При увеличении количества воркеров незначительно возрастает использование памяти, уменьшается скорость. Сильно уменьшается время выполнения.

