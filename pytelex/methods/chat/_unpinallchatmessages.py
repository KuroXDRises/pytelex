# pytelex/methods/chat/_unpinallchatmessages.py



class UnpinAllChatMessages:
    async def unpin_all_chat_messages(
        self,
        chat_id: int,
    ) -> bool:
        result = await self._invoke("unpinAllChatMessages", {
            "chat_id": chat_id,
        })
        return result
