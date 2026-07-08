from pathlib import Path
from typing import BinaryIO, Union


class InputFile:
    def __init__(self, file: Union[str, Path, bytes, BinaryIO], filename: str = None):
        self.file = file
        self.filename = filename

    @property
    def name(self):
        if self.filename:
            return self.filename

        if isinstance(self.file, (str, Path)):
            return Path(self.file).name

        return "file"

    def open(self):
        if isinstance(self.file, (str, Path)):
            return open(self.file, "rb")

        return self.file
