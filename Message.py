from datetime import datetime

class Message:
    def __init__(self, sender_name = None, timestamp_ms = None, content = None, message_type = None):
        """
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
    
    def __str__(self):
        return '{}\n{}\n{}\n{}\n'.format(self.sender_name, self.timestamp_ms, self.content, self.message_type)

if __name__ == '__main__':
    ts = 1579017491983
    
    m = Message(
        'Kenneth CK', 
        datetime.fromtimestamp(ts/1000.0), 
        "I\u00e2\u0080\u0099ll maneuver the Gas and brakes and you\u00e2\u0080\u0099ll steer", 
        "Generic"
    )
    print(m)
    