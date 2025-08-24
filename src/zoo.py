"""
Proyecto: Clase Zoo
Este archivo define una clase Zoo que puede almacenar diferentes animales.
"""
import logging

# Configuración básica del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Zoo:
    """
    La clase Zoo representa un zoológico que guarda varios animales.
    """
    def __init__(self):
        # Lista para almacenar los animales
        self.animals = []

    def add_animal(self, animal):
        """
        Método para agregar un animal al zoológico.
        """
        self.animals.append(animal)
        logging.info(f"Se agregó {animal} al zoológico.")

    def show_animals(self):
        """
        Método para mostrar todos los animales en el zoológico.
        """
        if not self.animals:
            logging.warning("El zoológico está vacío.")
        else:
            logging.info("Animales en el zoológico:")
            for animal in self.animals:
                print(f"- {animal}")


# Ejemplo de uso
if __name__ == "__main__":
    zoo = Zoo()

    # Agregar animales (pueden ser instancias o solo nombres)
    zoo.add_animal("Dog: Rex")
    zoo.add_animal("Cat: Luna")
    zoo.add_animal("Bird: Piolín")

    # Mostrar todos los animales
    zoo.show_animals()
