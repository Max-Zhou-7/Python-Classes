from Animal import Animal
class AnimalShelter:
    def __init__(self):
        self.animalShelter = {}
    def addAnimal(self, animal):
        if self.animalShelter.get(animal.species) == None:
            self.animalShelter[animal.species] = [animal]
        else:
            self.animalShelter[animal.species].append(animal)
    
    def removeAnimal(self, animal):
        for i in self.animalShelter.get(animal.species):
            if i.species == animal.species and i.name == animal.name and i.weight == animal.weight and i.age == animal.age:
                self.animalShelter.get(animal.species).remove(animal)
    
    def removeSpecies(self, species):
        species = species.upper()
        if self.animalShelter.get(species) != None:
            self.animalShelter.pop(species)
    def getAnimalsBySpecies(self, species):
        species = species.upper()
        string=""
        if self.animalShelter.get(species)==None:
            return string
        for  i in self.animalShelter.get(species):
            string += i.toString() + "\n"
        string = string[:-1]
        return string
    def doesAnimalExist(self,animal):
        
        if self.animalShelter.get(animal.species)==None:
    
            return False
        for i in self.animalShelter.get(animal.species):
            if i.species == animal.species and i.name == animal.name and\
                 i.weight == animal.weight and\
                      i.age == animal.age:
                return True
        return False
# ani = Animal("Cat",20,2,"floofy")
# ani1 = Animal("Cat",54,3,"bob")
# X= AnimalShelter()
# X.addAnimal(ani)
# X.addAnimal(ani1)
# print(X.doesAnimalExist(ani))
# print(X.getAnimalsBySpecies("CAT"))
# X.removeAnimal(ani1)
# X.removeAnimal(ani)
# print(X.getAnimalsBySpecies("cat"))
# X.addAnimal(ani1)
# print(X.getAnimalsBySpecies("cat"))
# X.removeSpecies("CAT")
# print(X.doesAnimalExist(ani1))
# X.addAnimal(ani1)
# print(X.doesAnimalExist(ani1))
# X.removeSpecies("CAT")
# print(X.doesAnimalExist(ani1))
