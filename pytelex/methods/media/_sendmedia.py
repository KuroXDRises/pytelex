# pytelex/methods/message/_sendmedia.py

from ...errors import BadRequest
from ...types import Message


class SendMedia:
    async def send_media(
        self,
        media_type: str,
        media,
        chat_id: int | str,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities=None,
        disable_notification: bool = False,
        protect_content: bool = False,
        reply_parameters=None,
        reply_markup=None,
        **extra_kwargs
    ):
        method = f"send{media_type.capitalize()}"
        field = media_type
    
        data, files, owned = self._resolve_media(
            media=media,
            field=field
        )
    
        payload = {
            "chat_id": chat_id,
            "caption": caption,
            "parse_mode": parse_mode,
            "caption_entities": caption_entities,
            "disable_notification": disable_notification,
            "protect_content": protect_content,
            "reply_parameters": reply_parameters,
            "reply_markup": reply_markup,
            **extra_kwargs,  # duration, width, height, etc — type specific extras
        }
    
        if data:
            payload[field] = data
    
        try:
            if files is not None:
                result = await self._upload(
                    method=method,
                    data=payload,
                    files=files
                )
            else:
                result = await self._invoke(
                    method=method,
                    payload=payload
                )
        finally:
            if owned and files:
                files[field].close()
    
        return Message._parse(self, result)