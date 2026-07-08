# pytelex/methods/file/_download.py

from ...types import File

class Download:
    async def download(
        self,
        file:File|str,
        file_name=None
    ):
        if isinstance(file, str):
            file = await self.get_file(file)
        url = f"https://api.telegram.org/bot{self.token}/{file.file_path}"
        return await self.request._download(url)