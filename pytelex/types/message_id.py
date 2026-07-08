# pytelex/types/message_id.py

from .object import Object


class MessageId(Object):
    def __init__(
        self,
        *,
        client=None,
        message_id:int=None
    ):
        super().__init__(client)
        self.message_id = message_id

    @classmethod
    def _parse(cls, client, data:dict):
        if not data:
            return None
        return cls(
            client=client,
            message_id=data.get('message_id')
        )