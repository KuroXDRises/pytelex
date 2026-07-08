# pytelex/methods/message/_copymessage.py


from ...types import MessageId


class CopyMessage:
    async def copy_message(
        self,
        chat_id:int,
        from_chat_id:int,
        message_id:int
    ):
        result = await self._invoke(
            method='copyMessage',
            payload={
                'chat_id':chat_id,
                'from_chat_id':from_chat_id,
                'message_id':message_id
            }
        )
        return MessageId._parse(self, result)