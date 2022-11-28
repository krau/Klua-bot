import requests
import os
import json

class Setu:
    def __init__(self,api) -> None:
        self.api=api

    def get_setu_url(self):
        '''从api get 1 张色图的直链'''
        setu_json = requests.get(self.api).json()
        setu_url = setu_json.get('url')
        return setu_url
