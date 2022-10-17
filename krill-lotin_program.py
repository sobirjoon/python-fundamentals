# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 17:52:22 2022

@author: sobirjon
"""қ

from transliterate import to_cyrillic, to_latin 
import telebot

TOKEN = '5555225644:AAHH0Ik9JIpZdt0qVFSQDFzfjr8HYQxosjQ'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    response = "Ассалом алейкум! Хуш келибсиз!"
    response += "\nМатн киритинг:"
    bot.reply_to(message, response)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    msg = message.text
    response = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)   
    # if msg.isascii():
    #     response = to_cyrillic(msg)
    # else:
    #     response = to_latin(msg)
    bot.reply_to(message, response(msg))

bot.polling()
    
#     # 5555225644:AAHH0Ik9JIpZdt0qVFSQDFzfjr8HYQxosjQ