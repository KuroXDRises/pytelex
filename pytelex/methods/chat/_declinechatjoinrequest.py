# pytelex/methods/chat/_declinechatjoinrequest.py


class DeclineChatJoinRequest:
    async def decline_chat_join_request(
        self,
        chat_id: int,
        user_id: int,
    ) -> bool:
        result = await self._invoke("declineChatJoinRequest", {
            "chat_id": chat_id,
            "user_id": user_id,
        })
        return result