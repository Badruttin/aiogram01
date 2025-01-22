from aiogram.types import   (ReplyKeyboardMarkup, KeyboardButton, 
                            InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],
                                     [KeyboardButton(text='Корзина')],
                                     [KeyboardButton(text='Контакты'),
                                     KeyboardButton(text='О нас')]
                                     ],
                                     
                                     resize_keyboard=True,
                                     input_field_placeholder='Выберите пункт меню')

catalog = InlineKeyboardMarkup