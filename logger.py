from decorator import singleton


@singleton
class Logger:
    def __init__(self):
        self.messages: list[str] = []

    def add_message(self, message_text: str) -> None:
        self.messages.append(message_text)

    def clear_all_messages(self) -> None:
        self.messages.clear()

    def get_message(self) -> str:
        message = '\n'.join(self.messages)
        self.clear_all_messages()
        return message
