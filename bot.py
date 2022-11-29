import os
import logging
import telegram
import yaml
import random
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CommandHandler

from Setu import Setu
from Words import Words
from KeywordsFilters import *
from Helper import Helper

'''初始化helper类'''
helper = Helper()

'''读取与设定配置'''
config = helper.read_config('config.yml')

TOKEN = config['token']
API = config['api']
if config['proxy'] != None:
    os.environ['http_proxy'] = config['proxy']
    os.environ['https_proxy'] = config['proxy']
#概率设置
pr_sese = config['pr_sese']
pr_henan = config['pr_henan']
pr_op = config['pr_op']
pr_sleep = config['pr_sleep']
pr_morning = config['pr_morning']
pr_niubi = config['pr_niubi']
pr_aoligei = config['pr_aoligei']

'''初始化类'''
setu = Setu(API)
words = Words(API)

'''bot方法'''


def start(update: Update, context: CallbackContext):
    '''/start'''
    context.bot.send_message(chat_id=update.effective_chat.id, text="你干嘛~")


def sese(update: Update, context: CallbackContext):
    '''涩图'''
    if helper.random_unit(pr_sese):
        setu_url = setu.get_setu_url()
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=setu_url)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,text='不许导!积回去!')

def henan(update: Update, context: CallbackContext):
    '''河南怎么你了'''
    texts = ['河南怎么你了?', '河南?', '你井盖马上就没!']
    if helper.random_unit(pr_henan):
        text = random.choice(texts)
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def words_op(update: Update, context: CallbackContext):
    '''OP!'''
    if helper.random_unit(pr_op):
        text = words.get_op()
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def words_sleep(update: Update, context: CallbackContext):
    '''晚安'''
    if helper.random_unit(pr_sleep):
        text = words.get_wanan()
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def words_morning(update: Update, context: CallbackContext):
    if helper.random_unit(pr_morning):
        text = words.get_moring()
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        context.bot.send_photo(chat_id=update.effective_chat.id,
                            photo='https://telegraph-image.pages.dev/file/f600e072974769d3aa66c.png')


def words_niubi(update: Update, context: CallbackContext):
    '''随机装牛逼'''
    if helper.random_unit(pr_niubi):
        text = words.get_niubi()
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    else:
        texts = ['嗯?', '哈?', '私は高性能です~']
        text = random.choice(texts)
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def words_aoligei(update: Update, context: CallbackContext):
    '''随机正能量'''
    if helper.random_unit(pr_aoligei):
        text = words.get_aoligei()
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def words_young(update: Update, context: CallbackContext):
    '''大老师语录'''
    text = words.get_young()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def main():
    '''主函数'''
    # 初始化
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    bot = telegram.Bot(token=TOKEN)

    '''初始化过滤器类'''
    setu_filter = FilterSetu()
    henan_filter = FilterHenan()
    sleep_filter = FilterSleep()
    niubi_filer = FilterNiubi()
    moring_filter = FilterMoring()
    aoligei_filter = FilterAoligei()
    op_filter = FilterOp()

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    '''handlers'''
    start_handler = CommandHandler('start', start)
    setu_handler = CommandHandler('setu', sese)
    young_handler = CommandHandler('young', words_young)
    setu_ncmd_handler = MessageHandler(setu_filter & (~Filters.command), sese)
    henan_handler = MessageHandler(henan_filter, henan)
    sleep_handler = MessageHandler(sleep_filter, words_sleep)
    niubi_handler = MessageHandler(niubi_filer, words_niubi)
    moring_handler = MessageHandler(moring_filter, words_morning)
    aoligei_handler = MessageHandler(aoligei_filter, words_aoligei)
    op_handler = MessageHandler(op_filter, words_op)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(setu_handler)
    dispatcher.add_handler(young_handler)
    dispatcher.add_handler(setu_ncmd_handler)
    dispatcher.add_handler(henan_handler)
    dispatcher.add_handler(sleep_handler)
    dispatcher.add_handler(niubi_handler)
    dispatcher.add_handler(moring_handler)
    dispatcher.add_handler(aoligei_handler)
    dispatcher.add_handler(op_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
