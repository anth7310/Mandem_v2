import json
from datetime import datetime
import regex
from datetime import datetime
from algorithms.unicodetoascii import unicodetoascii

# encode to UTF-8
from emoji import UNICODE_EMOJI
BYTES_EMOJI = [ emoji.encode() for emoji in list(UNICODE_EMOJI) ]


class Thread:
    def __init__(self, file_name: str):
        """
        file_name is path to file, representing json data
        """
        # load in json data as dictionary
        f = open(file_name, 'r')
        messages = f.read()
        messages_dict = json.loads(messages)
        f.close()

        self.data = messages_dict
        self.title = messages_dict['title']

        self._messages_to_ascii()
        
        self.messages_keys = self._generate_messages_keys()
    
    def _messages_to_ascii(self):
        """
        Replace all messages with non ascii characters to ascii equivalent, utf-8 encoding
        """
        def f(i, msg):
            # helper function - reassign string to byte in data object for index i
            self.data['messages'][i]['content'] = unicodetoascii(msg)

        [ f(i, x['content']) for i, x in enumerate(self.data['messages']) if 'content' in self.data['messages'][i] ]
    
    def _generate_messages_keys(self):
        """
        Returns a set containing all keys used in messages
        All messages do not have same keys
        """
        keys = set()
        for msg in self.data['messages']:
            keys = keys.union(set(msg.keys()))
        return keys

    def search(self, phrase: str) -> list:
        """
        Return a list of messages containing this phrase
        """
        results = []
        for msg in self.messages():
            if phrase in msg:
                results.append(msg)
        return results

    def messages(self) -> list:
        """
        Return messages as list
        """
        msgs = [ x['content'] for i, x in enumerate(self.data['messages']) if 'content' in x ]
        return msgs

    def participants(self):
        """
        Return list of all participants
        """
        return [ obj['name'] for obj in self.data['participants'] ]
    
    def title(self):
        """
        Return name of chat
        """
        return self.data['title']
    
    def is_still_participant(self):
        """
        Return true if user still participant of chat
        """
        return self.data['is_still_participant']
    
    def number_messages(self, participant = None):
        """
        Return the number of messages in thread
        If participant != None return number of messages for participant
        """
        def helper(i, x):
            return participant == self.data['messages'][i]['sender_name']
        if participant:
            return len([ x for i, x in enumerate(self.data['messages']) if helper(i, x) ] )
        return len(self.data['messages'])

    def span(self):
        """
        Return the span of the conversation history
        """
        msg_len = len(self.data['messages'])
        ts_start = self.data['messages'][msg_len-1]['timestamp_ms']
        ts_end = self.data['messages'][0]['timestamp_ms']

        datetime_start = datetime.fromtimestamp(ts_start/1000.0)
        datetime_end = datetime.fromtimestamp(ts_end/1000.0)
        return str(datetime_start), str(datetime_end)

if __name__ == '__main__':
    pass