# pytelex/types/photo_size.py


from .object import Object


class PhotoSize(Object):
    def __init__(
        self,
        *,
        client=None,
        file_id=None,
        file_unique_id=None,
        height=None,
        width=None,
        file_size=None
    ):
        super().__init__(client)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.height = height
        self.width = width
        self.file_size = file_size

    @classmethod
    def _parse(cls, client, data:dict):
        if not data:
            return None
        return cls(
            client=client,
            file_id=data.get('file_id'),
            file_unique_id=data.get('file_unique_id'),
            height=data.get('height'),
            width=data.get('width'),
            file_size=data.get('file_size')
        )