# pytelex/methods/chat/_unbanchatmember.py


class UnbanChatMember:
    async def unban_chat_member(
        self,
        chat_id: int,
        user_id: int,
        only_if_banned: bool | None = None,
    ) -> bool:
        result = await self._invoke("unbanChatMember", {
            "chat_id":        chat_id,
            "user_id":        user_id,
            "only_if_banned": only_if_banned,
        })
        return result