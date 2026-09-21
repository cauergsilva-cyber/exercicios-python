numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 > numero2:
    print(f"{numero1} é o maior")
elif numero2 > numero1:
    print(f"{numero2} é o maior")
else:
    print("Os números são iguais")
