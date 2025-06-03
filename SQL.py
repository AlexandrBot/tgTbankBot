import telebot
from telebot import types

bot = telebot.TeleBot('8119411434:AAF_Zv12JKBDIAwDEavO2KLq2ri6IOh7PEw')

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton(text='популярный вопрос 1', callback_data='1')
    but2 = types.InlineKeyboardButton(text='популярный вопрос 2', callback_data='2')
    but3 = types.InlineKeyboardButton(text='популярный вопрос 3', callback_data='3')
    but4 = types.InlineKeyboardButton(text='популярный вопрос 4', callback_data='4')
    but5 = types.InlineKeyboardButton(text='популярный вопрос 5', callback_data='5')
    but6 = types.InlineKeyboardButton(text='популярный вопрос 6', callback_data='6')
    but7 = types.InlineKeyboardButton(text='популярный вопрос 7', callback_data='7')
    keyboard.add(but1, but2, but3, but4, but5, but6,but7)
    bot.send_message(message.chat.id, 'Привет, я имитирую бота тинькова тут появятся типо популярные вопросы', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.data =='1':
        bot.send_message(call.message.chat.id, 'Ответ на вопрос номер 1')
    if call.data =='2':
        bot.send_message(call.message.chat.id, 'Ответ на вопрос номер 2')
    if call.data =='3':
        bot.send_message(call.message.chat.id, 'Ответ на вопрос номер 3')
    if call.data =='4':
        bot.send_message(call.message.chat.id, 'Ответ на вопрос номер 4')
    if call.data =='5':
        bot.send_message(call.message.chat.id, 'Ответ на вопрос номер 5')
    if call.data =='6':
        bot.send_message(call.message.chat.id, 'Ответ на вопрос номер 6')
    if call.data =='7':
        bot.send_message(call.message.chat.id, 'Ответ на вопрос номер 7')


bot.infinity_polling()