from concurrent.futures import ThreadPoolExecutor
from os import link
from urllib.request import Request, urlopen
from urllib.parse import unquote
from bs4 import BeautifulSoup
from tqdm import tqdm


def find_links():
    url = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%A1%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'
    res = open('res.txt', 'w', encoding='utf8')

    for _ in tqdm(range(100)):
        html = urlopen(url).read().decode('utf8')
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all('a')

        for l in links:
            href = l.get('href')
            if href and href.startswith('http') and 'wiki' not in href:
                print(href, file=res)
                
def check_links(url):
    try:
        request = Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},  
        )
        resp = urlopen(request, timeout=5)
        code = resp.code
        # print(code)
        resp.close()
        return code
    except Exception as e:
        return url, e
            
if __name__ == '__main__':
    links = open('res.txt', encoding='utf8').read().splitlines()
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        for i in executor.map(check_links, links):
            print(i)