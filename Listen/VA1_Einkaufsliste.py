class Einkaufsliste:
    def __init__(self):
        self.einkaufsliste = []

    def artikel_hinzufuegen(self, artikel):
        if artikel not in self.einkaufsliste:
            self.einkaufsliste.append(artikel)
            print(artikel, " wurde zur Einkaufsliste hinzugefügt.")
        else:
            print(artikel, " ist bereits in der Einkaufsliste.")

    def artikel_entfernen(self, artikel):
        if artikel in self.einkaufsliste:
            self.einkaufsliste.remove(artikel)
            print(artikel, " wurde aus der Einkaufsliste entfernt.")
        else:
            print(artikel, " ist nicht in der Einkaufsliste.")

    def liste_anzeigen(self):
        if len(self.einkaufsliste) > 0:
            print("Einkaufsliste:")
            for artikel in self.einkaufsliste:
                print(artikel)
        else:
            print("Die Einkaufsliste ist leer.")

# Beispielverwendung
einkaufsliste = Einkaufsliste()
einkaufsliste.artikel_hinzufuegen("Orange")
einkaufsliste.artikel_hinzufuegen("Ei")
einkaufsliste.artikel_hinzufuegen("Orange")  # Duplikat, wird nicht hinzugefügt
einkaufsliste.liste_anzeigen()
einkaufsliste.artikel_entfernen("Ei")
einkaufsliste.liste_anzeigen()
