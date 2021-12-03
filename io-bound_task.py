import concurrent.futures
import urllib
from datetime import datetime
from urllib.request import urlopen, Request

from bs4 import BeautifulSoup
from tqdm import tqdm

url = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%A1%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'


def writeRefs():
    with open('res.txt', 'w', encoding='utf8') as res:
        for i in tqdm(range(100)):
            html = urlopen(url).read().decode('utf8')
            soup = BeautifulSoup(html, 'html.parser')
            links = soup.find_all('a')

            for l in links:
                href = l.get('href')
                if href and href.startswith('http') and 'wiki' not in href:
                    print(href, file=res)


def readRefs():
    with open('res.txt', encoding='utf8') as links:
        for url in links.readlines():
            try:
                request = Request(
                    url,
                    headers={
                        'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
                )
                resp = urlopen(request, timeout=5)
                code = resp.code
                print(code)
                resp.close()
            except Exception as e:
                print(url, e)


def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as resp:
        code = resp.code
        return code


def readMultiThreadRefs():
    with open('res.txt', encoding='utf8') as links:
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            future_urls = {executor.submit(load_url, url, 5): url for url in links.readlines()}
            for future in concurrent.futures.as_completed(future_urls):
                url = future_urls[future]
                try:
                    data = future.result()
                    print(data)
                except Exception as e:
                    print(url, e)


start_time = datetime.now()
readMultiThreadRefs()
end_time = datetime.now()
print(end_time - start_time)
