class Message:
    def __init__(self, sender_name = None, timestamp_ms = None, content = None, message_type = None):
        """
        hi

        sender_name - name of sender
        timestamp_ms - time message was sent
        content - content of message
        message_type - type of message
        """

        self.sender_name = sender_name
        self.timestamp_ms = timestamp_ms
        self.content = content
        self.message_type = message_type

        # TODO: implement
        self.sticker = None
        self.files = None
        self.gifs = None
        self.share = None
        self.photos = None
        self.reactions = None

if __name__ == '__main__':
    pass