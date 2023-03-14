class Doggy():
    
    num_of_dogs = 0
    birth_of_dogs = 0
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1
        
    def bark(self):
        print('bark!')
    
    def __del__(self):
        Doggy.num_of_dogs -= 1
    
    @classmethod
    def get_status(cls):
        print(cls.num_of_dogs, cls.birth_of_dogs)

    

d1 = Doggy('우진','불독')
d2 = Doggy('진우','치와와')
d3 = Doggy('진우우','치와와와')
Doggy.get_status()
d1.bark()


