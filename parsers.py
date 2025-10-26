import requests
import re 
from scrapy import Selector
from urllib.parse import urljoin
from settings import BASE_URL, HEADERS, TIMEOUT

def get_category_links():
    response = requests.get(BASE_URL, headers=HEADERS, timeout=TIMEOUT)
    sel = Selector(text=response.text)
    print(response.status_code) 
    categories = {}
    for a in sel.css("div.side_categories ul li ul li a"):
        name = a.css("::text").get().strip()
        href = a.attrib["href"]
        url = urljoin(BASE_URL, href)
        categories[name] = url
    return categories

def parse_list_page(category_url):
    urls = []
    next_url = category_url
    while next_url:
        response = requests.get(next_url, headers=HEADERS, timeout=TIMEOUT)
        sel = Selector(text=response.text)
        for element in sel.css('article.product_pod h3 a::attr(href)').getall():
            urls.append(urljoin(next_url, element))
        next_page = sel.css('li.next a::attr(href)').get()
        next_url = urljoin(next_url, next_page) if next_page else None
    return urls

def parse_product_page(product_url):
    response = requests.get(product_url, headers=HEADERS, timeout=TIMEOUT)
    response.encoding = 'utf-8' 
    sel = Selector(text=response.text)
    titre = sel.css("h1::text").get()
    prix = sel.css("p.price_color::text").get()
    dispo_text = next((x.strip() for x in sel.css("p.instock.availability::text").getall() if x.strip()), "")
    match = re.search(r"\((\d+) available\)", dispo_text)
    dispo = int(match.group(1)) if match else 0
    note_class = sel.css('p.star-rating::attr(class)').get()  # "star-rating Two"
    note = note_class.split()[-1] if note_class else ""
    upc = sel.xpath('//tr[th="UPC"]/td/text()').get()
    image = sel.css('img::attr(src)').get()
    image_absolu = urljoin(product_url, image)
    return {
        "titre": titre,
        "prix": prix,
        "dispo": dispo,
        "note": note,
        "upc": upc,
        "image": image_absolu
    }
