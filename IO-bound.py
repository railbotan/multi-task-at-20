import urllib
from urllib.request import Request, urlopen
from urllib.parse import unquote
import concurrent.futures

links = open('res.txt', encoding='utf8').read().split('\n')


def load_url(link, timeout):
    with urllib.request.urlopen(link, timeout=timeout) as conn:
        return conn.code


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