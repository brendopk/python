iphones = ["(0)iPhone11", "(1)iPhone11 Pro", "(2)iPhone11 Pro Max"]
print(iphones[0])
print(iphones[1])
print(iphones[2])

nome = input("Qual o seu nome? ")

usuario = int(input("Escolha um iphone: "))

if usuario == 0:
    print(f"Olá {nome} você escolheu {iphones[0]}!")
elif usuario == 1:
    print(f"Olá {nome} você escolheu {iphones[1]}!")
elif usuario == 2:
    print(f"Olá {nome} você escolheu {iphones[2]}!")
else:
    print(f"{nome} não temos esse modelo!")
