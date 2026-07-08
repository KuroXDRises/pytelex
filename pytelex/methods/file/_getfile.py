# pytelex/methods/file/_getfile.py


from ...types import File


class GetFile:
    async def get_file(
        self,
        file_id:str
    ) -> File:
        result = await self._invoke(
            method="getFile",
            payload={
                "file_id":file_id
            }
        )
        return File._parse(self, result)