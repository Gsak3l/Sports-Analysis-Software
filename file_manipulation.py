from urllib import request
from bs4 import BeautifulSoup


def html_to_text(page):
    url_1 = page
    page = request.urlopen(url_1)
    soup = BeautifulSoup(page)
    return soup.prettify()


def open_html_file(page):
    with open('./index.html') as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        return soup.prettify()
