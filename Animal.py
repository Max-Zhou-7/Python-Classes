class Animal:
    def __init__(self, species=None, weight=None, 
    age=None, name=None):
        self.species = species.upper()
        self.weight = weight
        self.age = age
        self.name = name.upper()
    def setSpecies(self,species):
        self.species = species.upper()
    def setWeight(self,weight):
        self.weight = weight
    def setAge(self,age):
        self.age = age
    def setName(self,name):
        self.name = name.upper()


    def toString(self):
        return   "Species: " + self.species + ", Name: " + self.name+ \
        ", Age: " + str(self.age)+ ", Weight: " + str(self.weight)

   
# a = Animal("dog", 12.2, 2, "Ruffles")
# print(a.toString())


