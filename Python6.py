# Crie  uma  lista  de  números  e  utilize  um loop for para  calcular  a  soma  de  todos os elementos. Utilize um bloco try - except para lidar com possíveis exceções.
nums = [10, 4, 5, 3, 6, 7, 8, 2, 9, 1]
soma = 0
try:
    for index in nums:
        soma += index

    print(f"A soma de todos os números é: {soma}")
except:
    print("Erro")
