from silabeador import *

_INTERSILABA = 'pi'

def pipalabra(word):
    silabas = silabea(word)
    newword = _INTERSILABA+ _INTERSILABA.join(silabas)
    
    return newword

def pilengua(word):
    if ' ' in word:
        newphrase = []
        palabras = word.split()
        for palabra in palabras:
            newword = silabea(palabra)
            if newword and newword[0][0].lower() == 'r':
                newword[0] = newword[0][0] + newword[0]

            newword = _INTERSILABA + _INTERSILABA.join(newword) 
            newphrase.append(newword)
        return ' '.join(newphrase).lower()
    else:
        return pipalabra(word)

