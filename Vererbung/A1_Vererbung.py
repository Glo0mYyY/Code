class Fahrzeug:
    def __init__(self, anzahlSitze):
        self.sitze = anzahlSitze
        self.standardTarif = self.sitze * 100
    def tarif(self):
        return self.standardTarif
    
class Bus(Fahrzeug):
    def __init__(self, anzahlSitze):
        super().__init__(anzahlSitze)
        self.standardTarif = self.standardTarif * 1.1

    
vwbus = Bus(10)
print("Gesamtfahrpreis = ", vwbus.tarif(), "CHF")
vwbeetle = Fahrzeug(4)
print("Gesamtfahrpreis = ", vwbeetle.tarif(), "CHF")