def calorie_calc(vol, abv):
    return vol*(abv*10)*.25


def start():
    vol = input("How many oz ?: ")
    abv = input("What ABV?: ")
    cals = calorie_calc(float(vol), float(abv))
    print("Consumed {} calories".format(round(int(cals), -1)))


while 1:
    start()
