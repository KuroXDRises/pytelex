# pytelex/methods/media/base.py

from ..base import BaseMethod
from ._sendmedia import SendMedia
from ._editmessagecaption import EditMessageCaption


class MediaMethod(
    BaseMethod,
    SendMedia,
    EditMessageCaption
):
    pass