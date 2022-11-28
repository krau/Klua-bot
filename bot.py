import os
import logging
import telegram
import yaml
import random
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CommandHandler

from Setu import Setu
from KeywordsFilters import *

configpath = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), 'config.yml')
with open(configpath, 'r', encoding='utf-8') as f:
    config = f.read()
config = yaml.load(config, Loader=yaml.FullLoader)

TOKEN = config['token']
SETUAPI = config['setuapi']
if config['proxy'] != None:
    os.environ['http_proxy'] = config['proxy']
    os.environ['https_proxy'] = config['proxy']


def start(update: Update, context: CallbackContext):
    '''/start'''
    context.bot.send_message(chat_id=update.effective_chat.id, text="你干嘛~")


def setu(update: Update, context: CallbackContext):
    '''涩图'''
    setu = Setu(SETUAPI)
    setu_url = setu.get_setu_url()
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=setu_url)


def henan(update: Update, context: CallbackContext):
    '''河南怎么你了'''
    texts = ['河南怎么你了?', '河南?']
    text = random.choice(texts)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def main():
    '''主函数'''
    # 初始化
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    bot = telegram.Bot(token=TOKEN)

    # 过滤器
    setu_filter = FilterSetu()
    henan_filter = FilterHenan()

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    # handlers
    start_handler = CommandHandler('start', start)
    setu_handler = CommandHandler('setu', setu)
    setu_ncmd_handler = MessageHandler(setu_filter & (~Filters.command), setu)
    henan_handler = MessageHandler(henan_filter, henan)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(setu_handler)
    dispatcher.add_handler(setu_ncmd_handler)
    dispatcher.add_handler(henan_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
