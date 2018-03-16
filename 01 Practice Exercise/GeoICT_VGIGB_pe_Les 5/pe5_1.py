def convert(granden_celsius):
    fahrenheid = granden_celsius *1.8 + 32
    return fahrenheid

#print(convert(25))

def table():

    for celsius in range (-30, 40, 10):
        print(convert(celsius), celsius)

table()

