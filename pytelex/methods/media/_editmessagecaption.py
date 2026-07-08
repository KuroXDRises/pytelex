# pytelex/methods/media/_editmessagecaption.py


from ...types import Message


class EditMessageCaption:
    async def edit_message_caption(
        self,
        chat_id: int,
        message_id: int,
        caption: str = None,
        parse_mode = None,
        caption_entities = None,
        reply_markup = None
    ) -> Message:

        payload = {
            "chat_id": chat_id,
            "message_id": message_id,
            "caption": caption,
            "parse_mode": parse_mode,
            "caption_entities": caption_entities,
            "reply_markup": reply_markup
        }

        result = await self._invoke(
            "editMessageCaption",
            payload
        )

        return Message._parse(self, result)