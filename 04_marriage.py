import random
boys = {"ali", "reza", "yasin", "benyamin", "mehrdad", "sajjad", "aidin", "shahin"}
girls = {"sara", "zari", "neda", "homa", "eli", "goli", "mary", "mina"}
marriage = []
toole_bazeh_boys = len(boys)
toole_bazeh_girls = len(girls)
if toole_bazeh_boys == toole_bazeh_girls:
    while toole_bazeh_boys > 0:
        rand_boys = random.choice(tuple(boys))
        rand_girls = random.choice(tuple(girls))
        marriage.append((rand_boys,rand_girls))
        boys.remove(rand_boys)
        girls.remove (rand_girls)
        toole_bazeh_boys = toole_bazeh_boys - 1
    print (marriage)
else:
    print ("One person will be single! Change the lists and try again later.")