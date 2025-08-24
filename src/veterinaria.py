"""
Proyecto: Clase Veterinarian
Este archivo define la clase Veterinarian que puede revisar animales.
"""

class Veterinarian:
    def __init__(self, name: str):
        self.name = name

    def checkup(self, animal):
        """
        Recibe un animal y muestra un mensaje de revisión.
        Asume que el animal tiene atributos 'name' y 'species'.
        """
        print(f"El veterinario {self.name} está revisando a {animal.name}, que es un {animal.species}.")

# ============================
# EJEMPLO DE USO
# ============================
if __name__ == "__main__":
    # Definimos una clase Animal simple para probar
    class Animal:
        def __init__(self, name, species):
            self.name = name
            self.species = species

    perro = Animal("Rex", "perro")
    gato = Animal("Misu", "gato")

    vet = Veterinarian("Dr. López")
    vet.checkup(perro)
    vet.checkup(gato)
