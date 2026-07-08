# pytelex/types/inline_keyboard_markup.py

from typing import List
from .object import Object
from .inline_keyboard_button import InlineKeyboardButton


class InlineKeyboardMarkup(Object):
    def __init__(
        self,
        inline_keyboard:List[List[InlineKeyboardButton]]
    ):
        super().__init__(None)
        self.inline_keyboard = inline_keyboard

    def write(self):
        return {
            'inline_keyboard': [
                [
                    button.write()
                    for button in row
                ]
                for row in self.inline_keyboard
            ]
        }