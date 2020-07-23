import os, requests
import tarfile 
import mailparser
import nltk
from nltk.corpus import stopwords
import re 
from os import listdir
import os 

def download(url):
    get_response = requests.get(url,stream=True)
    file_name  = url.split("/")[-1]
    with open(file_name, 'wb') as f:
        for chunk in get_response.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)


download("https://spamassassin.apache.org/old/publiccorpus/20021010_easy_ham.tar.bz2")
download('https://spamassassin.apache.org/old/publiccorpus/20021010_spam.tar.bz2')


ham = tarfile.open('20021010_easy_ham.tar.bz2')
ham.extractall()
ham.close()

spam = tarfile.open('20021010_spam.tar.bz2')

spam.extractall()
spam.close()

################### <3

a = mailparser.parse_from_file('spam/0500.2e8762b67913d1b07bc8da293448d27f')
body = a.body.lower().split()
header = a.headers.lower()

body = [re.sub('(^[^a-z]*)|([^a-z]*$)', '', words) for words in body]

body = [words.split('/') for words in body]


body = [a for word in body for a in word]

body = list(filter(None, body)) 


filter(None, body)
def aux(x):
    if x in stopwords.words('english'):
        return 0
    else:
        return 1


body_set = set(list(filter(aux, body))) 

### looping over spam files


for i in listdir(os.getcwd() + '\\spam'):
    a = mailparser.parse_from_file(i)
    body = a.body.lower().split()
    body = [re.sub('(^[^a-z]*)|([^a-z]*$)', '', words) for words in body]

body = [words.split('/') for words in body]


body = [a for word in body for a in word]

body = list(filter(None, body)) 


filter(None, body)
def aux(x):
    if x in stopwords.words('english'):
        return 0
    else:
        return 1


body_set = set(list(filter(aux, body))) 