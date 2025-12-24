# Desafio 1
nome = input('Por favor digite seu nome: ')
salario = float(input('Agora digite seu salário: '))
bonus_percentual = float(input('Já está acabando, só falta o bonus em porcentual (por exemplo 15% digitar 1.15): '))

calculo_kpi = float(1000 + salario * bonus_percentual)

print(f'Olá {nome}, o seu valor bônus foi de {calculo_kpi}.')