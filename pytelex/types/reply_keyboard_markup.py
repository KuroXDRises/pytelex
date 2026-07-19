from .object import Object
from .keyboard_button import KeyboardButton


class ReplyKeyboardMarkup(Object):
    def __init__(
        self,
        keyboard: list[list[KeyboardButton]],
        resize_keyboard: bool = None,
        one_time_keyboard: bool = None,
        selective: bool = None,
        is_persistent: bool = None,
        input_field_placeholder: str = None
    ):
        super().__init__(None)

        self.keyboard = keyboard
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.selective = selective
        self.is_persistent = is_persistent
        self.input_field_placeholder = input_field_placeholder

    def write(self):
        return {
            "keyboard": [
                [
                    button.write()
                    for button in row
                ]
                for row in self.keyboard
            ],
            **{
                k: v
                for k, v in {
                    "resize_keyboard": self.resize_keyboard,
                    "one_time_keyboard": self.one_time_keyboard,
                    "selective": self.selective,
                    "is_persistent": self.is_persistent,
                    "input_field_placeholder": self.input_field_placeholder
                }.items()
                if v is not None
            }
        }