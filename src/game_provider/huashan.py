'''
Created on 3 Aug 2021
@author: qsong
'''
import requests as requests
import unittest
from bs4 import BeautifulSoup


class huanshan_message(object):
    '''
    This module provides huanshan functions
    '''
    game_base_url = "https://bbs.hszqb2.com/bbs-1.html"

    def __init__(self):
        '''
        Constructor
        '''
        return

    def __del__(self):
        return

    def get_huashan_message(self):
        huanshan_response = requests.get(self.game_base_url)
        if huanshan_response.status_code == 200:
            soup = BeautifulSoup(huanshan_response.content, 'html.parser', from_encoding="gb18030")
            soup.prettify()
            ul_table = soup.find('ul')
            li_list = ul_table.find_all('li')
            for li_item in li_list:
                print("li_item.contents = " + str(len(li_item.contents)))
                if len(li_item.contents) > 3 and :
                    print("time" + li_item.contents[-2].text)  # time
                    print("name" + li_item.contents[-3].text)  # name
                    print("message" + li_item.contents[-5].text)  # message
                    print("---------------")

        return li_list


class Test(unittest.TestCase):

    def setUp(self):
        self.test_obj = huanshan_message()

    def tearDown(self):
        self.test_obj = None
        return

    def test_get_huanshan_message(self):
        self.test_obj.get_huashan_message()
        return
