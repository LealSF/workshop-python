class Dog:
    tricks = []
    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
        self.tricks = []
    
    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)

