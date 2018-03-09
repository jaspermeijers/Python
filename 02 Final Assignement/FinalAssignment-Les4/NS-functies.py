def standaardprijs (afstandKM):
    '80cent pkm, rit >50km 15,-+60 pkm,bij invoer negatieve afstand 0 euro'
    if afstandKM <0:
        prijs = afstandKM*0
    elif afstandKM <50:
        prijs = afstandKM*80/100
    else:
        prijs = afstandKM+15*60/100
    return prijs

print(standaardprijs(51))


def ritprijs(leeftijd, dag, afstandKM):
    'op werkdagen reizen kinderen <12 en ouderen >65 met 30% korting'

    doordeweeks = ['maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag']
    weekend = ['zaterdag', 'zondag']
    normale_prijs=standaardprijs(afstandKM)

    if leeftijd <12 and dag in doordeweeks:
        betaald = normale_prijs/100*70
    elif leeftijd >65 and dag in doordeweeks:
        betaald = normale_prijs/100*70

    elif leeftijd <12 and dag in weekend:
        betaald = normale_prijs/100*65
    elif leeftijd >65 and dag in weekend:
        betaald = normale_prijs/100*65

    elif leeftijd and dag in weekend:
        betaald = normale_prijs/100*60
    else:
        betaald =normale_prijs
    return betaald
print(ritprijs(11,'maandag',51))
