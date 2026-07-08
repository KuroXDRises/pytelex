from .types import Message

class Dispatcher:
    def __init__(self, app):
        self.app = app
    async def dispatch(self, update):
        if "message" not in update:
            return
        message = Message._parse(self.app, update["message"])
        for handler in self.app.handlers:
            if handler.condition.check(message):
                await handler.callback(self.app, message)