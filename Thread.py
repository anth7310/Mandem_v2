import json
from datetime import datetime
from datetime import timedelta
import regex
from algorithms.unicodetoascii import unicodetoascii
from Message import Message

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
        self._message_list = self._create_message_list()
        
        self.messages_keys = self._generate_messages_keys()
    
    def get_message_list(self):
        return (str(msg) for msg in self._message_list)
    
    def _create_message_list(self, participant=None):
        """
        Return a list of Message objects in a thread
        Only consider messages with 'content' tag
        If participant not None, return all messages by participant
        if group_by != None return a dict where key: date and value: list of messages
        group_by:
            day
            month
            year
        """
        d = self.data['messages']
        # helper function
        def f(x, participant=None):
            if participant:
                return 'content' in x and x['sender_name'] == participant
            return 'content' in x

        # encode into Message object
        msgs = [ 
            Message(d[i]['sender_name'], d[i]['timestamp_ms'], d[i]['content']) for i, x in enumerate(d) if f(d[i], participant)
        ]
        return msgs
    
    def group_by(self, participant=None, time='month'):
        """
        Group a message_list by dates: day, month, or year
        """
        msg_list = self._create_message_list(participant)
        d = dict()
        ts = msg_list[0].timestamp_ms
        timedelta(days=1)
        print(datetime.fromtimestamp(ts/1000.0))
        exit()
        for msg in msg_list:
            if time == 'day':
                pass
            elif time == 'month':
                pass
            elif time == 'year':
                pass

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

    def messages(self, participant = None) -> list:
        """
        Return messages as list
        If participant not None, return all messages by participant
        """
        if participant == None:
            msgs = [ x['content'] for i, x in enumerate(self.data['messages']) if 'content' in x ]
        else:
            msgs = [ x['content'] for i, x in enumerate(self.data['messages']) if 'content' in x and x['sender_name'] == participant ]
        return msgs

    def participants(self):
        """
        Return list of all participants
        """

        p = set([ msg['sender_name'] for msg in self.data['messages'] ])
        return list(p)
    
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
    
    def average_length(self, participant=None):
        """
        Return the average length of messages in thread
        If participant != None return number of messages for participant
        """
        pass

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
    
    def extract_emojis(self, s):
        return ''.join(c for c in s if c in BYTES_EMOJI)

if __name__ == '__main__':
    import plotly.graph_objects as go
    from datetime import datetime
    

    # np.random.seed(1)
    x = Thread('./threads/mandam.json')
    print(x.span())
    msg_list = x._create_message_list()

    participants = sorted(x.participants(), reverse=True)
    dates = [datetime.fromtimestamp(msg.timestamp_ms/1000.0) for msg in msg_list]

    # count number messages per participant
    # create matrix using dictionary to store all values
    dmys = [(date.year, date.month, date.day) for date in dates]
    d = dict()
    print(participants)
    for p in participants:
        d[p] = dict()
        for date in set(dmys):
            d[p][date] = 0

    for msg in msg_list:
        date = datetime.fromtimestamp(msg.timestamp_ms/1000.0)
        # keep count by day, month, year
        dmy = (date.year,  date.month, date.day)
        p = msg.sender_name # participant name
        if dmy in d[p]:
            d[p][dmy] += 1

    # message count for each date as matrix (participant, datetime)
    z = []
    for p in participants:
        z.append([ d[p][v] for v in sorted(d[p].keys(), reverse=False) ])

    # datetime objects are required for Heatmap figure in plotly
    dates = sorted([datetime(year, month, day) for (year, month, day) in set(dmys)])
    fig = go.Figure(data=go.Heatmap(
            z=z,
            x=dates,
            y=participants,
            colorscale='Viridis'))

    fig.update_layout(
        title='Messages sent per day in {}'.format(x.title),
        xaxis_nticks=36) # 36

    fig.show()