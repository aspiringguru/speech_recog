import spacy
nlp = spacy.load("en")
doc = nlp("The big grey dog ate all of the chocolate, but fortunately he wasn't sick!")
doc.text.split()
[token.orth_ for token in doc]
[(token, token.orth_, token.orth) for token in doc]
[token.orth_ for token in doc if not token.is_punct | token.is_space]
practice = "practice practiced practicing"
nlp_practice = nlp(practice)
nlp_practice

doc2 = nlp("Conor's dog's toy was hidden under the man's sofa in the woman's house")


pos_tags = [(i, i.tag_) for i in doc2]

owners_possessions = []
for i in pos_tags:
    if i[1] == "POS":
        owner = i[0].nbor(-1)
        possession = i[0].nbor(1)
        owners_possessions.append((owner, possession))
        owners_possessions
