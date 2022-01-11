'''
Created on 3 Aug 2021
@author: qsong
'''
import requests as requests
import unittest
from bs4 import BeautifulSoup
from ..utils import util_time

class wh_message(object):
    '''
    This module provides wuhu20888 functions
    '''
    game_base_url = "https://wh20888.com/"

    def __init__(self):
        '''
        Constructor
        '''
        return

    def __del__(self):
        return

    def get_wh_message(self):
        wh_response = requests.get(self.game_base_url)
        wh_response = wh_response
        if wh_response.status_code == 200:
            soup = BeautifulSoup(wh_response.content, 'html.parser', from_encoding="gb18030")
            soup.prettify()
            ul_table = soup.find('ul')
            li_list = ul_table.find_all('li')

            for li_item in li_list:
                if len(li_item.contents) >= 5:
                    wh_message_provider =  li_item.contents[-3].contents[0]
                    wh_message_time =  li_item.contents[-2].replace('】', '')
                    wh_message_text =  li_item.contents[-5].contents[0]
                    wh_message_link =  li_item.contents[-5].attrs['href']
                    print(wh_message_time)
        return li_list

class Test(unittest.TestCase):

    def setUp(self):
        self.test_obj = wh_message()

    def tearDown(self):
        self.test_obj = None
        return

    def test_get_wuhu_message(self):
        self.test_obj.get_wh_message()
        return