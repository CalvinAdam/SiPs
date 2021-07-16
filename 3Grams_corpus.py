import glob
from textblob import TextBlob
try:
    import cPickle as pickle
except ImportError:
    import pickle
ThreeGrams = {}
wiki = []


articles = glob.glob("C:/Users/Calvin/Desktop/Kofax/Wiki_Language/files/en (english)/*.txt")
for path in articles:
    with open(path, 'r', encoding="utf8") as article:
        wiki.append(TextBlob(article.read()[8:]).lower())
_sum_ = 0
_max_ = 0
i = 0
for article in wiki:
    article_threegrams = []
    blob = article.ngrams(n=3)
    print(i, "/", len(wiki))
    i += 1
    for ThreeGram in blob:
        key = f'{ThreeGram[0]} {ThreeGram[1]} {ThreeGram[2]}'
        if "'" in key or '"' in key:
            continue
        if key not in article_threegrams:
            if key in ThreeGrams.keys():
                ThreeGrams[key] += 1
            else:
                ThreeGrams[key] = 1
            article_threegrams.append(key)
            _sum_ += 1
for ThreeGram in ThreeGrams:
    ThreeGrams[ThreeGram] = ThreeGrams[ThreeGram]/_sum_
    if ThreeGrams[ThreeGram] > _max_:
        _max_ = ThreeGrams[ThreeGram]
ThreeGrams['max_p'] = _max_
print(_max_, _sum_)
pickle.dump(ThreeGrams, open('ThreeGrams.pkl', 'wb'))
