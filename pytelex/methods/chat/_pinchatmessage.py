# pytelex/methods/chat/_pinchatmessage.py


class PinChatMessage:
    async def pin_chat_message(
        self,
        chat_id: int,
        message_id: int,
        disable_notification: bool | None = None,
    ) -> bool:
        result = await self._invoke("pinChatMessage", {
            "chat_id":              chat_id,
            "message_id":           message_id,
            "disable_notification": disable_notification,
        })
        return result