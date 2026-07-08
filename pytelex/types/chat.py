# pytelex/types/chat.py

from .object import Object


class Chat(Object):
    def __init__(
        self,
        *,
        client=None,
        id:int=None,
        title:str=None,
        type:str=None,
        username:str=None,
        first_name:str=None,
        last_name:str=None
    ):
        super().__init__(client)
        self.id = id
        self.type = type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def _parse(cls, client, data:dict):
        if not data:
            return None
        return cls(
            client=client,
            id=data.get('id'),
            type=data.get('type'),
            title=data.get('title'),
            username=data.get('username'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name')
        )