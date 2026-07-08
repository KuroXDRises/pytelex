class MessageHandler:
    def __init__(self, callback, condition):
        self.type= 'message'
        self.callback = callback
        self.condition = condition
    def check(self, update):
        return 'message' in update