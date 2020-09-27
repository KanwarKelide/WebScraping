# -*- coding: utf-8 -*-
# -*- coding: ISO-8859-1 -*-
# -*- coding: ISO-8859-2 -*-
import re
from itertools import chain
import dateutil.parser
#Folders
main_dir = "D:\\Projects\\Automotive\\"
path = main_dir + "Output\Formatted\\"
temp = main_dir + "Output\Temp\\"
fina = main_dir + "Output\Final\\"
data = main_dir + "Data\\"
import datetime
import pytz, datetime
#Libraries

import numpy as np
import pandas as pd
import itertools
import nltk
from collections import Counter
from itertools import groupby
from operator import itemgetter
from collections import Counter
import time
import nltk
from nltk.corpus import wordnet as wn

import nltk

# nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import os
import glob
import langdetect
import time
import random

import sys
from langdetect import detect
from langdetect import detect_langs
import unicodedata
import warnings
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag
from requests import get
from bs4 import BeautifulSoup
#warnings.filterwarnings("ignore")
#'python from langdetect import DetectorFactory DetectorFactory.seed = 0'
import functools
from functools import reduce
import dateutil.parser
import datetime
import pytz, datetime
import urllib3
import unicodedata
import pytz
import random
from dateutil import tz
from_zone = tz.gettz('UTC')

import requests
import _strptime
from multiprocessing.dummy import Pool as ThreadPool
from random import randint
import time
import multiprocessing
from itertools import product

def strip_tags(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

contextual_stop_words = ['continent','years','months','month','year','century','centuries','days','day','weeks','week','country','decade','already','even']
modal_verbs = ["has","can","could","do","should","does","would","have","had","did","is","are","hasnt","cannot","couldnt","dont","shouldnt","doesnt","wouldnt","havent","hadnt","didnt","isnt"]
verbs_tag = ['VB','VBD','VBG','VBN','VBP','VBZ']
nouns_tag = ["NN","NNP","NNS","NNPS"]
adjectives_tag = ['JJ','JJR','JJS']
adverbs_tag = ["RB","RBR","RBS"]
prepositions_tag = ["IN",'TO']
useless_tag = ["CD",'DT']

def byteify(input):
    if isinstance(input, dict):
        return {byteify(key):byteify(value) for key,value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

def remove_unicode(text):
    text = text.replace('Â', '').replace('â€™', "'").replace('â', '').replace("...", "").replace("]","").replace('&#039;',"'").replace('"','').replace('&amp;','&').replace('*','').replace('&amp;','&')
    text = text.replace('A&#770; ', ' ').replace("\\", "").strip()
    text = text.replace('\xe2\x80\x99',"'").replace('\xe2\x80\x98',"'")
    # text = unicodedata.normalize("NFKD",text)
    text = unicodedata.normalize("NFKD", unicode(text, encoding='utf-8'))
    text = byteify(text).decode('unicode_escape').encode("ascii", "ignore").lstrip().rstrip().replace('   ', '')
    return text

import datetime
import pytz, datetime
# Libraries
import numpy as np
import pandas as pd
import itertools
import urllib2
import glob
import langdetect
import pandas as pd
import langid
import sys
from langdetect import detect
from langdetect import detect_langs
import unicodedata
import warnings
warnings.filterwarnings("ignore")
'python from langdetect import DetectorFactory DetectorFactory.seed = 0'
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
sys.setdefaultencoding("ISO-8859-1")
sys.setdefaultencoding("ISO-8859-2")
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stdout = codecs.getwriter("iso-8859-1")(sys.stdout, 'xmlcharrefreplace')
sys.stdout = codecs.getwriter("iso-8859-2")(sys.stdout, 'xmlcharrefreplace')
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import urllib3
http = urllib3.PoolManager()
from bs4 import BeautifulSoup
import string
from string import punctuation

import urllib
import re
import dateutil
from dateutil.parser import parse
# import calendar
import pycountry
from django.utils.encoding import smart_str, smart_unicode
import requests
from difflib import SequenceMatcher as SM
import datetime
from datetime import date
from datetime import datetime
from datetime import timedelta
from dateutil import rrule
from dateutil import parser
import time
urllib3.disable_warnings()
import calendar
import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")

modal_verbs = ["has","can","could","do","should","does","would","have","had","did","is","are","hasnt","cannot","couldnt","dont","shouldnt","doesnt","wouldnt","havent","hadnt","didnt","isnt"]
verbs_tag = ['VB','VBD','VBG','VBN','VBP','VBZ']
nouns_tag = ["NN","NNP","NNS","NNPS"]
adjectives_tag = ['JJ','JJR','JJS']
nnp_tag = ["NNP", "NNPS"]
adverbs_tag = ["RB","RBR","RBS"]
prepositions_tag = ["IN"]
useless_tag = ["CD"]










start_words1 = []

start_words2 = [""]

plurals = [""]

start_words = start_words1 + start_words2
wrong_words = ["never"]
months = calendar.month_name
months2 = [x.lower() for x in months]
months_abbr = calendar.month_abbr
months_abbr2 = [x.lower() for x in months_abbr]
week_days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
small_letters = map(chr, range(ord('a'), ord('z')+1))


stop_NNPs = ['Mr.','Dr.']
plural_PRPs = ['they','their','them','those','us','we','those','themselves','it', 'itself','you','yourselves','yourself','our','ourselves','ourself']

stative_verbs = ["like","liked", "love", "loved","hate","hated", "dislike","disliked", "want","wanted", "hope","hoped", "wish","wished", "feel","felt", "need", "prefer","preferred",
                 "enjoy","enjoyed", "appreciate","appreciated", "fear","feared", "envy","envied", "care","cared","smelt","smelled","tasted","contains","contained","consists","gets"]

stop_titles = ["ENTERTAINMENT WEEKLY","FACEBOOK","YOUTUBE","TUMBLR","INSTAGRAM","PINTEREST","GOOGLE+"]

infinitive_words = ["progressively","quite","towards"]
infinitive_words2 = ["full","little","pretty","worth","absolute","huge","top","pure","total"]
ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])
all_ordinals = []
all_ordinals.append([ordinal(n) for n in range(1,5000)])
eng_numerals = ["first","second","third","fourth","fifth","sixth","seventh","eighth","nineth","ninth","tenth"]

# Definitions
def byteify(input):
    if isinstance(input, dict):
        return {byteify(key):byteify(value) for key,value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

 def remove_unicode(text):
#     text = text.replace('Â', '').replace('â€™', "'").replace('â', '').replace("...", "").replace("]","").replace('&#039;',"'").replace('&ldquo;','"').replace('"','').replace('&amp;','&').replace('*','')
#     text = text.replace('A&#770; ', ' ').replace("\\", "").strip()
#     text = unicodedata.normalize("NFKD", unicode(text, encoding='utf-8'))
#     text = byteify(text).decode('unicode_escape').encode("ascii", "ignore").lstrip().rstrip().replace('   ', '')
#     return text

# from html.parser import HTMLParser
from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

punctuation2 = '-!"#$%&()*+,:;<=>?@[\]^_`{|}~“Ââ€¦«'

def strip_punctuation(s):
   return ''.join(c for c in s if c not in (punctuation2))

def replace_words(input):
    input = input.replace("i am a ","i am ")
    input = input.replace("under active","underactive")
    input = input.replace("under-active", "underactive")
    input = input.replace("diagnoised","diagnosed")
    input = input.replace("im ","i am ")
    input = input.replace("hasnt", "has not")
    input = input.replace("hadnt", "had not")
    input = input.replace("havent", "have not")
    input = input.replace("haven't", "have not")
    input = input.replace("dont", "do not")
    input = input.replace("don't", "do not")
    input = input.replace("didnt", "did not")
    input = input.replace("didn't", "did not")
    input = input.replace("wouldnt", "would not")
    input = input.replace("wouldn't", "would not")
    input = input.replace("cannot", "can not")
    input = input.replace(" can't ", " cant ")
    input = input.replace(" cant ", " can not ")
    input = input.replace("couldnt", "could not")
    input = input.replace("couldn't", "could not")
    input = input.replace("shouldnt", "should not")
    input = input.replace("shouldn't", "should not")
    input = input.replace('doesnt', "does not")
    input = input.replace("doesn't", "does not")
    input = input.replace('isnt', " is not")
    input = input.replace("isn't", " is not")
    input = input.replace("it's", "its")
    input = input.replace("great", "good")
    input = input.replace("best", "good")
    # input = input.replace(" an ", " ")
    # input = input.replace(" a ", " ")
    # input = input.replace("much", " ")
    input = input.replace("  ", " ")
    input = input.replace(".", " . ")
    # input = input.replace(" the ", " ")
    # input = input.replace(" my ", " ")
    # input = input.replace(" this ", " ")
    # input = input.replace(" as ", " ")
    input = input.replace("i've", " i have ")
    input = input.replace(" ive ", " i have ")
    input = input.replace("'ve", " have ")
    input = input.replace("i'm", " i am ")
    input = input.replace("'m", " am ")
    input = input.replace("'s","s")
    input = input.replace("theyre","they are")
    input = input.replace("more and more","more")
    input = input.replace("..."," ")
    return input


def join_lines(s):
    s = filter(lambda y: y in string.printable, s)
    s = ' '.join(s.split()).strip()
    s = ' '.join(s.split())
    return s

def get_soup(url):
    soup = BeautifulSoup(urllib.urlopen(url).read(),"html.parser")

    if "ACCESS DENIED" in str(soup).upper() or "403 FORBIDDEN" in str(soup).upper() or 'BANNED YOUR ACCESS' in str(soup).upper():
        http = urllib3.PoolManager()
        r = http.request('GET', url)
        page = r.data
        soup = BeautifulSoup(page, "html.parser")
    return soup

all_countries = []
all_states = []
all_scripts = []
all_currencies = []
all_languages = []

for i in range(len(pycountry.countries)):
    x = list(pycountry.countries)[i].name
    all_countries.append(x)

all_countries2 = [x.lower() for x in all_countries]

for i in range(len(pycountry.subdivisions)):
    x = list(pycountry.subdivisions)[i].name
    all_states.append(x)

for i in range(len(pycountry.scripts)):
    x = list(pycountry.scripts)[i].name
    all_scripts.append(x)

for i in range(len(pycountry.currencies)):
    x = list(pycountry.currencies)[i].name
    all_currencies.append(x)

for i in range(len(pycountry.languages)):
    x = list(pycountry.languages)[i].name
    all_languages.append(x)

from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree

from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree

# def get_continuous_chunks(text):
#     chunked = ne_chunk(pos_tag(word_tokenize(text)))
#     prev = None
#     continuous_chunk = []
#     current_chunk = []
#
#     for i in chunked:
#         if type(i) == Tree:
#             current_chunk.append(" ".join([token for token, pos in i.leaves()]))
#         elif current_chunk:
#             named_entity = " ".join(current_chunk)
#             if named_entity not in continuous_chunk:
#                 continuous_chunk.append(named_entity)
#                 current_chunk = []
#         else:
#             continue
#
#     if continuous_chunk:
#         named_entity = " ".join(current_chunk)
#         if named_entity not in continuous_chunk:
#             continuous_chunk.append(named_entity)
#
#     return continuous_chunk


def get_continuous_chunks(text):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    prev = None
    continuous_chunk = []
    current_chunk = []
    for i in chunked:
         if type(i) == Tree:
                 current_chunk.append(" ".join([token for token, pos in i.leaves()]))
         elif current_chunk:
                 named_entity = " ".join(current_chunk)
                 if named_entity not in continuous_chunk:
                         continuous_chunk.append(named_entity)
                         current_chunk = []
         else:
                 continue
    return continuous_chunk



def replace_words2(input):
    input = input.replace("great", "good")
    input = input.replace("best", "good")
    input = input.replace("greatest", "good")
    input = input.replace("better", "good")
    input = input.replace(","," ").strip()
    input = input.replace("-"," ").strip()
    return input

plot_bucket = ["plot","plots","subplot","subplots","plotting","story","stories","theme","concept","plotline","plotlines","sub-plot","sub-plots","subject","storyline","storylines"]
subject_bucket = ["actor","actress"]
series_bucket = ["series","episodes","episode","show","shows","pantomime"]

stars = ['5star', '4star', '3star', '2star', '1star']

access_key = "AKIAJLYQIWTBYHHIS33Q"
secret_key = "bzuB28H70Gw47gtz4KjrpWTx5EprCQql"
access_key2 = "AKIAJP27D3TDPCHTG6RA"
secret_key2 = "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"

access_key_main = "AKIAI7E2OH565WG4WRXQ"
secret_key_main = "lfpgMugoYFkcAaZ0AdFjt/V9UnyA6PbibSkYhjXk"
# track_id = "test0dc96-21"

def replace_digits(input):
    input = input.replace("1. ","1 ")
    input = input.replace("2. ", "2 ")
    input = input.replace("3. ", "3 ")
    input = input.replace("4. ", "4 ")
    input = input.replace("5. ", "5 ")
    input = input.replace("6. ", "6 ")
    input = input.replace("7. ", "7 ")
    input = input.replace("8. ", "8 ")
    input = input.replace("9. ", "9 ")
    return input

def replace_chapters(input):
    input = input.lower()
    input = input.replace("chapter fourteen", "14.")
    input = input.replace("chapter fifteen", "15.")
    input = input.replace("chapter sixteen", "16.")
    input = input.replace("chapter seventeen", "17.")
    input = input.replace("chapter eighteen", "18.")
    input = input.replace("chapter nineteen", "19.")
    input = input.replace("chapter twenty", "20.")
    input = input.replace("chapter one","1.")
    input = input.replace("chapter two", "2.")
    input = input.replace("chapter three", "3.")
    input = input.replace("chapter four", "4.")
    input = input.replace("chapter five", "5.")
    input = input.replace("chapter six", "6.")
    input = input.replace("chapter seven", "7.")
    input = input.replace("chapter eight", "8.")
    input = input.replace("chapter nine", "9.")
    input = input.replace("chapter ten", "10.")
    input = input.replace("chapter eleven", "11.")
    input = input.replace("chapter twelve", "12.")
    input = input.replace("chapter thirteen", "13.")
    return input

def article_stops(input):
    input = input.replace("market","")
    input = input.replace("global","")
    input = input.replace("report","")
    input = input.replace("research","")
    input = input.replace("analysis","")
    input = input.replace("forecasts","")
    input = input.replace("segment","")
    input = input.replace("europe","")
    input = input.replace("outlook","")
    input = input.replace("product","")
    input = input.replace("size","")
    input = input.replace("trends","")
    input = input.replace("trend","")
    input = input.replace("usability","")
    input = input.replace("profiles","")
    input = input.replace("by","")
    input = input.replace("east","")
    input = input.replace("west","")
    input = input.replace("north","")
    input = input.replace("south","")
    input = input.replace("type", "")
    input = input.replace("summary", "")
    input = input.replace("context", "")
    return input

article_stop = \
    ["market",
     "global",
     "report",
     "research",
     "analysis",
     "analytics",
     "forecasts",
     "segment",
     "europe",
     "outlook",
     "product",
     "size",
     "trends",
     "trend",
     "usability",
     "profiles",
     "by",
     "east",
     "west",
     "north",
     "south",
     ]


def google_news(u):
    page = http.request('GET',u).data
    soup = BeautifulSoup(page,"html.parser")

    for i in soup.find_all('div'):
        j = str(i)
        j2 = join_lines(j)
        if '<div class="slp">' in j2 and 'class="g"' in j2 and j2.split('"')[1] == "g":
            j2 = j2[j2.find('href='):]
            news_url = j2.split('"')[1].split("&amp;")[0].replace('/url?q=','').strip()
            news_title = strip_tags(j2.split('"')[2]).replace(">","").strip()
            j2 = j2[j2.find('class="f"'):].split(">")[1].split("<")[0]
            source = strip_tags(j2.split("-")[0].strip())
            date_posted = j2.split("-")[1]
            date_posted = " ".join(date_posted.split())
            all_titles.append(news_title)
            all_sources.append(source)
            all_urls.append(news_url)
            all_dates.append(date_posted)
            all_tickers.append(t)

def strip_company_tags(input):
    input = input.replace("Inc.","")
    input = input.replace("& Company","")
    input =input.replace("& Co","")
    input = input.replace(" Corporation",'')
    input = input.strip()
    return input

