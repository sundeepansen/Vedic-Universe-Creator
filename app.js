// Universe object
var vedicUniverse = {
    cosmicBodies: [],
    addCosmicBody: function(cosmicBody) {
        this.cosmicBodies.push(cosmicBody);
    },
    removeCosmicBody: function(cosmicBody) {
        var index = this.cosmicBodies.indexOf(cosmicBody);
        if (index !== -1) {
            this.cosmicBodies.splice(index, 1);
        }
    },
    getCosmicBodies: function() {
        return this.cosmicBodies;
    }
};

// CosmicBody constructor
function CosmicBody(name) {
    this.name = name;
    this.position = [0, 0, 0];
}
CosmicBody.prototype.getName = function() {
    return this.name;
};
CosmicBody.prototype.setPosition = function(x, y, z) {
    this.position = [x, y, z];
};
CosmicBody.prototype.getPosition = function() {
    return this.position;
};
CosmicBody.prototype.calculateDistance = function(otherBody) {
    var x1 = this.position[0];
    var y1 = this.position[1];
    var z1 = this.position[2];
    var x2 = otherBody.position[0];
    var y2 = otherBody.position[1];
    var z2 = otherBody.position[2];
    var distance = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2) + Math.pow(z2 - z1, 2));
    return distance;
};
CosmicBody.prototype.getMass = function() {
    return 0; // Placeholder for mass calculation
};
CosmicBody.prototype.getRadius = function() {
    return 0; // Placeholder for radius calculation
};
CosmicBody.prototype.toString = function() {
    return this.name;
};

// Planet constructor
function Planet(name, orbit, mass, radius) {
    CosmicBody.call(this, name);
    this.orbit = orbit;
    this.mass = mass;
    this.radius = radius;
}
Planet.prototype = Object.create(CosmicBody.prototype);
Planet.prototype.constructor = Planet;
Planet.prototype.getOrbit = function() {
    return this.orbit;
};
Planet.prototype.getMass = function() {
    return this.mass;
};
Planet.prototype.getRadius = function() {
    return this.radius;
};
Planet.prototype.toString = function() {
    return this.name + " (Orbit: " + this.orbit + ", Mass: " + this.mass + " kg, Radius: " + this.radius + " m)";
};

// Moon constructor
function Moon(name, orbit, mass, radius, planet) {
    CosmicBody.call(this, name);
    this.orbit = orbit;
    this.mass = mass;
    this.radius = radius;
    this.planet = planet;
}
Moon.prototype = Object.create(CosmicBody.prototype);
Moon.prototype.constructor = Moon;
Moon.prototype.getOrbit = function() {
    return this.orbit;
};
Moon.prototype.getMass = function() {
    return this.mass;
};
Moon.prototype.getRadius = function() {
    return this.radius;
};
Moon.prototype.getPlanet = function() {
    return this.planet;
};
Moon.prototype.toString = function() {
    return this.name + " (Orbit: " + this.orbit + ", Mass: " + this.mass + " kg, Radius: " + this.radius + " m, Planet: " + this.planet + ")";
};

// Function to create the cosmic body and update the UI
function createCosmicBody() {
    var cosmicBodyInput = document.getElementById("cosmicBody");
    var cosmicTypeInput = document.getElementById("cosmicType");
    var orbitInput = document.getElementById("orbit");
    var massInput = document.getElementById("mass");
    var radiusInput = document.getElementById("radius");
    var planetInput = document.getElementById("planet");

    var cosmicBody = cosmicBodyInput.value;
    var cosmicType = cosmicTypeInput.value;
    var orbit = orbitInput.value;
    var mass = parseFloat(massInput.value);
    var radius = parseFloat(radiusInput.value);
    var planet = cosmicType === "Moon" ? planetInput.value : "";

    if (cosmicType === "Planet") {
        var planetObj = new Planet(cosmicBody, orbit, mass, radius);
        vedicUniverse.addCosmicBody(planetObj);
    } else if (cosmicType === "Moon") {
        var moonObj = new Moon(cosmicBody, orbit, mass, radius, planet);
        vedicUniverse.addCosmicBody(moonObj);
    } else {
        console.log("Invalid cosmic body type. Skipping...");
    }

    updateCosmicBodiesList();
}

// Function to update the list of cosmic bodies in the UI
function updateCosmicBodiesList() {
    var cosmicBodiesList = document.getElementById("cosmicBodies");
    cosmicBodiesList.innerHTML = "";

    vedicUniverse.getCosmicBodies().forEach(function(cosmicBody) {
        var listItem = document.createElement("li");
        listItem.textContent = cosmicBody.toString();
        cosmicBodiesList.appendChild(listItem);
    });
}
