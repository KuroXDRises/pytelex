from .request import Request
from .types.user import User
from .handlers.message import MessageHandler
from .dispatcher import Dispatcher
from .types import Message
from .types import Chat
from .types.input_file import InputFile
from .conditions import Conditions
from .methods.client import ClientMethod
from .errors import BadRequest, Forbidden, TelegramError
import asyncio
import os



class TeleClient(ClientMethod):
esr        self.token = token
        self.request = Request(self.token)
        self.offset = 0
        self.handlers = []
        self.dispatcher = Dispatcher(self)

    async def start(self):
        await self.request.start()

    async def stop(self):
        await self.request.stop()

    async def _run(self):
        await self.start()
        try:
            await self._polling()
        finally:
            await self.stop()

    def run(self):
        asyncio.run(self._run())

    async def _polling(self):
        while True:
            updates = await self.request.post(
                "getUpdates",
                {
                    "offset": self.offset,
                    "timeout": 30,
                },
            )
            if not updates["ok"]:
                continue
            for update in updates["result"]:
                self.offset = update["update_id"] + 1
                await self.dispatcher.dispatch(update)

    def add_handler(self, handler):
        self.handlers.append(handler)

    def message_handler(self, condition=Conditions.All):
        def decorator(func):
            handler = MessageHandler(func, condition)
            self.add_handler(handler)
            return func
        return decorator