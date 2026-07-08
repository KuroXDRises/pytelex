# pytelex/methods/message/_editmessagetext.py

from ...types import Message


class EditMessageText:
    async def edit_message_text(
            self,
            chat_id: str | int,
            message_id: int,
            text: str,
            parse_mode: str | None = None,
            entities: list | None = None,
            link_preview_options=None,
            reply_markup=None,
        ) -> "Message":
            result = await self._invoke("editMessageText", {
                "chat_id": chat_id,
                "message_id": message_id,
                "text": text,
                "parse_mode": parse_mode,
                "entities": entities,
                "link_preview_options": link_preview_options,
                "reply_markup": reply_markup,
            })
            return Message._parse(self, result)