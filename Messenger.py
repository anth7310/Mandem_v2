from Message import *
from Thread import *

from datetime import datetime

class Messenger:
    def __init__(self):
        self.threads = dict()

    def add_thread(self, thread_path, thread_name = None):
        """
        Add a Messenger thread representing a conversation
        if thread_name is provided, label the thread as thread_name
        """
        new_thread = Thread(thread_path)
        if thread_name:
            self.threads[thread_name] = new_thread
        else:
            self.threads[new_thread.title] = new_thread
    
    def thread_names(self):
        """
        Return list of thread titles
        """
        return list(self.threads.keys())

    def search(self, phrase, title=None):
        pass

    def vocabulary(self):
        """
        Return a dict representing vocabulary count
        """
        pass
    
    # def extract_emojis(self, s):
    #     return ''.join(c for c in s if c in BYTES_EMOJI)

if __name__ == '__main__':

    x = Messenger()
    # x.add_thread('kenneth.json')
    x.add_thread('threads/mandam.json')
    # print threads
    print(x.thread_names())
    thread_name = x.thread_names()[0]

    print(x.threads[thread_name].messages()[1])
    

    # all participants in thread
    # participants = x.threads[thread_name].participants()
    # print(participants)

    # # number of messages
    # print(x.threads[thread_name].number_messages())
    # for p in participants:
    #     print(x.threads[thread_name].number_messages(p), p)

    # span of thread
    print(x.threads[thread_name].span())