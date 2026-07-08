# pytelex/types/inline_keyboard_button.py

from .object import Object

class InlineKeyboardButton(Object):
    def __init__(
        self,
        *,
        text:str,
        callback_data:str=None,
        url:str=None,
        style='default',
        web_app=None,
        login_url=None,
        switch_inline_query=None,
        switch_inline_query_current_chat=None,
        callback_game=None,
        pay:bool=None
    ):
        super().__init__(None)
        self.text = text
        self.callback_data = callback_data
        self.url = url
        self.style = style
        self.web_app = web_app
        self.login_url = login_url
        self.switch_inline_query = switch_inline_query
        self.switch_inline_query_current_chat = switch_inline_query_current_chat
        self.callback_game = callback_game
        self.pay = pay

    def write(self):
        return {
           k:  (
               v.write()
               if hasattr(v, 'write')
               else v
           )
            for k, v in self.__dict__.items()
            if v is not None and not k.startswith('_')
        }