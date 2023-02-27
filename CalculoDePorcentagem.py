salário = float(input("Qual o valor do salário? R$"))

novo = salário + (salário * 15 / 100)
# Não ultizamos o sinal de % por isso será necessário por o valor da variavel multiplicado por um numero de sua
# preferencia, dividido por 100.

print("O funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}".format(salário, novo))
