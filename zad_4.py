class Element:
    def __init__(self, x):
        self.podatak = x
        self.iduci = None


class Lista:
    def __init__(self):
        self.prvi = None
        self.zadnji = None
        self.trenutni = None
        self.broj_elemenata = 0

    def resetiraj(self):
        self.trenutni = self.prvi

    def iduci(self):
        if self.trenutni is None:
            self.resetiraj()
            return None
        x = self.trenutni
        self.trenutni = x.iduci
        return x

    def dodaj(self, element):
        x = Element(element)
        if self.zadnji:
            self.zadnji.iduci = x
            self.zadnji = x
        else:
            self.prvi = x
            self.zadnji = x
            self.trenutni = self.prvi
        self.broj_elemenata += 1


    def nadji(self, fn):
        return self.pom_funkcija(self, fn)

    def pom_funkcija(self, el, fn):
        pokazivac = el.prvi
        za_vratiti = ""
        if(fn(pokazivac)):
            return pokazivac.podatak
        while(pokazivac.iduci != None):
            if isinstance(pokazivac.iduci.podatak, Lista):
                za_vratiti = self.pom_funkcija(pokazivac.iduci.podatak, fn)
            else:
                if(fn(pokazivac.iduci)):
                    return pokazivac.iduci.podatak
            pokazivac = pokazivac.iduci
        if za_vratiti == "":
            return None
        else:
            return za_vratiti


    def obrisi(self, element):
        pokazivac = self.prvi
        if pokazivac.podatak == element:
            self.prvi = self.prvi.iduci
            self.zadnji = None
            self.broj_elemenata -= 1
        else:
            while(pokazivac.iduci != None):
                if pokazivac.iduci.podatak == element:
                    pokazivac.iduci = pokazivac.iduci.iduci
                    self.broj_elemenata -= 1
                pokazivac = pokazivac.iduci


    def tekstualno(self, string=""):
        pokazivac = self.prvi
        string += "<"
        while pokazivac:
            if isinstance(pokazivac.podatak, Lista):
                string += "; "
                string = pokazivac.podatak.tekstualno(string)
            else:
                if pokazivac == self.prvi:
                    string += str(pokazivac.podatak) + ""
                else:
                    string += "; " + str(pokazivac.podatak) + ""
            pokazivac = pokazivac.iduci
        string += ">"
        return string


x = Lista()
x.dodaj((1, 2))
print(x.tekstualno())  # ispisuje <(1, 2)>
x.obrisi((1, 2))
print(x.tekstualno())  # ispisuje <>
x.dodaj((1, 3))
print(x.tekstualno())  # ispisuje <(1, 3)>
x.dodaj((1, 4))
print(x.tekstualno())  # ispisuje <(1, 3); (1, 4)>
x.obrisi((1, 3))
print(x.tekstualno())  # ispisuje <(1, 4)>
x.obrisi((1, 4))
print(x.tekstualno())  # ispisuje <>

y = Lista()
y.dodaj('y1')
y.dodaj('y2')

z = Lista()
z.dodaj('z1')
z.dodaj('z2')
z.dodaj('z3')

y.dodaj(z)  # lista y sadrzi listu z kao element

x.dodaj(1)
x.dodaj(2)
x.dodaj(y)  # lista x sadrzi listu y kao element
x.dodaj(3)
x.dodaj(y)  # lista x sadrzi listu y kao element

# ispisuje <1; 2; <y1; y2; <z1; z2; z3>>; 3; <y1; y2; <z1; z2; z3>>>
print(x.tekstualno())

# x je tipa Element
r = x.nadji(lambda x: x.podatak == 'z3')
print(r)  # ispisuje z3
r = x.nadji(lambda x: x.podatak == 'abc')
print(r)  # ispisuje None
print(x.nadji(lambda x: x.podatak == 1))
print(x.nadji(lambda x: x.podatak == 4))
print(x.nadji(lambda x: x.podatak == 3))
print(x.nadji(lambda x: x.podatak == 2))
