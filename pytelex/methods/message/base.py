# pytelex/method/message/base.py

from ..base import BaseMethod
from ._sendmessage import SendMessage
from ._copymessage import CopyMessage
from ._forwardmessage import ForwardMessage
from ._deletemessage import DeleteMessage
from ._editmessagetext import EditMessageText


class MessageMethod(
    BaseMethod,
    SendMessage,
    CopyMessage,
    ForwardMessage,
    DeleteMessage,
    EditMessageText
):
    pass