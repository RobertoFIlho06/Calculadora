while True:
    print("---- Calculadora ----")
    print("Digite A: Soma ")
    print("Digite B: Subtração ")
    print("Digite C: Divisão ")
    print("Digite D: Multiplicação ")

    opção = input("Digite o operador:")
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    if opção.upper() == "A":
        resultado = n1 + n2
    elif opção.upper() == "B":
        resultado = n1 - n2
    elif opção.upper() == "C":
        resultado = n1 / n2
    elif opção.upper() == "D":
        resultado = n1 * n2
    print(f"Resultado: {resultado}")
    resposta = input("Deseja fazer outro cálculo?" )
    if resposta.capitalize() == "Sim":
        print(" ")
    else:
        break










