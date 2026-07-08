# pytelex/methods/file/base.py


from ..base import BaseMethod
from ._download import Download
from ._getfile import GetFile


class FileMethod(
    BaseMethod,
    GetFile,
    Download
):
    pass