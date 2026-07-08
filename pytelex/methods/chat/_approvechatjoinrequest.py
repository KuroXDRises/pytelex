# pytelex/methods/chat/_approvechatjoinrequest.py


class ApproveChatJoinRequest:
    async def approve_chat_join_request(
        self,
        chat_id: int,
        user_id: int,
    ) -> bool:
        result = await self._invoke("approveChatJoinRequest", {
            "chat_id": chat_id,
            "user_id": user_id,
        })
        return result