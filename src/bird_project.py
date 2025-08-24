"""
Proyecto: Ejemplo de herencia en POO con aves.
Este archivo define la clase Bird y la clase Eagle que hereda de Bird.
Incluye logging y comentarios explicativos sobre herencia.
"""
import logging

# Configuración básica del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Bird:
    """
    Clase base Bird representa el concepto general de un ave.
    En POO, una clase base puede ser heredada por otras clases más específicas.
    """
    def __init__(self, name: str, age: int, species: str):
        self.name = name
        self.age = age
        self.species = species
        logging.info(f"Se ha creado un ave de especie {self.species} llamada {self.name} de {self.age} años.")

    def sing(self):
        """
        Método que representa el canto del ave.
        """
        logging.info(f"{self.name} está cantando.")
        print(f"{self.name}: ¡Pío pío!")

    def birthday(self):
        self.age += 1
        logging.info(f"{self.name} ahora tiene {self.age} años.")

    def migrate(self, destination: str):
        """
        Método que representa la migración del ave.
        """
        logging.info(f"{self.name} está migrando hacia {destination}.")
        print(f"{self.name} está migrando hacia {destination}.")


# Ejemplo de herencia: Eagle hereda de Bird
class Eagle(Bird):
    """
    Clase Eagle hereda de Bird.
    En POO, la herencia permite que una clase hija obtenga atributos y métodos de la clase padre.
    """
    def __init__(self, name: str,age: int):
        # Llama al constructor de Bird con especie fija "Águila"
        super().__init__(name, age, "Águila")
        logging.info(f"Se ha creado un águila llamada {self.name}.")

    def fly(self):
        """
        Método propio de Eagle, además de los heredados de Bird.
        """
        logging.info(f"{self.name} está volando alto.")
        print(f"{self.name}: ¡Estoy volando alto!")
    
    def altitud(self, distancia: int ):
        logging.info (f"La altitud de {self.name} es: {distancia}m")
        print(f"{self.name} vuela a {distancia}m")


class Parrot(Bird):

    def __init__(self, name: str, age: int):
        super().__init__(name, age, "Loro")
        logging.info(f"Se ha creado un loro llamado {self.name}.")

    def talk(self, frase: str ):
        logging.info(f"{self.name} dice: {frase}")
        print(f"{self.name} dice: {frase}")


if __name__ == "__main__":
    Eagle1 = Eagle("Pablo", 6)
    Eagle1.birthday()

    parrot1 = Parrot("Pepe", 2)
    parrot1.sing()
    parrot1.talk("Hola, soy Pepe el loro!!")

    Eagle1.altitud(20)

    # Probando el nuevo método migrate en ambas aves
    Eagle1.migrate("las montañas del norte")
    parrot1.migrate("la selva amazónica")
