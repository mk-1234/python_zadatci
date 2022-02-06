def dubina_elementa(znak, l, dubina = -1, velicina_liste = -1, broj = -1):
    dubina += 1
    if velicina_liste < 0:
        velicina_liste = len(l)
    for i in range(len(l)):
        if(znak == l[i]):
            print("Dubina elementa", znak, "je", dubina)
            return 1
        else:
            if isinstance(l[i], list):
                if dubina_elementa(znak, l[i], dubina, velicina_liste, broj):
                    return 1
            else:
                if i == velicina_liste - 1:
                    if broj != 1:
                        print("Element", znak, "se ne nalazi u listi.")



if __name__ == '__main__':
    dubina_elementa('g', ['a', [['b', 'c'], 'd', ['e']], 'f'])
    dubina_elementa('d', ['a', [['b', 'c'], 'd', ['e']], 'f'])
    dubina_elementa('f', ['a', [['b', 'c'], 'd', ['e']], 'f'])
    dubina_elementa('c', ['a', [['b', 'c'], 'd', ['e']], 'f'])
    
    dubina_elementa('j', ['a', [['b', 'c'], 'd', ['e']], 'f', 'i', 'j', ['k', 'l', 'm', ['n', 'o']]])
    dubina_elementa('o', ['a', [['b', 'c'], 'd', ['e']], 'f', 'i', 'j', ['k', 'l', 'm', ['n', 'o']]])
    dubina_elementa('z', ['a', [['b', 'c'], 'd', ['e']], 'f', 'i', 'j', ['k', 'l', 'm', ['n', 'o']]])
    dubina_elementa('m', ['a', [['b', 'c'], 'd', ['e']], 'f', 'i', 'j', ['k', 'l', 'm', ['n', 'o']]])
    dubina_elementa('e', ['a', [['b', 'c'], 'd', ['e']], 'f', 'i', 'j', ['k', 'l', 'm', ['n', 'o']]])