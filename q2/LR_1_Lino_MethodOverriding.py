class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return self.name

    def make_sound(self):
        return self.name

class Lion(Animal):
    def make_sound(self):
        super().make_sound()
        return "roars"

    def eat(self):
        super().eat()
        return "fresh meat"

class Elephant(Animal):
    def make_sound(self):
        super().make_sound()
        return "trumphets"

    def eat(self):
        super().eat()
        return "grass and fruit"

class Monkey(Animal):
    def make_sound(self):
        super().make_sound()
        return "chatters"

    def eat(self):
        super().eat()
        return "banana"

lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

print("Animal Sounds and Eating Habits")
print("-------------------------------")
print(f"{lion.name} {lion.make_sound()} loudly and eats {lion.eat()}!")
print(f"{elephant.name} {elephant.make_sound()} and eats {elephant.eat()}!")
print(f"{monkey.name} {monkey.make_sound()} and eats {monkey.eat()}!")      