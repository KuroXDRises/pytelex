# pytelex/methods/base.py

import os

from ..errors import BadRequest
from ..errors import Forbidden
from ..errors import TelegramError


class BaseMethod:
    async def _invoke(self, method: str, payload: dict = None):
        payload = {
            k: v
            for k, v in (payload or {}).items()
            if v is not None
        }

        payload = self._serialize(payload)
        
        response = await self.request.post(
            method=method,
            json=payload
        )

        if not response.get("ok"):
            code = response.get("error_code", 0)
            description = response.get("description", "Unknown error")

            if code == 400:
                raise BadRequest(description)
            elif code == 403:
                raise Forbidden(description)
            else:
                raise TelegramError(description)

        return response["result"]

    async def _upload(
        self,
        method: str,
        data: dict = None,
        files: dict = None
    ):
        data = {
            k: v
            for k, v in (data or {}).items()
            if v is not None
        }

        response = await self.request.upload(
            method=method,
            data=data,
            files=files or {}
        )

        if not response.get("ok"):
            code = response.get("error_code", 0)
            description = response.get("description", "Unknown error")

            if code == 400:
                raise BadRequest(description)
            elif code == 403:
                raise Forbidden(description)
            else:
                raise TelegramError(description)

        return response["result"]

    def _resolve_media(self, media, field: str):
        if not isinstance(media, str):
            return None, {field: media}, False

        if media.startswith(("http://", "https://")):
            return media, None, False

        if os.path.isfile(media):
            return None, {field: open(media, "rb")}, True

        return media, None, False

    def _serialize(self, value):
        if hasattr(value, "write"):
            return value.write()
    
        if isinstance(value, list):
            return [self._serialize(i) for i in value]
    
        if isinstance(value, dict):
            return {
                k: self._serialize(v)
                for k, v in value.items()
            }
    
        return value