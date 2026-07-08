import httpx
from .errors import ClientNotStarted

class Request:
    def __init__(self, token: str):
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{token}"
        self.http: httpx.AsyncClient | None = None

    async def start(self):
        if self.http is not None:
            return
        timeout = httpx.Timeout(
            connect=10.0,
            read=60.0,
            write=60.0,
            pool=10.0
        )
        self.http = httpx.AsyncClient(
            timeout=timeout
        )

    async def stop(self):
        if self.http is None:
            return
        await self.http.aclose()
        self.http = None

    async def post(self, method: str, json: dict | None = None):
        if self.http is None:
            raise ClientNotStarted("Request Client has not been started.")    
        url = f"{self.base_url}/{method}"    
        response = await self.http.post(
            url=url,
            json=json
        )    
        data = response.json()    
        return data

    async def upload(self, method: str, data: dict, files: dict, retries: int = 2):
        if self.http is None:
            raise ClientNotStarted('Request Client has not been started.')
        url = f"{self.base_url}/{method}"
        response = await self.http.post(
            url=url,
            data=data,
            files=files
        )
        return response.json()

    async def download(self, url: str):
        if self.http is None:
            raise ClientNotStarted(
                "Request Client has not been started."
            )
        response = await self.http.get(url)
        response.raise_for_status()
        return response.content