class Pakuri:
    def __init__(self, species):  #defines species, attack, defense and speed
        self.species = species
        self.attack = (len(species) * 7) + 9
        self.defense = (len(species) * 5) + 17
        self.speed = (len(species) * 6 )+ 13

    def get_species(self): #species returned
        return self.species
    def get_attack(self): #attack stat returned
        return self.attack
    def get_defense(self): #defense stat returned
        return self.defense
    def get_speed(self): #speed stat returned
        return self.speed
    def set_attack(self, new_attack): #new attack returned
        self.attack = new_attack
    def evolve(self): #if evolved then stats updated
        self.attack = 2 * self.attack
        self.defense = 4 * self.defense
        self.speed = 3 * self.speed

    def __lt__(self, other): #comparing species
        return self.species <= other.species

