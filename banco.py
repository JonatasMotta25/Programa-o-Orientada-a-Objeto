class Banco:
    #Método Construtor
    def __init__(self, banco, agencia, conta, cliente, cpf):
        self.banco = banco
        self.agencia = agencia
        self.conta = conta
        self.cliente = cliente
        self.cpf = cpf
        self.saldo = 0
        self.login = None
        self.senha = None
    
    # Login e senha
    def definir_senha(self):
        self.senha = None
    # método de definição de senha 
    def definir_senha(self, new_senha):
        if self.senha == None:
            self.senha = new_senha
            print("Sua senha foi definida!")
        elif self.senha != None:
            decisao = input("Você já possui uma senha definida. Deseja mudar a senha mesmo assim?").lower()
            if decisao == "sim":
                 self.senha = new_senha
        else:
            print("Escolha errada!")

    # Método de apresentação
    def __str__(self):
        return f"""
Cliente {self.cliente} cadastrado com sucesso:
Conta: {self.conta}
Agencia: {self.agencia}
Banco: {self.banco}
        """
    # deposito
    def deposito(self, valor):
        if isinstance(valor, (int, float)):
            self.saldo += valor
            print(f"Saldo atualizado com sucesso no valor de R${float(valor)}.")
    # saque
    def saque(self, senha, valor):
        if self.senha == senha and self.saldo >= valor and isinstance(valor, (int, float)):
            self.saldo -= valor 
            print(f"Saque realizado no valor de: {float(valor)}")
        else:
            print("Valor ou senha incorreta, tente novamente")
    # transferencia
    # pix
    def pix(self, destinatario, valor):
        if isinstance(valor, (int, float)) and self.saldo >= valor:
            self.saldo -= valor
            destinatario.saldo += valor
            print(
                 f"""
Pix realizado no valor de R${valor}
De: {self.cliente}
Para: {destinatario.cliente}
                """
            )
    # caixinha
    # extrato
    def extrato(self):
        print(
        f""" 
- - - - - - - - - - - - - - -
Conta: {self.conta}
Agencia: {self.agencia}
Saldo: {self.saldo}
Cliente: {self.cliente}
- - - - - - - - - - - - - - -
"""
        )

    

    
