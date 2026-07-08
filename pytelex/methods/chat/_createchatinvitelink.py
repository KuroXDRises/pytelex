# pyetelex/methods/chat/_createchatinvitelink.py


class CreateChatInviteLink:
    async def create_chat_invite_link(
        self,
        chat_id: int,
        name: str | None = None,
        expire_date: int | None = None,
        member_limit: int | None = None,
        creates_join_request: bool | None = None,
    ) -> dict:
        result = await self._invoke("createChatInviteLink", {
            "chat_id":              chat_id,
            "name":                 name,
            "expire_date":          expire_date,
            "member_limit":         member_limit,
            "creates_join_request": creates_join_request,
        })
        return result