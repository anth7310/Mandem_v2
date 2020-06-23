import Message
from Thread import *

class Messenger:
    def __init__(self):
        self.threads = dict()

    def add_thread(self, thread_path):
        new_thread = Thread(thread_path)
        self.threads[new_thread.title] = new_thread
    
    def thread_names(self):
        """
        Return list of thread titles
        """
        return list(self.threads.keys())

    def search(self, phrase, title=None):
        pass
    
    def extract_emojis(self, s):
        return ''.join(c for c in s if c in BYTES_EMOJI)

if __name__ == '__main__':

    x = Messenger()
    # x.add_thread('kenneth.json')
    x.add_thread('Threads/zach.json')
    # print threads
    # print(x.thread_names())
    print(x.threads['Zach Barlow'].number_messages())
    print(x.threads['Zach Barlow'].span())
    # print(x.number_messages())