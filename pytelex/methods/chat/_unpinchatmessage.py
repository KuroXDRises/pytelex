# pytelex/methods/chat/_unpinchatmessage.py



class UnpinChatMessage:
    async def unpin_chat_message(
        self,
        chat_id: int,
        message_id: int,
    ) -> bool:
        result = await self._invoke("unpinChatMessage", {
            "chat_id":    chat_id,
            "message_id": message_id,
        })
        return result