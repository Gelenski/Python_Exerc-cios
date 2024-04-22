# Solicite  ao  usuário  um  número  e,  em  seguida, utilize um loop for para  imprimir  a  tabuada  desse  número,  indo de 1 a 10.
def tabuada():
    num = int(input("Digite um número: "))
    for index in range(1, 11):
        resultado = num * index
        print(f"{num} x {index} = {resultado}")


tabuada()
