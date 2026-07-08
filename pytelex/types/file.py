# pytelex/types/file.py

from .object import Object


class File(Object):
    def __init__(
        self,
        *,
        client=None,
        file_id=None,
        file_unique_id=None,
        file_size=None,
        file_path=None
    ):
        super().__init__(client)
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.file_path = file_path
        self.file_size = file_size

    @classmethod
    def _parse(cls, client, data: dict):
        if not data:
            return None
        return cls(
            client=client,
            file_id=data.get("file_id"),
            file_unique_id=data.get("file_unique_id"),
            file_path=data.get("file_path"),
            file_size=data.get("file_size")
        )
