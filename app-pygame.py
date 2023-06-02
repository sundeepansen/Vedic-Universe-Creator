import math
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

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
def create_universe(cosmic_body, cosmic_type, orbit, mass, radius, planet):
    vedicUniverse.addCosmicBody(cosmic_body)
    if cosmic_type == "Moon":
        moon = Moon(cosmic_body, orbit, mass, radius, planet)
        vedicUniverse.addCosmicBody(moon)

class VedicUniverseCreatorApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.cosmic_bodies_label = Label(text="Cosmic Bodies in the Vedic Universe:")
        layout.add_widget(self.cosmic_bodies_label)
        self.cosmic_bodies_list = Label(text="")
        layout.add_widget(self.cosmic_bodies_list)
        self.cosmic_body_input = TextInput(multiline=False, hint_text="Cosmic Body Name")
        layout.add_widget(self.cosmic_body_input)
        self.cosmic_type_input = TextInput(multiline=False, hint_text="Cosmic Body Type (e.g., Planet, Moon)")
        layout.add_widget(self.cosmic_type_input)
        self.orbit_input = TextInput(multiline=False, hint_text="Orbit (e.g., Solar, Earth)")
        layout.add_widget(self.orbit_input)
        self.mass_input = TextInput(multiline=False, hint_text="Mass (in kg)")
        layout.add_widget(self.mass_input)
        self.radius_input = TextInput(multiline=False, hint_text="Radius (in meters)")
        layout.add_widget(self.radius_input)
        self.planet_input = TextInput(multiline=False, hint_text="Planet (for Moons only)")
        layout.add_widget(self.planet_input)
        self.add_cosmic_body_button = Button(text="Add Cosmic Body", on_press=self.add_cosmic_body)
        layout.add_widget(self.add_cosmic_body_button)
        return layout

    def add_cosmic_body(self, instance):
        cosmic_body = self.cosmic_body_input.text
        cosmic_type = self.cosmic_type_input.text
        orbit = self.orbit_input.text
        mass = float(self.mass_input.text)
        radius = float(self.radius_input.text)
        planet = self.planet_input.text if cosmic_type == "Moon" else ""
        create_universe(cosmic_body, cosmic_type, orbit, mass, radius, planet)
        self.update_cosmic_bodies_list()

    def update_cosmic_bodies_list(self):
        cosmic_bodies = [str(cosmic_body) for cosmic_body in vedicUniverse.getCosmicBodies()]
        self.cosmic_bodies_list.text = '\n'.join(cosmic_bodies)

# Start creating the universe
print("Welcome to the Vedic Universe Creator!")
vedicUniverse = Universe()
VedicUniverseCreatorApp().run()
print("Universe creation complete!")
