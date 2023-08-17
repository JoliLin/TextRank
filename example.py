#### Prepare stopwords ####
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stop = stopwords.words('english')
#### Prepare stopwords ####

from src.tokenizer import tokenize, _is_punctuation
from src.TextRank import textrank

#### Raw data ####
corpus = [
    "Give every man thy ear, but few thy voice; Take each man’s censure, but reserve thy judgment.",
    "Therefore, since brevity is the soul of wit, And tediousness the limbs and outward flourishes.",
    "It's not the drugs that make a drug addict, it's the need to escape reality."
]

#### Remove symbol ####
corpus = [''.join([j for j in i if _is_punctuation(j) == False]) for i in corpus]

#### Split by space ####
corpus = [tokenize(i) for i in corpus]

#### Run TextRank ####
res = textrank(corpus, remove_stop=stop)

#### Without removing Stopwords ####
#res = textrank(corpus)

for i in res:
    print(i)
