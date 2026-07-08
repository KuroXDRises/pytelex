# pytelex/methods/message/_forwardmessage.py


from ...types import Message

class ForwardMessage:
    async def forward_message(
        self,
        chat_id:int,
        from_chat_id:int,
        message_id:int
    ):
        result = await self._invoke(
            methods='forwardMessage',
            payload={
                'chat_id':chat_id,
                'from_chat_id':from_chat_id,
                'message_id':message_id
            }
        )
        return Message._parse(self, result)