from aiogram.types import ReplyKeyboardMarkup, KeyboardButton 

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Sherik kerak'),
            KeyboardButton(text='Ish joyi kerak'),
        ],
        [
            
            KeyboardButton(text='Hodim kerak'),
            KeyboardButton(text='Ustoz kerak'),
        ],
        [
            KeyboardButton(text='Shogird')
        ]
    ],
    resize_keyboard=True
)