from .object import Object


class KeyboardButton(Object):
    def __init__(
        self,
        text: str,
        request_contact: bool = None,
        request_location: bool = None,
        request_poll=None,
        web_app=None
    ):
        super().__init__(None)

        self.text = text
        self.request_contact = request_contact
        self.request_location = request_location
        self.request_poll = request_poll
        self.web_app = web_app

    def write(self):
        return {
            k: (
                v.write()
                if hasattr(v, "write")
                else v
            )
            for k, v in self.__dict__.items()
            if not k.startswith("_") and v is not None
        }