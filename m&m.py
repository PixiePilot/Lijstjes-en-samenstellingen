import random
def mEnm(amount):
    bag = []
    for x in range(amount):
        colors = ['oranje', 'blauw', 'groen', 'bruin']
        random.shuffle(colors)
        bag.append(colors[0])
    orange = []
    blauw = []
    groen = []
    bruin = []
    for x in bag:
        if 'oranje' in x:
            orange.append(x)
    for x in bag:
        if 'blauw' in x:
            blauw.append(x)
    for x in bag:
        if 'groen' in x:
            groen.append(x)
    for x in bag:
        if 'bruin' in x:
            bruin.append(x)
    orangelen = len(orange)
    blauwlen = len(blauw)
    groenlen= len(groen)
    bruinlen = len(bruin)
    dictMM = {
        'Oranje': (orangelen),
        'Groen ': (groenlen),
        'Blauw ': (blauwlen),
        'Bruin ': (bruinlen),
    }
    a = sorted(dictMM.items(), key=lambda x: x[1])       
    return a


print(mEnm(10))





