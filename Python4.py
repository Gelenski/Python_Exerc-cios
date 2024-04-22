# Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
nums = [10, 4, 5, 3, 6, 7, 8, 2, 9, 1]


def lista_nums():
    maior_numero = max(nums)
    for index in range(maior_numero, 0, -1):
        if index in nums:
            print(index)


lista_nums()
