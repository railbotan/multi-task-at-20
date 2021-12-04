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