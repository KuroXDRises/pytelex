class MetagramError(Exception):
    pass

class ClientNotStarted(MetagramError):
    pass

class TelegramError(Exception):
    pass

class Forbidden(TelegramError):
    pass

class BadRequest(TelegramError):
    pass