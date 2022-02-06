def frekv_sort(l):
    pomocna_lista = []
    ponavljanja_lista = []
    for i in range(len(l)):
        br_pon = 0
        for j in range(len(l)):
            if l[i] == l[j]:
                br_pon += 1
        if len(pomocna_lista) == 0:
            pomocna_lista += [l[i]]
            ponavljanja_lista += [br_pon]
        else:
            pom_brojac = 0
            for j in range(len(pomocna_lista)):
                if l[i] != pomocna_lista[j]:
                    pom_brojac += 1
                if pom_brojac == len(pomocna_lista):
                    pomocna_lista += [l[i]]
                    ponavljanja_lista += [br_pon]
    najveci = ponavljanja_lista[0]
    for i in range(len(ponavljanja_lista)):
        najveci = ponavljanja_lista[i]
        najv_index = i
        promjena = 0
        for j in range(i + 1, len(ponavljanja_lista)):
            if ponavljanja_lista[j] > najveci:
                najveci = ponavljanja_lista[j]
                najv_index = j
                promjena = 1
        if promjena == 1:
            temp = najveci
            x = najv_index - 1
            while x >= i:
                ponavljanja_lista[x + 1] = ponavljanja_lista[x]
                x -= 1
            ponavljanja_lista[i] = temp
            temp = pomocna_lista[najv_index]
            x = najv_index - 1
            while x >= i:
                pomocna_lista[x + 1] = pomocna_lista[x]
                x -= 1
            pomocna_lista[i] = temp
    konacna_lista = []
    for i in range(len(pomocna_lista)):
        for j in range(ponavljanja_lista[i]):
            konacna_lista += [pomocna_lista[i]]
    print(konacna_lista)


if __name__ == '__main__':
    frekv_sort([4, 4, 1, 5, 4, 1, 8, 2])
    print()
    frekv_sort([4, 4, 1, 5, 4, 1, 8, 2, 2, 2, 2])
    print()
    frekv_sort([4, 4, 1, 5, 4, 1, 1, 1, 8, 2])
    print()
    frekv_sort([4, 3, 3, 3, 3, 3, 3, 1, 1, 4, 4, 4, 4, 2, 2, 1, 5, 4, 1, 1, 1, 8, 2])
    #[4, 4, 4, 1, 1, 5, 8, 2]  # ispis
