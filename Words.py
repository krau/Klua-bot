import requests
import random


class Words:
    def __init__(self, baseapi) -> None:
        self.baseapi = baseapi+'/words'

    def get_wanan(self):
        '''晚安！'''
        wanan_api = self.baseapi+'/wanan'
        try:
            wanan_words = requests.get(wanan_api).json()[0]
            return wanan_words
        except:
            return 'Exception:夜晚，使人宁静'

    def get_aoligei(self):
        '''正能量'''
        aoligei_api = self.baseapi+'/aoligei'
        try:
            aoligei_words = requests.get(aoligei_api).json()[0]
            return aoligei_words
        except:
            return 'Exception:好好好好好好'

    def get_niubi(self):
        '''牛逼'''
        niubi_api = self.baseapi+'/niubi'
        try:
            niubi_words = requests.get(niubi_api).json()[
                0].replace('${name}', 'Klua')
            return niubi_words
        except:
            return 'Exception:你说的对，后面忘了'

    def get_young(self):
        '''大老师'''
        young_api = self.baseapi+'/young'
        try:
            young_words = requests.get(young_api).json()[0]
            return young_words
        except:
            return 'Exception:再中二的少年，总有一天也会被现实打败。'

    def get_moring(self):
        '''早安!'''
        morings = ['我的小鱼你醒了，还记得清晨吗?', '昨夜你曾说过，愿夜幕永不开启', '这个点才醒?fw']
        text = random.choice(morings)
        return text

    def get_op(self):
        '''原神'''
        ops = ['你说的对，后面忘了','原神怎么你了?','原神国产三A大作，谁喷谁罕见!','我超','你说对，但原神，米自研，冒险游，提瓦特，神选中，授神眼，引元素。扮角色，邂同伴，击强敌，掘真相。']
        text = random.choice(ops)
        return text
