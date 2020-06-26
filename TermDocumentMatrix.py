import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_selection import chi2
import numpy as np
from Messenger import *
from tqdm import tqdm
 
# Sample data for analysis
class TermDocumentMatrix:
    def document_dataframe(self, thread):
        """
        Return a dataframe where each row is string of entire thread per participant
        """
        # vectorizer = TfidfVectorizer()
        # doc_vec = vectorizer.fit_transform(df1.iloc[0])

        df = pd.DataFrame()
        # for thread_name in x.thread_names():
        for p in thread.participants():
            df[p] = [' '.join(thread.messages(p))]
        return df

    def term_freq_dataframe(self, thread):
        """
        Return dataframe of messenger threads
        """
        df1 = self.document_dataframe(thread)
        
        vectorizer = CountVectorizer()
        doc_vec = vectorizer.fit_transform(df1.iloc[0])

        # Create dataFrame
        df2 = pd.DataFrame(doc_vec.toarray().transpose(),
                        index=vectorizer.get_feature_names())

        # Change column headers
        df2.columns = df1.columns
        return df2
    
    def chi2(self, thread):
        """
        Return the chisquare test statistic and p-value for each word in thread
        """
        df = self.term_freq_dataframe(thread)
        x = chi2(df.T, list(df.columns))
        return x
    
    def correlated(self, thread, p=0.05, debug=False):
        """
        Return a list of words that are correlated for each participant
        ie. they are used by one participant more often than the other
        """
        x = self.chi2(thread)
        df2 = self.term_freq_dataframe(thread)

        # correlated features
        idx=np.array(x[1]) < p
        if debug:
            print('original features:', len(np.array(df2.T.columns)))
            print('correlated features:', len(np.array(df2.T.columns)[idx]))
        return np.array(df2.T.columns)[idx]

    def independent(self, thread, p=0.05, debug = False):
        """
        Return a list of words that are independent from each participant
        ie. they are both used as frequently by each participant
        statisic model, variable cannot be used to for training
        """
        x = self.chi2(thread)
        df2 = self.term_freq_dataframe(thread)

        # independent stopwords
        idx=np.array(x[1]) >= p
        if debug:
            print('original features:', len(np.array(df2.T.columns)))
            print('independent features (stopwords?):', len(np.array(df2.T.columns)[idx]))
        return np.array(df2.T.columns)[idx]
    
    # def 


if __name__ == "__main__":
    x = Messenger()
    path = 'threads/'
    threads = ['zach']
    # add threads to Messenger
    for t in threads:
        f = path + t + '.json'
        x.add_thread(f)

    p = x.thread_names()[0]
    td = TermDocumentMatrix()
    # idx = td.independent(x[p])
    
    idx = td.correlated(x[p])
    print(idx)

    # more options can be specified also
    # with pd.option_context('display.max_rows', None, 'display.max_columns', None):  
    #     print(td.term_freq_dataframe(x[p]).loc[idx])
        # print(td.term_freq_dataframe(x[p]))
    # print(td.chi2(x[p]))
    for word in td.correlated(x[p], debug=True):
        print(word)
    

# vectorizer = TfidfVectorizer()
# doc_vec = vectorizer.fit_transform(df1.iloc[0])







