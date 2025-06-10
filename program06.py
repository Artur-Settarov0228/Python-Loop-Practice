from random import randint
maxfiy = randint(1,7)
i = 0
while i < 3 :
    son = input("son kiriting")
    i += 1
    if son == maxfiy:
        print("tugri")
        break
    else:
        print("xato")