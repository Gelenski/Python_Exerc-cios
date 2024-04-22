# Utilize um loop for para calcular a soma  dos números ímpares de 1 a 10.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def calcula():
    impares = 0
    for index in nums:
        if (index % 2 != 0):
            impares += index
    print(impares)


calcula()
