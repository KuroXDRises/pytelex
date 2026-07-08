from .enums import ChatType

class Condition:
    def check(self, message):
        return True
    def __and__(self, other):
        return AndCondition(self, other)
    def __or__(self, other):
        return OrCondition(self, other)
    def __invert__(self):
        return NotCondition(self)

# Operator Overloading
class AndCondition(Condition):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def check(self, m):
        return (self.left.check(m) and self.right.check(m))

class OrCondition(Condition):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def check(self, m):
        return (self.left.check(m) or self.right.check(m))

class NotCondition(Condition):
    def __init__(self, condition):
        self.condition = condition
    def check(self, m):
        return not self.condition.check(m)

# All Conditions
class AlwaysCondition(Condition):
    def check(self, m):
        return True

# Text Condition
class TextCondition(Condition):
    def check(self, m):
        if m.text is None:
            return False
        if m.text.startswith("/"):
            return False
        return True      

# Command Condition
class CommandCondition(Condition):
    def __init__(self, commands: str | list[str]):
        if isinstance(commands, str):
            self.commands = [commands.lower()]
        else:
            self.commands = [cmd.lower() for cmd in commands]
    def check(self, m):
        if m.text is None:
            return False
        if not m.text.startswith("/"):
            return False
        command = m.text.split()[0][1:]
        if "@" in command:
            command = command.split("@")[0]
        return command.lower() in self.commands

# Reply Condition
class ReplyCondition(Condition):
    def check(self, m):
        return m.reply_to is not None

# Chat Conditions
class GroupCondition(Condition):
    def check(self, m):
        return m.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP)

class PrivateCondition(Condition):
    def check(self, m):
        return m.chat.type == ChatType.PRIVATE

class ChannelCondition(Condition):
    def check(self, m):
        return m.chat.type == ChatType.CHANNEL

# Allow User Condition
class UserCondition(Condition):
    def __init__(self, users:list[int]|int):
        if isinstance(users, int):
            self.users = [users]
        else:
            self.users = [int(user) for user in users]
    def check(self, m):
        if m.from_user is None:
            return False
        return m.from_user.id in self.users

# Media Conditions
class PhotoCondition(Condition):
    def check(self, m):
        return m.photo is not None

class VideoCondition(Condition):
    def check(self, m):
        return m.video is not None

class VoiceCondition(Condition):
    def check(self, m):
        return m.voice is not None

class AudioCondition(Condition):
    def check(self, m):
        return m.audio is not None

class DocumentCondition(Condition):
    def check(self, m):
        return m.document is not None

class StickerCondition(Condition):
    def check(self, m):
        return m.sticker is not None

class AnimationCondition(Condition):
    def check(self, m):
        return m.animation is not None

# Bot or Human Conditions
class BotCondition(Condition):
    def check(self, m):
        if not m.from_user:
            return False
        if not m.from_user.isBot:
            return False
        return True

class HumanCondition(Condition):
    def check(self, m):
        if not m.from_user:
            return False
        if m.from_user.isBot:
            return False
        return True

# Chat Admin
class AdminOnly(Condition):
    def check(self, m):
        admins = m.chat.get_administrators()
        return m.from_user.id in admins

# Conditions Class (that developers use)
class Conditions:
    All = AlwaysCondition()
    Text = TextCondition()
    Photo = PhotoCondition()
    Reply = ReplyCondition()
    Private = PrivateCondition()
    Group = GroupCondition()
    Video = VideoCondition()
    Voice = VoiceCondition()
    Audio = AudioCondition()
    Document = DocumentCondition()
    Sticker = StickerCondition()
    Animation = AnimationCondition()
    Bot = BotCondition()
    Human = HumanCondition()
    ChatAdmin = AdminOnly()
    
    @staticmethod
    def Command(commands:str|list[str]):
        return CommandCondition(commands=commands)

    @staticmethod
    def Users(users:int|list[int]):
        return UserCondition(users=users)