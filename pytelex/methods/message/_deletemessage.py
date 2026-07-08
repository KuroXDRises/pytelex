# pytelex/methods/message/_deletemessage.py

from ...types import Message

class DeleteMessage:
    async def delete_message(self, chat_id: str | int, message_id: int) -> bool:
        result = await self._invoke("deleteMessage", {
            "chat_id": chat_id,
            "message_id": message_id,
        })
        return bool(result)