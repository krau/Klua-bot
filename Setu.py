import requests

class Setu:
    def __init__(self,baseapi) -> None:
        self.baseapi=baseapi

    def get_setu_url(self):
        '''从api get 1 张色图的直链'''
        setu_api = self.baseapi+'/setu'
        setu_json = requests.get(setu_api).json()
        setu_url = setu_json.get('url')
        return setu_url
