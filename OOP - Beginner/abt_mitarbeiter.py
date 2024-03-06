class Mitarbeiter:
    def __init__(self, name, position, alter):
        self.name = name
        self.position = position
        self.alter = alter
    
    def __str__(self):
        return f"{self.name}"

class Abteilung:
    def __init__(self, abteilungsname):
        self.abteilungsname = abteilungsname
        self.mitarbeiter_liste = []
    
    def mitarbeiter_hinzufuegen(self, mitarbeiter):
        self.mitarbeiter_liste.append(mitarbeiter)
    
    def mitarbeiter_auflisten(self):
        for mitarbeiter in self.mitarbeiter_liste:
            print(mitarbeiter, mitarbeiter.alter)
    def durchschnittsalter(self):
        alter_summe = 0
        for mitarbeiter in self.mitarbeiter_liste:
            alter_summe += mitarbeiter.alter
        return alter_summe / len(self.mitarbeiter_liste)

# Testaufrufe
# Erstellung von Mitarbeitern
mitarbeiter1 = Mitarbeiter("Max Mustermann", "Entwickler", 25)
mitarbeiter2 = Mitarbeiter("Erika Musterfrau", "Projektmanagerin", 30)
mitarbeiter3 = Mitarbeiter("Hans Peter", "Marketing Manager", 35)
# Erstellung einer Abteilung und Hinzufügen von Mitarbeitern
abteilungIT = Abteilung("IT")
abteilungMarketing = Abteilung("Marketing")
abteilungIT.mitarbeiter_hinzufuegen(mitarbeiter1)
abteilungIT.mitarbeiter_hinzufuegen(mitarbeiter2)
abteilungMarketing.mitarbeiter_hinzufuegen(mitarbeiter3)

# Auflistung der Mitarbeiter in der Abteilung
abteilungIT.mitarbeiter_auflisten()
print (abteilungIT.durchschnittsalter())
