from Messenger import *
from nltk.corpus import stopwords
from nltk import word_tokenize
from string import punctuation
from tqdm import tqdm

import matplotlib.pyplot as plt
from wordcloud import WordCloud

stop_words = set(stopwords.words('english'))
custom_stop_words = [
    'i', 'u', '\'s', 'n\'t', '``', '\'\'', '\'m', '\'ll', '\'re',
    'ur', 'im', 'ill', 'tho', '\'ve', '...', 
    '\'d'
]
stop_words = stop_words.union(custom_stop_words)

class NLP:
    def __init__(self):
        self.stopwords = stop_words
    
    def vocabulary_count(self, thread, participant=None):
        """
        Return the vocabulary count as a dictionary given thread x
        """
        token_set = dict()
        for i in tqdm(range(len(thread.messages(participant)))):
            # all tokens to lower case
            sentence = thread.messages(participant)[i].lower()
            tokens = word_tokenize(sentence)
            for t in tokens:
                if t in token_set:
                    token_set[t] += 1
                else:
                    token_set[t] = 1
        return token_set
    
    def sorted_vocabulary(self, token_set, min_count=10):
        """
        print a sorted vocabulary count
        """
        stop_words = self.stopwords
        d = [k for k, v in sorted(token_set.items(), key=lambda item: item[1])]
        print(len(token_set))
        for k in d[::-1]:
            if k not in stop_words and k not in punctuation and token_set[k] > min_count:
                print(k, token_set[k])

if __name__ == '__main__':
    x = Messenger()
    x.add_thread('threads/sulay.json')
    thread_name = x.thread_names()[0]

    # nlp = NLP()
    # print(x[thread_name].participants())
    # ['Seema Mistry', 'Anthony Inthavong']
    # for p in x[thread_name].participants():
    # token_set = nlp.vocabulary_count(x[thread_name], 'Anthony Inthavong')
    # s = sum([v for k, v in token_set.items()])
    # avg = s/len(token_set)
    # nlp.sorted_vocabulary(token_set, int(avg))

    ['Sulayman Malik', 'Anthony Inthavong']
    comment_words = ''.join(x[thread_name].messages('Anthony Inthavong'))
    # comment_words = [k]
    wordcloud = WordCloud(collocations=False, stopwords=stop_words).generate(comment_words) 
  
    # plot the WordCloud image                        
    plt.figure(figsize = (8, 8), facecolor = None) 
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 
    
    plt.show() 
   
    