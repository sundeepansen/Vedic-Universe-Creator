import math
import ephem
import random

class Universe:
    def __init__(self):
        self.cosmicBodies = []

    def addCosmicBody(self, cosmicBody):
        self.cosmicBodies.append(cosmicBody)

    def removeCosmicBody(self, cosmicBody):
        self.cosmicBodies.remove(cosmicBody)

    def getCosmicBodies(self):
        return self.cosmicBodies

class CosmicBody:
    def __init__(self, name):
        self.name = name
        self.position = (0, 0, 0)

    def getName(self):
        return self.name

    def setPosition(self, x, y, z):
        self.position = (x, y, z)

    def getPosition(self):
        return self.position

    def calculateDistance(self, otherBody):
        x1, y1, z1 = self.position
        x2, y2, z2 = otherBody.position
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
        return distance

    def getMass(self):
        return 0  # Placeholder for mass calculation

    def getRadius(self):
        return 0  # Placeholder for radius calculation

    def __str__(self):
        return self.name

class Planet(CosmicBody):
    def __init__(self, name, orbit, mass, radius):
        super().__init__(name)
        self.orbit = orbit
        self.mass = mass
        self.radius = radius

    def getOrbit(self):
        return self.orbit

    def getMass(self):
        return self.mass

    def getRadius(self):
        return self.radius

    def __str__(self):
        return f"{self.name} (Orbit: {self.orbit}, Mass: {self.mass} kg, Radius: {self.radius} m)"

class Moon(CosmicBody):
    def __init__(self, name, orbit, mass, radius, planet):
        super().__init__(name)
        self.orbit = orbit
        self.mass = mass
        self.radius = radius
        self.planet = planet

    def getOrbit(self):
        return self.orbit

    def getMass(self):
        return self.mass

    def getRadius(self):
        return self.radius

    def getPlanet(self):
        return self.planet

    def __str__(self):
        return f"{self.name} (Orbit: {self.orbit}, Mass: {self.mass} kg, Radius: {self.radius} m, Planet: {self.planet})"

# Function to create the universe dynamically
def create_universe():
    vedicUniverse = Universe()

    sun = Star("Sun", 5778, 1.989e30, 696340000)
    sun.setPosition(0, 0, 0)
    vedicUniverse.addCosmicBody(sun)

    # Interact with ChatGPT to create cosmic bodies
    while True:
        cosmic_body = input("Enter the name of a cosmic body (or 'done' to finish): ")
        if cosmic_body == "done":
            break

        cosmic_type = input("Enter the type of cosmic body (e.g., Planet, Moon): ")
        orbit = input("Enter the orbit (e.g., Solar, Earth): ")
        mass = float(input("Enter the mass in kg: "))
        radius = float(input("Enter the radius in meters: "))

        if cosmic_type == "Planet":
            planet = Planet(cosmic_body, orbit, mass, radius)
            vedicUniverse.addCosmicBody(planet)
            print(f"Added {cosmic_body} as a planet to the universe.")
        elif cosmic_type == "Moon":
            planet = input("Enter the planet it orbits: ")
            moon = Moon(cosmic_body, orbit, mass, radius, planet)
            vedicUniverse.addCosmicBody(moon)
            print(f"Added {cosmic_body} as a moon of {planet} to the universe.")
        else:
            print("Invalid cosmic body type. Skipping...")

    # Display the cosmic bodies in the universe
    print("\nCosmic bodies in the Vedic universe:")
    for cosmic_body in vedicUniverse.getCosmicBodies():
        print(cosmic_body)

# Start creating the universe
print("Welcome to the Vedic Universe Creator!")
create_universe()
print("Universe creation complete!")
