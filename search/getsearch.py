#-*-coding:utf-8-*-
import requests, re
from bs4 import BeautifulSoup as bs
import yaml


class Search_:

    headers = {
        'accept':'*/*', 
        'user-agent':'Mozilla/5.0 \
        (X11; Linux x86_64) AppleWebKit/537.36\
        (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    url = 'https://www.move2oregon.com/all-properties/farms-ranches'
    ROOT = 'https://www.move2oregon.com'
   
    def __init__(self):
        self.all_data = []

    def get_soup(self):
        self.session = requests.Session()
        self.request = self.session.get(Search_.url, headers=Search_.headers)
        self.soup = bs(self.request.content, 'html.parser')
        return self.soup

    def no_records_found(self):
        if self.soup.find(string=re.compile('Sorry, no records were found. Please try again.')):
            return True
        else:
            return False

    def get_data(self):
        #if there is 1 page
        self.end_marker = self.soup.find('li', class_='pagination-end').a.get('href')
        if not self.end_marker:
            print('1 page')
        else:
            print('MORE than 1 page')  # kind of: /all-properties/farms-ranches?start=125
            self.url_digits = int(re.findall(r'[0-9]+', self.end_marker)[0])
            
            while not self.url_digits < 0: #нам нужно и 0, а потом будет -25, -50 и тд, тогда и прекратим
                self.middle_url = Search_.url + '?start=' + str(self.url_digits)
                self.session = requests.Session()
                self.request = self.session.get(self.middle_url, headers=Search_.headers)
                self.soup = bs(self.request.content, 'html.parser')
                
                #ПОЛУЧИМ ЗНАЧЕНИЯ КАЖДОГО ДОМА
                for i in self.soup.find_all('div', class_='row-fluid ip-row0 ip-overview-row'):
                    
                    # img url
                    self.soup_img = i.find('div', class_='ip-property-thumb-holder').img.get('src').replace('_thumb', '').strip()
                    self.img_url = Search_.ROOT + self.soup_img
                    
                    # item title
                    self.item_title = i.find('div', class_='ip-overview-title').a.text.strip()          # 105 Dog Creek Rd
                    
                    # item url 
                    self.item_url = Search_.ROOT + i.find('div', class_='ip-overview-title').a.get('href').strip()
                    
                    # location
                    self.pre_located = i.find('div', class_='ip-overview-title').get_text().strip().replace(u'\xa0', u' ') 
                    # location is between - and Beds: - Wolf Creek, Oregon United StatesBeds:
                    self.item_location = str(re.search(r"-(.*)States", self.pre_located)[0])
                                        
                    # 2 types of price tag:
                    if i.find('h4', attrs={'class':'ip-overview-price pull-right'}):
                        self.item_price = i.find('h4', attrs={'class':'ip-overview-price pull-right'}).text.strip()
                    if i.find('span', attrs={'class':'ip-newprice'}):
                        self.item_price = i.find('span', class_='ip-newprice').text.strip()
                   
                    # additional info
                    self.item_add_info = i.find('div', class_='ip-overview-title').em.text.strip().replace(u'\xa0', u' ')

                    # item descripton
                    self.item_descripton = i.find('div', class_='ip-overview-short-desc').text.strip()
                
                    self.all_data.append([
                        self.img_url,
                        self.item_title,   
                        self.item_url, 
                        self.item_location, 
                        self.item_price,
                        self.item_add_info,
                        self.item_descripton
                    ])

                    print(self.middle_url, '\n', self.all_data)

                    input('NEXT')

                
                self.url_digits -= 25


         
            print('FINISHED')



'''

from search.getsearch import Search_
import re
s = Search_()
s.get_soup()
if s.no_records_found():
    print(f'NO RECORDS for url: {Search_.url}')
else:
    s.get_data()


'''