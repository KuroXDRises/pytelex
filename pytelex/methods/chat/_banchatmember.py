# pytelex/methods/chat/_banchatmember.py


class BanChatMember:
    async def ban_chat_member(
        self,
        chat_id: int,
        user_id: int,
        until_date: int | None = None,
        revoke_messages: bool | None = None,
    ) -> bool:
        result = await self._invoke("banChatMember", {
            "chat_id":         chat_id,
            "user_id":         user_id,
            "until_date":      until_date,
            "revoke_messages": revoke_messages,
        })
        return result