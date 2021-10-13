dagen = ['Maandag', 'Dinsdag', 'Woensdag', 'Donderdag', 'Vrijdag', 'Zaterdag', 'Zondag']
print('Dit zijn de dagen van de week:')
for x in dagen:
    print(x)
print('Dit zijn alle werk dagen:')
werkdagen = (dagen[0:4])
for x in werkdagen:
    print(x)
weekenddagen = (dagen[5:7])
print('Dit zijn alle weekend dagen:')
for x in weekenddagen:
    print(x)

reverseweek = dagen
reverseweek.reverse()
print('Dit zijn alle dagen omgekeerd:')
for x in weekenddagen:
    print(x)
print('Dit zijn de weekend dagen omgekeerd:')
reverseweekend = dagen[-6] , dagen[-7]
print(reverseweekend)