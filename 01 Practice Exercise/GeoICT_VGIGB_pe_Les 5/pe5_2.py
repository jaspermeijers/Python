kaartnummers =open('pe5_2_kaartnummers', 'r')
#dit opent op de achtergrond de text file

lijst=kaartnummers.readlines()
#lijst met regels

for regel in lijst:
    fl = regel.split(',')
    naam=('{:1} heeft kaartnummer: {:1}'.format(fl[1].strip(), fl[0]))
    print(naam)
