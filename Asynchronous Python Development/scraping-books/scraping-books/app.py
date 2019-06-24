import requests
import logging

from pages.all_books_page import AllBooksPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')

logger = logging.getLogger('scraping')

logger.info('Loading books list...')

books = []
page_content = requests.get(f'http://books.toscrape.com/').content
page = AllBooksPage(page_content)

for i in range(page.page_count):
    page_content = requests.get(f'http://books.toscrape.com/catalogue/page-{i+1}.html').content
    page = AllBooksPage(page_content)
    books.extend(page.books)
