# pytelex/methods/chat/_unbansenderchat.py


class UnbanSenderChat:
    async def unban_sender_chat(
        self,
        chat_id: int,
        sender_chat_id: int,
    ) -> bool:
        result = await self._invoke("unbanChatSenderChat", {
            "chat_id":        chat_id,
            "sender_chat_id": sender_chat_id,
        })
        return result