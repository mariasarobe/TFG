from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
c_vec=CountVectorizer(stop_words=stoplist, ngram_range=(2,3))
ngrams=c_vec.fit_transform(df['Abstract'])
count_values=ngrams.toarray().sum(axis=0)
vocab=c_vec.vocabulary_
df_ngram=pd.DataFrame(sorted([(count_values[i],k) for k,i in vocab.items()],reverse=True)).rename(columns={0: 'frequency', 1:'bigram/trigram'})
