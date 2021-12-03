from urllib.request import Request, urlopen
import concurrent.futures


urls = open('res.txt', encoding='utf8').read().split('\n')


def viewer(url):
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


with concurrent.futures.ThreadPoolExecutor(50) as executor:
    future_to_url = {executor.submit(viewer, url=url): url for url in urls}
    for future in concurrent.futures.as_completed(future_to_url):
        future.result(60)