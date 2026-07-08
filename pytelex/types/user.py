# pytelex/types/user.py

from .object import Object


class User(Object):
    def __init__(
        self,
        *,
        client=None,
        id:int=None,
        first_name:str=None,
        last_name:str=None,
        username:str=None,
        language_code:str=None,
        is_bot:bool
    ):
        super().__init__(client)
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.language_code = language_code

    @classmethod
    def _parse(cls, client, data:dict):
        if not data:
            return None
        return cls(
            client=client,
            id=data.get('id'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            language_code=data.get('language_code'),
            is_bot=data.get('is_bot')
        )