lst = '5-9-7-1-7-8-3-2-4-8-7-9'

ploeg = lst.split('-')
invoer = [ ]

for char in ploeg:
    getal = int(char)
    invoer.append(getal)

print('Gesorteerde list van ints: ' + invoer.sort())
print('Grootste getal: ' + max(invoer) + ' en Kleinste getal: ' + min(invoer))
print('Aantal getallen: ' + str(len(invoer)) + ' en Som van de getallen: ' + str(sum(invoer)))
print('Gemiddelde: ' + average(invoer))

