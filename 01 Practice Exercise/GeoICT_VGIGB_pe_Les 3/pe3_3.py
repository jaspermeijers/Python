leeftijd=eval(input('geef je leeftijd: '))
paspoort=(input('Nederlands paspoort: '))

if leeftijd >=18 and paspoort == 'ja':
    print('Gefeliciteerd je mag stemmen')
else:
    print('Sorry je mag niet stemmen')