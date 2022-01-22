'''
Created on 3 Aug 2021
@author: qsong
'''
import requests as requests
import unittest
from bs4 import BeautifulSoup
import psycopg2 as psycopg2
from src import utils

class wh_message(object):
    '''
    This module provides wuhu20888 functions
    '''
    game_base_url = "https://wh20888.com/"

    def __init__(self):
        '''
        Constructor
        '''
        self.postgre_conn = psycopg2.connect(
            host="192.168.31.202",
            database="qwin",
            user="postgres",
            password="admin")
        return

    def __del__(self):
        return

    def add_message_to_db (self, message):
        cur = self.postgre_conn.cursor()
        # sql = """INSERT INTO vendors(vendor_name)
        #      VALUES(%s) RETURNING vendor_id;"""
        # cur.execute(sql, (value1, value2))
        sql = """SELECT * FROM users;"""
        cur.execute(sql)
        user_records = cur.fetchall()
        print('user_records')
        return

    def get_wh_message(self):
        wh_response = requests.get(self.game_base_url)
        wh_response = wh_response
        if wh_response.status_code == 200:
            soup = BeautifulSoup(wh_response.content, 'html.parser', from_encoding="gb18030")
            soup.prettify()
            ul_table = soup.find('ul')
            li_list = ul_table.find_all('li')
            wh_message = {}
            for li_item in li_list:
                if len(li_item.contents) >= 5:
                    wh_message['wh_message_provider'] =  li_item.contents[-3].contents[0]
                    wh_message['wh_message_time'] =  li_item.contents[-2].replace('】', '')
                    wh_message['wh_message_time_int'] = utils.convert_time_to_int(wh_message['wh_message_time'])
                    wh_message['wh_message_text'] =  li_item.contents[-5].contents[0]
                    wh_message['wh_message_link'] =  li_item.contents[-5].attrs['href']
                    self.add_message_to_db(wh_message)

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