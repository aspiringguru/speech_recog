import spacy
nlp = spacy.load("en")
doc = nlp("These are apples. These are oranges.")

#identify sentences from text.
for sent in doc.sents:
    print(sent)


doc = nlp("Next week I'll be in Madrid.")
print([(token.text, token.tag_) for token in doc])

doc = nlp("Next week I'll be in Madrid with my Ford.")
for ent in doc.ents:
    print(ent.text, ent.label_)

doc = nlp("Next week I'll be in Madrid with my Ford to play cricket.")
for ent in doc.ents:
    print(ent.text, ent.label_)

doc = nlp("Next week I'll be in Madrid with my Ford but no Mary.")
for ent in doc.ents:
    print(ent.text, ent.label_)

from spacy import displacy
doc = nlp('Wall Street Journal just published an interesting piece on crypto currencies')
for token in doc:
    print("{0}/{1} <--{2}-- {3}/{4}".format(
        token.text, token.tag_, token.dep_, token.head.text, token.head.tag_))

#https://spacy.io/usage/visualizers
#this only works in a notebook.
displacy.render(doc, style='dep', jupyter=True, options={'distance': 90})
#opens a server on port 5000
displacy.serve(doc, style='dep')
