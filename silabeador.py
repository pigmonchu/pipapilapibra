consonantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'll', 'm', 'n', 'ñ', 'p', 'q', 'r', 'rr', 's', 't', 'v', 'w', 'x', 'z']
vocales_abiertas = ['a', 'e', 'o', 'á', 'é', 'í', 'ó', 'ú']
vocales_cerradas = ['i', 'u', 'ü']
semivocales = ['y']

def esDiptongo(position, word):
    if len(word) < position + 2:
        return False
    
    return (word[position] in vocales_cerradas and (word[position+1] in vocales_cerradas or word[position+1] in semivocales)) or \
           (word[position] in vocales_abiertas and (word[position+1] in vocales_cerradas or word[position+1] in semivocales)) or \
           (word[position] in vocales_cerradas and word[position+1] in vocales_abiertas)

def esTriptongo(position, word):
    if len(word) < position + 3:
        return False

    return (word[position] in vocales_cerradas and word[position+1] in vocales_abiertas and (word[position+2] in vocales_cerradas or word[position+2] in semivocales))

def gruposVocales(word):
    grupos = []
    jump = 0
    for position, caracter in enumerate(word):
        if jump:
            jump-=1
            continue

        if caracter in vocales_abiertas or caracter in vocales_cerradas:
            if esTriptongo(position, word):
                grupo = (position, word[position: position + 3])
                jump = 2
            elif esDiptongo(position, word):
                grupo = (position, word[position: position + 2])
                jump = 1
            else:
                grupo = (position, word[position])
                jump = 0
            grupos.append(grupo)
    
    return grupos

def hayConsonante(word, position, delante=True):
    if position < 0 or position >= len(word):
        return False

    if position == 0 and delante or position == len(word)-1 and not delante :
        return False

    position += -1 if delante else 1

    return word[position] in consonantes or (word[position] in semivocales if delante else False) 

def consonantesDelante(word, groups):
    if len(groups) == 0:
        return None

    for ix, group in enumerate(groups):
        if hayConsonante(word, group[0]):
            position = group[0]-1
            newGroup = (position, word[position] + group[1])
            groups[ix] = newGroup 

    return groups


