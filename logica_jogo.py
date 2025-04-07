import random

n1 = random.randint(0,9)
n2 = random.randint(0,9)

op = ["+", "-", "*", "/"]

esc_op = random.choice(op)
if esc_op == "+":
    print(f"{n1} ? {n2} = {n1 + n2}")
elif esc_op == "-":
    print(f"{n1} ? {n2} = {n1 - n2}")
elif esc_op == "*":
    print(f"{n1} ? {n2} = {n1 * n2}")
elif esc_op == "/":
    print(f"{n1} ? {n2} = {n1 / n2}")
else:
    print("Invalid operator")
    
tentativa = input("Qual operador foi utilizado?\n+\n*\n-\n/")
if tentativa == esc_op:
    print("Correto")
else:
    print("Errado")
