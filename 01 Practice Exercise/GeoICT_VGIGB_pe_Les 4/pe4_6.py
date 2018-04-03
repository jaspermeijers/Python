def wijzig(letterlijst):
    'Zorg dat de functie de lijst leegt en de letters [ ‘d’, ‘e’, ‘f’ ] toevoegt. Er is geen return-waarde!'
    letterlijst.remove('a')
    letterlijst.remove('b')
    letterlijst.remove('c')
    letterlijst.append('d')
    letterlijst.append('e')
    letterlijst.append('f')

lijst = ['a', 'b', 'c']
print(lijst)
wijzig(lijst)
print(lijst)
