class Fahrzeug:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def display_info(self):
        print(f"Maximale Geschwindigkeit: {self.max_speed} km/h")
        print(f"Gefahrene Kilometer: {self.mileage} km")

# Beispielverwendung
auto = Fahrzeug(200, 50000)
auto.display_info()