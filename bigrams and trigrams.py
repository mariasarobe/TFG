import matplotlib.pyplot as plt
import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
import inflection as inf
from inflection import singularize
import re 
from collections import Counter

#load csv
data = pd.read_csv(r'/Users/mariasarobebove/Desktop/TFG_2/Patents/Lens/abstracts.csv')

#create dataframe
df= pd.DataFrame(data)

#remove stopwords
stop= stopwords.words('english')
df['Abstract'] = df['Abstract'].apply(lambda x: ' '.join([inf.singularize(word) for word in x.split() if word not in (stop)]))#extract bigrams/trigrams from a dataframe

#if we need to add additional stopwords
#extrastop=[]
#stop.extend(extrastop)

#used for the patents titles
c_vec=CountVectorizer(stop_words=stoplist, ngram_range=(2,3))
ngrams=c_vec.fit_transform(df['Abstract'])
count_values=ngrams.toarray().sum(axis=0)
vocab=c_vec.vocabulary_
df_ngram=pd.DataFrame(sorted([(count_values[i],k) for k,i in vocab.items()],reverse=True)).rename(columns={0: 'frequency', 1:'bigram/trigram'})

#extract bigrams/trigrams from a large dataframe 
#used for the patents abstracts

#generate unigrams
unigrams=(df['String'].str.lower().str.replace(r'[^a-z\s]', '').str.split(expand=True).stack())
# generate bigrams by concatenating unigram columns
bigrams = unigrams + ' ' + unigrams.shift(-1)
# generate trigrams by concatenating unigram and bigram columns
trigrams = bigrams + ' ' + unigrams.shift(-2)
# concatenate all series vertically, and remove NaNs
ngrams=pd.concat([unigrams, bigrams, trigrams]).dropna().reset_index(drop=True) #in my case i only used bigrams and trigrams
#count all the bigrams/trigrams
ngrams.value_counts()

#plot the 30 most common bigrams/trigrams 
results=ngrams.value_counts()[:30]
#horizontal bar chart 
results.plot.barh()
plt.title('Bigrams/Trigrams frequency in patent titles')
#sort the results from higher to lower 
plt.gca().invert_yaxis()
plt.show()
