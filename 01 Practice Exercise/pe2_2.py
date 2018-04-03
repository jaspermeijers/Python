cijferICT=eval(input('Cijfer Geo-ICT?'))
cijferDATA_R=eval(input('Cijver Geo_DATA Regine?'))
cijferDATA_H=eval(input('Cijfer Geo_DATA Hiddo?'))
cijferPRO=eval(input('Cijfer Geo_PRO?'))

gemiddelde=str((cijferPRO+cijferDATA_H+cijferICT+cijferDATA_R)/4)
beloning=str(cijferICT*30 +cijferDATA_R*30 +cijferDATA_H*30 +cijferPRO*30)

print('Met cijfers (gemiddeld een '+gemiddelde + ') leveren een beloning van €' +beloning + ' op!')