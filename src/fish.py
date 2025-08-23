class fish:
    def __init__(self, name: str, age: int, species: str):
        self.name = name
        self.age = age
        self.species = species
    def swim (self):
        print (f"el pez {self.name} nada en el mar")

if __name__ =="__main__":
    globo = fish("lina", 14,"Globo")
    globo.swim()