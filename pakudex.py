from pakuri import *
class Pakudex:
    def __init__(self, capacity = 20): #define capapcity and size and a empty list
        self.capacity = capacity
        self.size = 0
        self.pakulist = []
    def get_size(self): #size returned
        return self.size
    def get_capacity(self): #capacity returned
        return self.capacity
    def get_species_array(self): #when there are species the names are returned in order in the list
        if self.size > 0:
            for each_pakuri in self.pakulist:
                return each_pakuri.get_species()
        else:
            return None

    def get_stats(self, species): #stats of each species returned if there are species
        for each_pakuri in self.pakulist:
                if each_pakuri.get_species() == species: #checks if the names are equal to each other, then stats printed
                    return [each_pakuri.get_attack(), each_pakuri.get_defense(), each_pakuri.get_speed()]
        return None

    def sort_pakuri(self):
        def sorting_key(pakuri):
            return pakuri.get_species()

        self.pakulist.sort(key = sorting_key)
        print("Pakuri have been sorted!")

    def add_pakuri(self, species):
        if self.size == self.capacity:
            return False  #can't add anymore

        for each_pakuri in self.pakulist:
            if each_pakuri.get_species() == species:
                return False  #if we already added a species don't add it again

        self.pakulist.append(Pakuri(species))
        self.size += 1  #increase size for each added Pakuri
        return True
    def evolve_species(self, species): #evolving species as long as species in list is the right one
        for each_pakuri in self.pakulist:
            if each_pakuri.get_species() == species:
                each_pakuri.evolve()
                return True
        return False