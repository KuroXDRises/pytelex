# pytelex/methods/chat/_bansenderchat.py


class BanSenderChat:
    async def ban_sender_chat(
        self,
        chat_id: int,
        sender_chat_id: int,
    ) -> bool:
        result = await self._invoke("banChatSenderChat", {
            "chat_id":        chat_id,
            "sender_chat_id": sender_chat_id,
        })
        return result