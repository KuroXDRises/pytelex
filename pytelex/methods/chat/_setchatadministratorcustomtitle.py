# pytelex/methods/chat/_setchatadministratorcustomtitle.py


class SetChatAdministratorCustomTitle:
    async def set_chat_administrator_custom_title(
        self,
        chat_id: int,
        user_id: int,
        custom_title: str,
    ) -> bool:
        result = await self._invoke("setChatAdministratorCustomTitle", {
            "chat_id":      chat_id,
            "user_id":      user_id,
            "custom_title": custom_title,
        })
        return result