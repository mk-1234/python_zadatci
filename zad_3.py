def palindrom(s):
    if(len(s) < 2):
        return True
    else:
        if(s[0] != s[len(s) - 1]):
            return False
        else:
            return palindrom(s[1:len(s) - 1])


def pretraga(naziv, niz):
    if naziv in niz:
        return "Nalazi se u listi"
    else:
        for elem in niz:
            if isinstance(elem, list):
                return pretraga(naziv, elem)
        return "Nije pronadeno u listi"



def preokreni(l):
    if(len(l) <= 1):
        return l
    else:
        print("l(-1) = ", l[-1], "; l(0) =", l[0])
        return [l[-1]] + preokreni(l[1:len(l) - 1]) + [l[0]]
        

def pronadi(l, n, index_prvog, index_zadnjeg):
    if (index_zadnjeg + 1 - index_prvog > 0):
        pocetak = index_prvog
        kraj = index_zadnjeg
        sredina = (pocetak + kraj) // 2
        if(n != l[sredina]):
            if(n < l[sredina]):
                return pronadi(l, n, pocetak, sredina - 1)
            else:
                return pronadi(l, n, sredina + 1, kraj)
        else:
            print("Postoji broj!")
            return sredina
    else:
        return " --> Ne postoji broj!"


if __name__ == '__main__':
    lista = [2, 4, 5, 7, 12, 13, 16, 22, 28, 33]
    print("Broj 7 se nalazi u listi na mjestu", pronadi(lista, 7, 0, len(lista)))
    lista = [2, 4, 5, 7, 12, 13, 16, 22, 28, 33]
    print("Broj 10 se nalazi u listi na mjestu", pronadi(lista, 10, 0, len(lista)))
    lista = [2, 4, 5, 7, 12, 13, 16, 22, 28, 33]
    print("Broj 28 se nalazi u listi na mjestu", pronadi(lista, 28, 0, len(lista)))

    print("-----------------------")

    lista = ['abc', 'bcd', ['def', 'fgh', 'ijk', ['qwe', 'rtz', ['vbn', 'cxv', 'ayx'], 'wer']], 'klm', 'nop']
    strings = ["ayx", "tgb", "bcd", "vbn", "ewq", "klm"]
    for s in strings:
        print(s, "-->", pretraga(s, lista))
    
    print("-----------------------")

    lista = [3, 6, 4, 19, 31, 77, 21, 86, 140, 2, 56, 7, 12, 14, 9]
    print(preokreni(lista))
    lista = [1, 72, 9, 80, 31, 12, 14, 1251, 29]
    print(preokreni(lista))

    print("-----------------------")

    strings = ["prvistring", "qwewq", "trecistringgnirtsicert", "cetvrti"]
    for s in strings:
        print(s, ":", palindrom(s))