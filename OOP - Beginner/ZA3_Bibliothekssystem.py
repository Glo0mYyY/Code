class Buch:
    def __init__(self, titel, autor, isbn):
        self.titel = titel
        self.autor = autor
        self.isbn = isbn
    
    def info(self):
        return f"Titel: {self.titel}, Autor: {self.autor}, ISBN: {self.isbn}"

class Bibliothek:
    def __init__(self, name):
        self.name = name
        self.bestand = []
    
    def buch_hinzufuegen(self, buch):
        for b in self.bestand:
            if b.isbn == buch.isbn:
                return
        self.bestand.append(buch)
    
    def buch_entfernen(self, isbn):
        for buch in self.bestand:
            if buch.isbn == isbn:
                self.bestand.remove(buch)
                return
    
    def suche_nach_titel(self, titel):
        result = []
        for buch in self.bestand:
            if titel in buch.titel:
                result.append(buch)
        return result
    
    def anzeigen_aller_buecher(self):
        for buch in self.bestand:
            print(buch.info())

buch1 = Buch("Harry Potter", "J.K. Rowling", "123123")
buch2 = Buch("The Hobbit", "J.R.R. Tolkien", "14141414")
buch3 = Buch("To Kill a Mockingbird", "Harper Lee", "1515151515")

bibliothek = Bibliothek("HFTM Bibliothek")
bibliothek.buch_hinzufuegen(buch1)
bibliothek.buch_hinzufuegen(buch2)
bibliothek.buch_hinzufuegen(buch3)

bibliothek.anzeigen_aller_buecher()