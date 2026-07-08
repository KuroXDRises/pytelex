# pytelex/methods/message/_sendmessage.py

from ...errors import BadRequest
from ...types.message import Message

class SendMessage:
    async def send_message(
        self,
        chat_id: int | str,
        text: str,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
        parse_mode: str | None = None,
        entities: list | None = None,
        link_preview_options: dict | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        reply_parameters: dict | None = None,
        reply_markup=None,
    ) -> "Message":
        if hasattr(reply_markup, 'write'):
            reply_markup.write()
        result = await self._invoke("sendMessage", {
            "chat_id": chat_id,
            "text": text,
            "business_connection_id": business_connection_id,
            "message_thread_id": message_thread_id,
            "parse_mode": parse_mode,
            "entities": entities,
            "link_preview_options": link_preview_options,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "allow_paid_broadcast": allow_paid_broadcast,
            "message_effect_id": message_effect_id,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
        })
        return Message._parse(self, result)