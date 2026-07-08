# pytelex/methods/chat/_exportchatinvitelink.py


class ExportChatInviteLink:
    async def export_chat_invite_link(
        self,
        chat_id: int,
    ) -> str:
        result = await self._invoke("exportChatInviteLink", {
            "chat_id": chat_id,
        })
        return result