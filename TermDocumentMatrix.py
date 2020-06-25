import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from Messenger import *
from tqdm import tqdm
 
# Sample data for analysis

x = Messenger()
path = 'threads/'
threads = ['Zach']
extension = '.json'
for t in threads:
    f = path + t + extension
    x.add_thread(f)

df1 = pd.DataFrame()
# for thread_name in x.thread_names():
#     p = x[thread_name].participants()[0]
#     for i, msg in enumerate(x[thread_name].messages(p)):
#         # df1[i] = [' '.join(x[thread_name].messages(p))]
#         df1[i] = [msg]

# sparse matrix for each person
# i = 0
# for thread_name in x.thread_names():
#     p = x[thread_name].participants()[1]
#     label = p + str(i)
#     i += 1
#     # print(p)
#     df1[label] = [' '.join(x[thread_name].messages(p))]

for thread_name in x.thread_names():
    for p in x[thread_name].participants():
        df1[p] = [' '.join(x[thread_name].messages(p))]

# Initialize
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
doc_vec = vectorizer.fit_transform(df1.iloc[0])

# vectorizer = TfidfVectorizer()
# doc_vec = vectorizer.fit_transform(df1.iloc[0])

# Create dataFrame
df2 = pd.DataFrame(doc_vec.toarray().transpose(),
                index=vectorizer.get_feature_names())

# Change column headers
df2.columns = df1.columns

# for i, v in enumerate(df2.mean(0) >= df2.mean(0).mean()):
#     if v:
#         print(x[thread_name]._message_list[i])

# # display entire table
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):  
# # #     print(df2[df2[p] > df2.mean(0)[p]][p])
#     print(df2.T[df2.mean(0) >= df2.mean(0).mean()])
# print(df2)

from sklearn.feature_selection import chi2
import numpy as np
# print(list(df2.columns))
# print(df2.T)
x=chi2(df2.T, list(df2.columns))

# correlated features
idx=np.array(x[1]) >= 0.95
print('original features:', len(np.array(df2.T.columns)))
print('correlated features:', len(np.array(df2.T.columns)[idx]))
# print('independent features (stopwords?):', len(np.array(df2.T.columns)[idx]))
for word in np.array(df2.T.columns)[idx]:
    print(word)


# independent stopwords
# idx=np.array(x[1]) < 0.95
# print('original features:', len(np.array(df2.T.columns)))
# print('independent features (stopwords?):', len(np.array(df2.T.columns)[idx]))
# for word in np.array(df2.T.columns)[idx]:
#     print(word)


# with pd.option_context('display.max_rows', None, 'display.max_columns', None):  
# print(x[0][0])



