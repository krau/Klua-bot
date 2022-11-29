from telegram.ext.filters import MessageFilter


class FilterSetu(MessageFilter):
    def filter(self, message):
        keywords = ['色图', '涩图']
        for keyword in keywords:
            try:
                if keyword in message.text:
                    return True
            except:
                return False


class FilterHenan(MessageFilter):
    def filter(self, message):
        keywords = ['河南', '荷兰']
        for keyword in keywords:
            try:
                if keyword in message.text:
                    return True
            except:
                return False


class FilterSleep(MessageFilter):
    def filter(self, message):
        keywords = ['睡觉','眠','睡了','晚安']
        for keyword in keywords:
            try:
                if keyword in message.text:
                    return True
            except:
                return False


class FilterNiubi(MessageFilter):
    def filter(self,message):
        keywords = ['bot','机器人','klua','Klua','智械']
        for keyword in keywords:
            try:
                if keyword in message.text:
                    return True
            except:
                return False


class FilterAoligei(MessageFilter):
    def filter(self,message):
        keywords = ['正能量','想死','烦死','吐了','操你妈','尼玛','nmd']
        for keyword in keywords:
            try:
                if keyword in message.text:
                    return True
            except:
                return False


class FilterMoring(MessageFilter):
    def filter(self,message):
        keywords = ['醒了','刚醒','早安']
        for keyword in keywords:
            try:
                if keyword in message.text:
                    return True
            except:
                return False


class FilterOp(MessageFilter):
    def filter(self,message):
        keywords = ['原神','OP','米哈游','op','我超']
        for keyword in keywords:
            try:
                if keyword in message.text:
                    return True
            except:
                return False