# pytelex/methods/client.py

from .bot.base import BotMethod
from .chat.base import ChatMethod
from .message.base import MessageMethod
from .media.base import MediaMethod
from .user.base import UserMethod
from .admin.base import AdminMethod


class ClientMethod(
    BotMethod,
    ChatMethod,
    MediaMethod,
    MessageMethod,
    UserMethod,
    AdminMethod
):
    pass