class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print("Som genérico de animal")

class Cachorro(Animal):
    def fazer_som(self):
        print("Au au!")

class Gato(Animal):
    def fazer_som(self):
        print("Miau!")

# Polimorfismo
def fazer_animais_fazerem_som(animais):
    for animal in animais:
        animal.fazer_som()

# Criando objetos
animal_generico = Animal("Animal Genérico")
cachorro = Cachorro("Rex")
gato = Gato("Mingau")

# Demonstrando herança
print(cachorro.nome)  # Acessando o atributo 'nome' herdado da classe Animal
print(gato.nome)  # Acessando o atributo 'nome' herdado da classe Animal

# Demonstrando polimorfismo
animais = [animal_generico, cachorro, gato]
fazer_animais_fazerem_som(animais)