# pytelex/methods/chat/_getchat.py

import pytelex


class GetChat:
    async def get_chat(
        self:'pytelex.TeleClient',
        chat_id:int
    ):
        result = await self._invoke(
            method='getChat',
            payload={
                'chat_id':chat_id
            }
        )
        return pytelex.types.Chat._parse(
            self,
            result
        )