#-*-coding:utf-8-*-
import requests, re
from bs4 import BeautifulSoup as bs


'''
import requests, re
from bs4 import BeautifulSoup as bs
from search.getsearch import Search_, OnePage
from django.core.paginator import Paginator
s = Search_('https://www.move2oregon.com/all-properties/55-retirement')
s.get_soup()
o = OnePage()
o.main()
paginator = Paginator(o.all_data, 2) 
page = request.GET.get('page')
print(page)
pagination = paginator.get_page(page)
'''

class Search_:

    headers = {
        'accept':'*/*', 
        'user-agent':'Mozilla/5.0 \
        (X11; Linux x86_64) AppleWebKit/537.36\
        (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    ROOT = 'https://www.move2oregon.com/all-properties/' 
    CLEAR_ROOT = 'https://www.move2oregon.com'
    soup = ''

    def __init__(self):
        self.all_data = []
    
    def set_url(self, t):
        self.url = Search_.ROOT + t
        return self.url   

    def get_soup(self):
        self.session = requests.Session()
        self.request = self.session.get(self.url, headers=Search_.headers)
        self.soup = bs(self.request.content, 'html.parser')
        Search_.soup = self.soup
        return self.soup

    def records_found(self):
        if self.soup.find(string=re.compile('Sorry, no records were found. Please try again.')):
            return False
        else:
            return True

    def only_one_page_found(self): # if True, OnePage.main()
        try:
            self.end_marker = self.soup.find('li', class_='pagination-end').a.get('href')
            return False
        except AttributeError as e: # there is only 1 page for this category
            print('There is only 1 page for this real estate category')            
            return True
    
    def get_url_digits(self):
        print('MORE than 1 page')  # kind of: /all-properties/farms-ranches?start=125
        self.url_digits = int(re.findall(r'[0-9]+', self.end_marker)[0])
        self.zero = 0
        return (self.zero, self.url_digits)

    def main(self):            
        while self.zero < (self.url_digits+1): #нам нужно и 0, а потом будет -25, -50 и тд, тогда и прекратим
            self.url = self.url + '?start=' + str(self.zero)
            self.session = requests.Session()
            self.request = self.session.get(self.url, headers=Search_.headers)
            self.soup = bs(self.request.content, 'html.parser')
                        
            #ПОЛУЧИМ ЗНАЧЕНИЯ КАЖДОГО ДОМА
            for i in self.soup.find_all('div', class_='ip-overview-row'): 
                            
                # img url
                self.soup_img = i.find('div', class_='ip-property-thumb-holder').img.get('src').replace('_thumb', '').strip()
                self.img_url = Search_.CLEAR_ROOT + self.soup_img
                            
                # item title
                self.item_title = i.find('div', class_='ip-overview-title').a.text.strip()          # 105 Dog Creek Rd
                            
                # item url 
                self.item_url = Search_.ROOT + i.find('div', class_='ip-overview-title').a.get('href').strip()
                            
                # location
                self.item_pre_location = i.find('div', class_='ip-overview-title').text.strip().replace(u'\xa0', u' ') 
                # location is between - and Beds: - Wolf Creek, Oregon United StatesBeds 
                # or between - and none:
                try:
                    #case 1 (- and Beds)
                    self.item_location = re.findall('- (.*)Beds', self.item_pre_location)
                    #case 2 (- and none)
                    if len(self.item_location) == 0:
                        self.item_location = re.findall('- (.*)', self.item_pre_location)
                    #print(self.item_location)
                except Exception as err:
                    print(self.item_location, '\n', err)
                    input('ENTER TO CONTINUE')
                    print(self.item_title, self.item_location)
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
                    self.item_location[0], 
                    self.item_price,
                    self.item_add_info,
                    self.item_descripton
                ])   

            self.zero += 25
                 
        print('FINISHED')

        return self.all_data


class OnePage(Search_):
    '''
    if only one page at given category
    '''

    def __init__(self):
        self.all_data = []
        self.soup = Search_.soup
    
    def main(self):            
        try:
            '''self.session = requests.Session()
            self.request = self.session.get(self.url, headers=Search_.headers)
            self.soup = bs(self.request.content, 'html.parser')'''
                        
            #ПОЛУЧИМ ЗНАЧЕНИЯ КАЖДОГО ДОМА
            for i in self.soup.find_all('div', class_='ip-overview-row'): 
                            
                # img url
                self.soup_img = i.find('div', class_='ip-property-thumb-holder').img.get('src').replace('_thumb', '').strip()
                self.img_url = Search_.CLEAR_ROOT + self.soup_img
                            
                # item title
                self.item_title = i.find('div', class_='ip-overview-title').a.text.strip()          # 105 Dog Creek Rd
                            
                # item url 
                self.item_url = Search_.ROOT + i.find('div', class_='ip-overview-title').a.get('href').strip()
                            
                # location
                self.item_pre_location = i.find('div', class_='ip-overview-title').text.strip().replace(u'\xa0', u' ') 
                # location is between - and Beds: - Wolf Creek, Oregon United StatesBeds 
                # or between - and none:
                try:
                    #case 1 (- and Beds)
                    self.item_location = re.findall('- (.*)Beds', self.item_pre_location)
                    #case 2 (- and none)
                    if len(self.item_location) == 0:
                        self.item_location = re.findall('- (.*)', self.item_pre_location)
                    #print(self.item_location)
                except Exception as err:
                    print(self.item_location, '\n', err)
                    input('ENTER TO CONTINUE')
                    print(self.item_title, self.item_location)
                
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
                    self.item_location[0], 
                    self.item_price,
                    self.item_add_info,
                    self.item_descripton
                ])   
           
            print('FINISHED')

            return self.all_data

        except Exception as e:
            print(e)
            input('Error in OnePage, press enter')
 


'''
from search.getsearch import Search_, OnePage
import re  
s = Search_('https://www.move2oregon.com/all-properties/55-retirement')
s.get_soup()

s.records_found()       
s.only_one_page_found() IF TRUE, СОЗДАЕМ ОБЪЕКТ O = ONEPAGE()
s.get_end_marker()

from search.getsearch import Search_, OnePage
import re
o = OnePage('https://www.move2oregon.com/all-properties/55-retirement')
o.get_soup()
o.records_found()
o.only_one_page_found()
'''