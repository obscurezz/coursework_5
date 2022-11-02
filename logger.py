from decorator import singleton


@singleton
class Logger:
    """
    Log messages from players activities to a singleton
    """
    def __init__(self) -> None:
        self.messages: list[str] = []

    def add_message(self, message_text: str) -> None:
        """
        :param message_text: text of message
        :return: None
        """
        self.messages.append(message_text)

    def clear_all_messages(self) -> None:
        """
        :return: None, just clears previous message
        """
        self.messages.clear()

    def get_message(self) -> str:
        """
        :return: message output
        """
        message: str = '\n'.join(self.messages)
        self.clear_all_messages()
        return message
