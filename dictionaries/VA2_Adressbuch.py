class Adressbuch:
    def __init__(self):
        self.adressbuch = {}

    def person_hinzufuegen(self, name, email, telefonnummer):
        self.adressbuch[name] = {"Email": email, "Telefonnummer": telefonnummer}

    def person_loeschen(self, name):
        if name in self.adressbuch:
            del self.adressbuch[name]
            print(name," wurde aus dem Adressbuch gelöscht.")
        else:
            print(name, " wurde nicht im Adressbuch gefunden.")

    def kontaktdaten_suchen(self, name):
        if name in self.adressbuch:
            kontakt = self.adressbuch[name]
            print("Kontaktdaten von", name)
            print("Email:", kontakt['Email'])
            print("Telefonnummer:", kontakt['Telefonnummer'])
        else:
            print(name, " wurde nicht im Adressbuch gefunden.")

    def informationen_aktualisieren(self, name, email=None, telefonnummer=None):
        if name in self.adressbuch:
            kontakt = self.adressbuch[name]
            if email:
                kontakt['Email'] = email
            if telefonnummer:
                kontakt['Telefonnummer'] = telefonnummer
            print("Informationen von ", name, " wurden aktualisiert.")
        else:
            print(name," wurde nicht im Adressbuch gefunden.")


# Beispielverwendung
adressbuch = Adressbuch()

adressbuch.person_hinzufuegen("Max Mustermann", "max.mustermann@example.com", "123456789")
adressbuch.person_hinzufuegen("Erika Musterfrau", "erika.musterfrau@example.com", "987654321")

adressbuch.kontaktdaten_suchen("Max Mustermann")
adressbuch.kontaktdaten_suchen("Erika Musterfrau")

adressbuch.informationen_aktualisieren("Max Mustermann", email="max.mustermann@newemail.com")
adressbuch.kontaktdaten_suchen("Max Mustermann")

adressbuch.person_loeschen("Erika Musterfrau")
adressbuch.kontaktdaten_suchen("Erika Musterfrau")