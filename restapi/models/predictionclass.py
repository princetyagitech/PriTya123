import joblib
import re
import pandas as pd
import numpy as np
from sklearn.svm import LinearSVC
import nltk
from nltk.tokenize import word_tokenize
from sklearn.preprocessing import LabelEncoder
from nltk.corpus import stopwords
import string
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
import spacy

nlp = spacy.load('de_core_news_sm')
stop_words = set(stopwords.words("german"))
stemmer = SnowballStemmer("german")
nltk.download('punkt')

le = LabelEncoder()
le.classes_ = np.load('models/class.npy',allow_pickle=True)

def clean_mydata(text):
    RE_WSPACE = re.compile(r"\s+", re.IGNORECASE)
    RE_TAGS = re.compile(r"<[^>]+>")
    RE_ASCII = re.compile(r"[^A-Za-zÀ-ž ]", re.IGNORECASE)
    RE_SINGLECHAR = re.compile(r"\b[A-Za-zÀ-ž]\b", re.IGNORECASE)


    text = re.sub(RE_TAGS, " ", text)
    text = re.sub(RE_ASCII, " ", text)
    text = re.sub(RE_SINGLECHAR, " ", text)
    text = re.sub(RE_WSPACE, " ", text)

    word_tokens = word_tokenize(text)
    words_tokens_lower = [word.lower() for word in word_tokens]


    ##Stemming

    text = [stemmer.stem(word) for word in words_tokens_lower if not word in stop_words]
    doc = nlp(' '.join(text))
    result = ' '.join([x.lemma_ for x in doc])
    return result

def predictclass(text):

    return le.inverse_transform(joblib.load('models/model.pkl').predict(pd.Series(clean_mydata(text))))
