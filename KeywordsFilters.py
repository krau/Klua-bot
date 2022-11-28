from telegram.ext.filters import MessageFilter


class FilterSetu(MessageFilter):
    '''色图'''

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
