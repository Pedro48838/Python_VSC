from functions.user_interface import user_interface

class AparelhoEletrico:
    def __init__(self, nome, potencia):
        self.nome = nome
        self.potencia = potencia


class Comodo:
    def __init__(self, nome):
        self.nome = nome
        self.aparelhos = []

    def adicionar_aparelho(self, aparelho):
        self.aparelhos.append(aparelho)

    def calcular_carga_total(self):
        carga_total = sum(aparelho.potencia 
            for aparelho in self.aparelhos)
        return carga_total


class Casa:
    def __init__(self):
        self.comodos = []

    def adicionar_comodo(self, comodo):
        self.comodos.append(comodo)

    def calcular_carga_total_casa(self):
        carga_total_casa = sum(comodo.calcular_carga_total() for comodo in self.comodos)
        return carga_total_casa

    def verificar_sobrecarga(self, capacidade_disjuntor):
        carga_total_casa = self.calcular_carga_total_casa()
        if carga_total_casa > capacidade_disjuntor:
            print("Sobrecarga detectada! A carga total da casa excede a capacidade do disjuntor principal.")
        else:
            print("A carga total da casa está dentro dos limites seguros.")


# Criando os cômodos
sala = Comodo("Sala")
quarto1 = Comodo("Quarto 1")
quarto2 = Comodo("Quarto 2")
cozinha = Comodo("Cozinha")
banheiro = Comodo("Banheiro")
...
# Adicionando aparelhos aos cômodos
sala.adicionar_aparelho(AparelhoEletrico("Televisão", 200))
sala.adicionar_aparelho(AparelhoEletrico("Lâmpada", 60))
quarto1.adicionar_aparelho(AparelhoEletrico("Ar-condicionado", 1500))
cozinha.adicionar_aparelho(AparelhoEletrico("Geladeira", 800))
...
# Criando a casa e adicionando os cômodos
casa = Casa()
casa.adicionar_comodo(sala)
casa.adicionar_comodo(quarto1)
casa.adicionar_comodo(quarto2)
casa.adicionar_comodo(cozinha)
casa.adicionar_comodo(banheiro)
...

# Calculando a carga total da casa e verificando a sobrecarga
capacidade_disjuntor = 5000  # Defina a capacidade do disjuntor principal em Watts
carga_total_casa = casa.calcular_carga_total_casa()
print(f"A carga total da casa é de {carga_total_casa} Watts.")
casa.verificar_sobrecarga(capacidade_disjuntor)

