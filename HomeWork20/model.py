from random import randint

def start(end=6):
    return randint(1, end)

def credit(credit,cube):
    if cube == 6:
        credit +=3
        return credit
    else:
        credit -= 1
        return credit

def check(credit):
    if credit > 0 :
        return f'Игра продолжается \u2705 {credit} \nКубик 🎲 : {start()}', True
    elif credit <= 0 :
        return f'Не хватает средст \u274C {credit}', False
    
