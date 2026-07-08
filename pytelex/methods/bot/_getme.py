# pytelex/methods/bot/_getme.py

import pytelex

class GetMe:
    async def get_me(self:'pytelex:TeleClient'):
        response = await self._invoke("getMe")
        return pytelex.types.User._parse(self, response)
