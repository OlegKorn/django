#-*-coding:utf-8-*-
import requests, re
from bs4 import BeautifulSoup as bs


class Currency_:
    '''
    from bboard.currency import Currency_
    c = Currency_()
    c.get_soup()
    c.get_codes()
    c.get_nominals()
    c.get_names()
    c.get_values()
    c.get_changes()
    c.get_percents()
    '''

    headers = {
        'accept':'*/*', 
        'user-agent':'Mozilla/5.0 \
        (X11; Linux x86_64) AppleWebKit/537.36\
        (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    url = 'https://finance.rambler.ru/currencies'
   
    #SOUP
    def get_soup(self):
        self.session = requests.Session()
        self.request = self.session.get(Currency_.url, headers=Currency_.headers)
        self.soup = bs(self.request.content, 'html.parser')
    #SOUP

    def get_codes(self):
        self.codes_html = self.soup.find_all('div', class_=re.compile('.*--code.*'))[0:]
        self.codes = [self.code.text.replace('\n', '') for self.code in self.codes_html[1:]]
        return self.codes

    def get_nominals(self):
        self.nominals_html = self.soup.find_all('div', class_=re.compile('.*--denomination.*'))[0:]
        self.nominals = [self.nominal.text.replace('\n', '') for self.nominal in self.nominals_html[1:]]
        return self.nominals

    def get_names(self):
        self.names_html = self.soup.find_all('div', class_=re.compile('.*--currency.*'))[0:]
        self.names = [self.name.text.replace('\n', '') for self.name in self.names_html[1:]]
        return self.names     
    
    def get_values(self):
        self.value_html = self.soup.find_all('div', class_=re.compile('.*--value.*'))[0:]
        self.values = [self.value.text.replace('\n', '') for self.value in self.value_html[1:]]
        return self.values

    def get_changes(self):
        self.changes_html = self.soup.find_all('div', class_=re.compile('.*--change.*'))[0:]
        self.changes = [self.change.text.replace('\n', '') for self.change in self.changes_html[1:]]
        return self.changes   

    def get_percents(self):
        self.percents_html = self.soup.find_all('div', class_=re.compile('.*--percent.*'))[0:]
        self.percents = [self.percent.text.replace('\n', '') for self.percent in self.percents_html[1:]]
        return self.percents 

    def get_list_of_all(self):
        self.list_of_all = list(zip(
              self.get_codes(),
              self.get_nominals(),
              self.get_names(),
              self.get_values(),
              self.get_changes(),
              self.get_percents()
        ))

        return self.list_of_all

'''
from getcurrency.currency import Currency_
c = Currency_()
c.get_soup()
c.get_list_of_all()
'''