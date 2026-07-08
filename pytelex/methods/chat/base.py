# pytelex/methods/chat/base.py

from ..base import BaseMethod
from ._getchat import GetChat
from ._banchatmember import BanChatMember
from ._unbanchatmember import UnbanChatMember
from ._restrictchatmember import RestrictChatMember
from ._promotechatmember import PromoteChatMember
from ._setchatadministratorcustomtitle import SetChatAdministratorCustomTitle
from ._bansenderchat import BanSenderChat
from ._unbansenderchat import UnbanSenderChat
from ._approvechatjoinrequest import ApproveChatJoinRequest
from ._declinechatjoinrequest import DeclineChatJoinRequest
from ._exportchatinvitelink import ExportChatInviteLink
from ._createchatinvitelink import CreateChatInviteLink
from ._revokechatinvitelink import RevokeChatInviteLink
from ._pinchatmessage import PinChatMessage
from ._unpinchatmessage import UnpinChatMessage
from ._unpinallchatmessages import UnpinAllChatMessages



class ChatMethod(
    BaseMethod,
    GetChat,
    BanChatMember,
    UnbanChatMember,
    RestrictChatMember,
    PromoteChatMember,
    SetChatAdministratorCustomTitle,
    BanSenderChat,
    UnbanSenderChat,
    ApproveChatJoinRequest,
    DeclineChatJoinRequest,
    ExportChatInviteLink,
    CreateChatInviteLink,
    RevokeChatInviteLink,
    PinChatMessage,
    UnpinAllChatMessages,
    UnpinChatMessage
):
    pass