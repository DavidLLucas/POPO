import time

print("Seja Bem vindo")
name = input("Informe seu nome")
print("Bem vindo,", name + "!")

print("Como posso te ajudar ?")

print("1-Guns N'Roses")
print("2-Metallica")
print("3-Rammstein")

opcao = int(input("Digite o número da opção desejada:"))

if opcao == 1: 
    print("Guns N'Roses")

elif opcao == 2:
    print("Metallica")

elif opcao == 3:
    print("Rammstein")

else:
    print("Opção incorreta!")

""" tive que ajustar a indentação no bloco de condição 
Outro ponto é que faltou criar a função menu e depois chamá-la sempre que necessario.
Tents realizar os ajustes ou vemos na próxima aula

"""


        
