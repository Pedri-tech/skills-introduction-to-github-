class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
    
class Prey(Animal):
    def flee(self):
        print(f"This animal is fleeing")

class Predator(Animal):
    def flee(self):
        print(f"This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass


rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Rabbit("Nemo")

rabbit.flee()