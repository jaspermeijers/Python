def kwadraten_som(grondgetallen):
    'dit is een list [ ] met integers'
    kwadraten = []
    for positief in grondgetallen:
        if positief >0:
            kwadraten.append(positief**2)
    return sum(kwadraten)

print(kwadraten_som([4,5,3,-81]))
