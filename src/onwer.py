import logging

# Configuración básica del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# ============================
# CLASE BIRD
# ============================
class Bird:
    def __init__(self, name: str, age: int, species: str):
        self.name = name
        self.age = age
        self.species = species
        logging.info(f"Se ha creado un ave llamada {self.name}, especie {self.species}.")

    def eat(self):
        print(f"{self.name} está comiendo semillas.")


# ============================
# CLASE FISH
# ============================
class Fish:
    def __init__(self, name: str, age: int, species: str):
        self.name = name
        self.age = age
        self.species = species
        logging.info(f"Se ha creado un pez llamado {self.name}, especie {self.species}.")

    def eat(self):
        print(f"{self.name} está comiendo algas.")


# ============================
# CLASE OWNER
# ============================
class Owner:
    def __init__(self, owner_name: str):
        self.owner_name = owner_name
        self.animals = []  # lista de animales del dueño
        logging.info(f"Se ha creado un dueño llamado {self.owner_name}.")

    def add_animal(self, animal):
        """Agrega un animal a la lista del dueño"""
        self.animals.append(animal)
        logging.info(f"{self.owner_name} ahora tiene un {animal.species} llamado {animal.name}.")
        print(f"{self.owner_name} adoptó a {animal.name}, un {animal.species}.")

    def feed_all(self):
        """Alimenta a todos los animales del dueño"""
        print(f"{self.owner_name} está alimentando a sus animales...")
        for animal in self.animals:
            animal.eat()


# ============================
# EJEMPLO DE USO
# ============================
if __name__ == "__main__":
    owner1 = Owner("Juan")

    # Crear animales
    bird1 = Bird("Piolín", 2, "Canario")
    fish1 = Fish("Nemo", 1, "Pez Payaso")

    # Agregar animales al dueño
    owner1.add_animal(bird1)
    owner1.add_animal(fish1)

    # Alimentar a todos
    owner1.feed_all()
