from abc import ABC, abstractmethod

# Classe base para os veículos, chamada Automovel
class Automovel(ABC):
    def __init__(self, modelo, cor):
        self.modelo = modelo  # Modelo do veículo
        self.cor = cor  # Cor do veículo
        self.ligado = False  # Inicialmente, o veículo está desligado
    
    @abstractmethod
    def ligar(self):
        """Método para ligar o veículo"""
        pass
    
    @abstractmethod
    def desligar(self):
        """Método para desligar o veículo"""
        pass
    
    def acelerar(self):
        """Método padrão para acelerar, mas pode ser sobrescrito nas subclasses"""
        if self.ligado:
            print(f"{self.modelo} está acelerando.")
        else:
            print(f"Não é possível acelerar o {self.modelo}, pois ele está desligado.")

# Classe Moto (herda de Automovel)
class Moto(Automovel):
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"A moto {self.modelo} está ligada.")
        else:
            print(f"A moto {self.modelo} já está ligada.")
    
    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f"A moto {self.modelo} foi desligada.")
        else:
            print(f"A moto {self.modelo} já está desligada.")
    
    def acelerar(self):
        if self.ligado:
            print(f"A moto {self.modelo} acelera rapidinho!")
        else:
            print(f"Não dá para acelerar a moto {self.modelo}, ela está desligada.")

# Classe Carro (herda de Automovel)
class Carro(Automovel):
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"O carro {self.modelo} foi ligado.")
        else:
            print(f"O carro {self.modelo} já está ligado.")
    
    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f"O carro {self.modelo} foi desligado.")
        else:
            print(f"O carro {self.modelo} já está desligado.")
    
    # Não precisamos sobrescrever o método acelerar, o comportamento padrão já é bom

# Classe Caminhão (herda de Automovel)
class Caminhao(Automovel):
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"O caminhão {self.modelo} foi ligado.")
        else:
            print(f"O caminhão {self.modelo} já está ligado.")
    
    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f"O caminhão {self.modelo} foi desligado.")
        else:
            print(f"O caminhão {self.modelo} já está desligado.")
    
    def acelerar(self):
        if self.ligado:
            print(f"O caminhão {self.modelo} acelera devagar e com força.")
        else:
            print(f"Não dá para acelerar o caminhão {self.modelo}, ele está desligado.")

# Classe Ônibus (herda de Automovel)
class Onibus(Automovel):
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"O ônibus {self.modelo} foi ligado.")
        else:
            print(f"O ônibus {self.modelo} já está ligado.")
    
    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f"O ônibus {self.modelo} foi desligado.")
        else:
            print(f"O ônibus {self.modelo} já está desligado.")
    
    def acelerar(self):
        if self.ligado:
            print(f"O ônibus {self.modelo} acelera, mas devagar.")
        else:
            print(f"Não é possível acelerar o ônibus {self.modelo}, ele está desligado.")

# Função que pode operar qualquer veículo, ligando, acelerando e desligando
def operar_veiculo(veiculo):
    veiculo.ligar()
    veiculo.acelerar()
    veiculo.desligar()

# Criando alguns veículos para testar
moto = Moto("Honda CBR", "vermelha")
carro = Carro("Fusca", "azul")
caminhao = Caminhao("Scania", "branco")
onibus = Onibus("Volvo", "amarelo")

# Testando a função com diferentes veículos
print("\nOperando a moto:")
operar_veiculo(moto)

print("\nOperando o carro:")
operar_veiculo(carro)

print("\nOperando o caminhão:")
operar_veiculo(caminhao)

print("\nOperando o ônibus:")
operar_veiculo(onibus)

