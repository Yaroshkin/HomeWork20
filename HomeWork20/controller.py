import model
import view2 as v

n = model.start()
credit = 100

def controllerLoop():
    global credit
    u = v.getThrow()
    if u == 's':
        cube = model.start()
        print("🎲:",cube)
        s = model.credit(credit,cube)
        credit = s
        print("💸:",s)
        message, result = model.check(s)
        v.viewMassage(message)
        


def main():
    v.viewMassage('Игра в кости ')
    result = False
    v.getLoop()()
    

if __name__ == '__main__':
    main()