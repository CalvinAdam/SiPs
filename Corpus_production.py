import glob, toolz
from textblob import TextBlob
try:
    import cPickle as pickle
except ImportError:
    import pickle


def mutate_dict(f, d):
    for k, v in d.items():
        d[k] = f(v)

ThreeGrams, TwoGrams = {}, {}
wiki = []


articles = glob.glob("C:/Users/Calvin/Desktop/Kofax/Wiki_Language/files/en (english)/*.txt")
for path in articles:
    with open(path, 'r', encoding="utf8") as article:
        wiki.append(TextBlob(article.read()[8:]).lower())
sum3 = 0
sum2 = 0
max3 = 0
max2 = 0
i = 0
for article in wiki:
    article_threegrams, article_twograms = [], []
    blob3 = article.lower().ngrams(n=3)
    blob2 = article.lower().ngrams(n=2)
    print(i, "/", len(wiki))
    i += 1
    for ThreeGram in blob3:
        key = f'{ThreeGram[0]} {ThreeGram[1]} {ThreeGram[2]}'
        if "'" in key or '"' in key:
            continue
        if key not in article_threegrams:
            if key in ThreeGrams.keys():
                ThreeGrams[key] += 1
                if ThreeGrams[key] > max3:
                    max3 = ThreeGrams[key]
            else:
                ThreeGrams[key] = 1
            article_threegrams.append(key)
            sum3 += 1
    for twogram in blob2:
        key = f'{twogram[0]} {twogram[1]}'
        if "'" in key or '"' in key:
            continue
        if key not in article_twograms:
            if key in TwoGrams.keys():
                TwoGrams[key] += 1
                if TwoGrams[key] > max2:
                    max2 = TwoGrams[key]
            else:
                TwoGrams[key] = 1
            article_twograms.append(key)
            sum2 += 1
mutate_dict(lambda x: x/sum3, ThreeGrams)
mutate_dict(lambda x: x/sum2, TwoGrams)
ThreeGrams['max_p'] = max3/sum3
TwoGrams['max_p'] = max2/sum2
pickle.dump(ThreeGrams, open('ThreeGrams.pkl', 'wb'))
pickle.dump(TwoGrams, open('TwoGrams.pkl', 'wb'))
