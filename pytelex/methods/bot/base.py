# pytelex/methods/bot/base.py

from ..base import BaseMethod
from ._getme import GetMe

class BotMethod(
    BaseMethod,
    GetMe
):
    pass