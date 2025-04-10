import random
class DadosFuncionais:
    
    @staticmethod
    def gerarNumeros():
            num1 = random.randint(0, 9)
            num2 = random.randint(0, 9)
            return num1, num2

    @staticmethod
    def selecionarOperador():
        return random.choice(["+", "-", "/", "*"])

    @staticmethod
    def calcularResultado(a, b, op):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return round(a / (b if b != 0 else 1), 2)
        else:
            raise ValueError("Operador inválido")