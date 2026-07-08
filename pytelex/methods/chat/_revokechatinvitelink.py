# pytelex/methods/chat/_revokechatinvitelink.py


class RevokeChatInviteLink:
    async def revoke_chat_invite_link(
        self,
        chat_id: int,
        invite_link: str,
    ) -> dict:
        result = await self._invoke("revokeChatInviteLink", {
            "chat_id":     chat_id,
            "invite_link": invite_link,
        })
        return result