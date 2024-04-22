# Construa um código que calcule a média  dos  valores  em  uma  lista.  Utilize um  bloco try -except para  lidar  com  a divisão por zero, caso a lista esteja vazia.
nums = [10, 4, 5, 3, 6, 7, 8, 2, 9, 1]
media = 0
try:
    for index in nums:
        media += index
    media = media / len(nums)
    print(f"A média dos valores é: {media}")
except:
    print("Erro")
