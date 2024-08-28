import time

delayzinho = 1

def sauda():
    print("Seja Bem vindo !")
    time.sleep(delayzinho)
    name = input("Informe seu nome por favor: ")
    print("Bem vindo,", name + "!")


def menu():
    print("Qual sua banda favorita entre as alternativas abaixo ?")
    time.sleep(delayzinho)
    print("1-Guns N'Roses")
    time.sleep(delayzinho)
    print("2-Metallica")
    time.sleep(delayzinho)
    print("3-Rammstein")

    opcao = int(input("Digite o número da opção desejada:"))

    if opcao == 1: 
        print("Guns N'Roses (Bom e velho Guns N' Roses)")

    elif opcao == 2:
        print("Metallica (Uma das bandas mais famosas de trash metal do mundo.)")

    elif opcao == 3:
        print("Rammstein (Uma banda alemã de metal industrial, seus lançamentos mais famosos são Sonne, Du hast e Deutschland.")

    else:
        print("Opção incorreta!")


sauda()
menu()


        
