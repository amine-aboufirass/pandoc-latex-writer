from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
from datetime import datetime
import calendar

def online_resource(reference):
    result = '@misc{\n'
    result += f'    {reference["id"]},\n'
    result += f'    author = {{{{{reference["author"]}}}}},\n'
    result += f'    year = {reference["year"]},\n'

    url = reference['url']
    url_domain = "https://"+urlparse(url).netloc

    html = requests.get(url, verify=False).content
    html_domain = requests.get(url_domain, verify=False).content

    soup = BeautifulSoup(html, features="html.parser")
    soup_domain = BeautifulSoup(html_domain, features="html.parser")

    result += f'    journal = {{{{{soup_domain.title.string}}}}},\n'
    result += f'    title = {{{{{soup.title.string}}}}},\n'
    
    today = datetime.today()
    day = today.day
    year = today.year
    month = calendar.month_name[today.month]
    result += f'    note = {{[Online; accessed {day}-{month}-{year}]}},\n'
    result += f'    howpublished = {{\\href{{{url}}}{{link}}}},\n'
    
    result += '}\n\n'
    
    return result


def online_resource_manual(reference):
    result = '@misc{\n'
    result += f'    {reference["id"]},\n'
    result += f'    author = {{{{{reference["author"]}}}}},\n'
    result += f'    year = {reference["year"]},\n'
    result += f'    journal = {{{{{reference["pagetitle"]}}}}},\n'
    result += f'    title = {{{{{reference["homepagetitle"]}}}}},\n'
    today = datetime.today()
    day = today.day
    year = today.year
    month = calendar.month_name[today.month]
    result += f'    note = {{[Online; accessed {day}-{month}-{year}]}},\n'
    result += f'    howpublished = {{\\href{{{reference["url"]}}}{{link}}}},\n'

    result += '}\n\n'

    return result

def book(reference):
    result = "@book{\n"
    result += f'{reference["id"]},\n'
    result += f'    author = {{{{{reference["author"]}}}}},\n'
    result += f'    title = {{{{{reference["title"]}}}}},\n'
    result += f'    publisher = {{{{{reference["publisher"]}}}}},\n'
    result += f'    year = {reference["year"]},\n'

    if "edition" in reference.keys():
        result += f'    edition = {{{{{reference["edition"]}}}}},\n'

    result += '}\n\n'

    return result
