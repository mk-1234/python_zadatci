class Element:
    def __init__(self, x):
        self.elem = x
        self.sljedeci = None

        
class Lista:
    def __init__(self):
        self.head = None
        self.tail = None
        self.pointer = self.head
        self.velicina = 0
        
    def dodaj(self, el):
        e = Element(el)
        if(self.head == None):
            self.head = e
            self.pointer = self.head
        if(self.tail == None):
            self.tail = e
            self.velicina += 1
        else:
            self.tail.sljedeci = e
            self.tail = e
            self.velicina += 1
    
    def dodaj_na_pocetak(self, el):
        e = Element(el)
        if(self.velicina == 0):
            self.head = e
            self.pointer = self.head
            self.tail = e
            self.velicina += 1
        else:
            e.sljedeci = self.head
            self.head = e
            self.pointer = self.head
            self.velicina += 1
            
    def izbrisi(self):
        if(self.velicina > 0):
            self.head = self.head.sljedeci
            self.pointer = self.head
            self.velicina -= 1
        else:
            print("Nije moguće izbacivanje prvog elementa, nema elemenata u listi!")
    
    def izbrisi_zadnji(self):
        if(self.velicina == 0):
            print("Nije moguće izbacivanje zadnjeg elementa, nema elemenata u listi!")
        else:
            if(self.velicina > 1):
                self.pomocni = self.head
                while(self.pomocni.sljedeci != self.tail):
                    self.pomocni = self.pomocni.sljedeci
                self.pomocni.sljedeci = None
                self.tail = self.pomocni
                self.velicina -= 1
            else:
                self.head = None
                self.tail = None
                self.pointer = self.head
                self.velicina -= 1
            
    
    def ispis(self):
        if(self.velicina > 0):
            print(self.head.elem)
            while(self.pointer.sljedeci != None):
                print(self.pointer.sljedeci.elem)
                self.pointer = self.pointer.sljedeci
        else:
            print("Lista je prazna!")
    
    
if __name__ == '__main__':
    l = Lista()
    l.dodaj(2)
    l.dodaj(3)
    l.izbrisi()
    l.dodaj(6)
    l.dodaj(13)
    l.izbrisi_zadnji()
    l.ispis()
    print('------')
    l.izbrisi()
    l.izbrisi_zadnji()
    l.izbrisi_zadnji()
    l.izbrisi()
    l.dodaj(5)
    l.dodaj_na_pocetak(22)
    l.dodaj(4)
    l.izbrisi()
    l.dodaj_na_pocetak(17)
    l.dodaj(1)
    l.izbrisi_zadnji()
    print('------')
    l.ispis()