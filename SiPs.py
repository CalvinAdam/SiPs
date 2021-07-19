from textblob import TextBlob
try:
    import cPickle as pickle
except ImportError:
    import pickle

words = []
wiki = []
TwoGrams, ThreeGrams = {}, {}
improbabilities = {}
bigsum, smallsum = 0, 0
removable_characters = """,.;:!"(')-*&_/"""
# Import the TwoGrams_corpus for 2-grams
TwoGrams_corpus = pickle.load(open('TwoGrams.pkl', 'rb'))
max_p_two = TwoGrams_corpus['max_p']
del TwoGrams_corpus['max_p']
# Import the TwoGrams_corpus for 3-Grams (wikipedia)
ThreeGrams_corpus = pickle.load(open('ThreeGrams.pkl', 'rb'))
max_p_three = ThreeGrams_corpus['max_p']
del ThreeGrams_corpus['max_p']
# Import the document
with open("C:/Users/Calvin/Desktop/digital_rhetoric_politics.txt", "r", encoding='utf8') as d:
    document = TextBlob(d.read()).lower()
blob = document.ngrams(n=2)
print("Done with 2-Gram")
for TwoGram in blob:
    key = f'{TwoGram[0]} {TwoGram[1]}'
    if "'" in key or '"' in key:
        continue
    if key in TwoGrams.keys():
        TwoGrams[key] += 1
    else:
        TwoGrams[key] = 1
blob = document.ngrams(n=3)
print("Done with 3-Gram")
for ThreeGram in blob:
    key = f'{ThreeGram[0]} {ThreeGram[1]} {ThreeGram[2]}'
    if "'" in key or '"' in key:
        continue
    if key in ThreeGrams.keys():
        ThreeGrams[key] += 1
    else:
        ThreeGrams[key] = 1
print("Done with dictionary")


for TwoGram in TwoGrams:
    if TwoGram in TwoGrams_corpus.keys():
        improbability = (1-(TwoGrams_corpus[TwoGram]/max_p_two))**30
        improbabilities[TwoGram] = improbability*TwoGrams[TwoGram]
    else:
        improbabilities[TwoGram] = TwoGrams[TwoGram]
for index, phrase in enumerate(sorted(improbabilities, key=improbabilities.get)[::-1]):
    if index <= 10:
        print(phrase, improbabilities[phrase])
    else:
        break
print("*"*50)
improbabilities = {}
for ThreeGram in ThreeGrams:
    if ThreeGram in ThreeGrams_corpus.keys():
        improbability = (1-(ThreeGrams_corpus[ThreeGram]/max_p_three))**30
        improbabilities[ThreeGram] = improbability*ThreeGrams[ThreeGram]
    else:
        improbabilities[ThreeGram] = ThreeGrams[ThreeGram]
for index, phrase in enumerate(sorted(improbabilities, key=improbabilities.get)[::-1]):
    if index <= 10:
        print(phrase, improbabilities[phrase])
    else:
        break



