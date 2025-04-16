import random
class DadosFuncionais:
    
    @staticmethod
    def gerarNumeros():
        while(True):
            num1 = random.randint(0, 9)
            num2 = random.randint(0, 9)
            resultadoMais = num1 + num2
            resultadoMenos = num1 - num2
            resultadoMultiplicacao = num1 * num2
            if num2 != 0:
                resultadoDivisao = num1 / num2
            else:
                resultadoDivisao = None
            
            if (resultadoMais!=resultadoMenos and
                resultadoMais!=resultadoMultiplicacao and
                resultadoMais!=resultadoDivisao and
                resultadoMenos!=resultadoMultiplicacao and
                resultadoMenos!=resultadoDivisao and
                resultadoMultiplicacao!=resultadoDivisao):
                    
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
            resultado = a / b
            if resultado.is_integer():
                return int(resultado)
            else:
                return round(resultado, 2)