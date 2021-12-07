import concurrent.futures
import urllib
from datetime import datetime
from urllib.request import urlopen


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
