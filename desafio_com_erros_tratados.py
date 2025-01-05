CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome
nome_usuario = input('Por favor digite seu nome: ')
if nome_usuario.isdigit():
    print('Você digitou um número. Por favor digite um nome de usuário válido.')
    exit()
elif len(nome_usuario) == 0:
    print('Você não digitou nenhum valor. Por favor digite um nome de usuário válido.')
    exit()
elif nome_usuario.isspace():
    print('Você digitou somente espaço. Por favor digite um nome de usuário válido.')
    exit()

# 2) Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
try:
    salario = float(input('Por favor digite seu salário: '))
except ValueError:
    print('Você não digitou nenhum valor, texto ou letra. Por favor digite um o valor do salário válido.')
exit()
# 3) Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
porcentagem_bonus = float(input('Por favor digite o Porcentual do bônus: '))

# 4) O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
bonus = float(CONSTANTE_BONUS + salario * porcentagem_bonus)

#5) Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".
print('Olá ' + nome_usuario + ', o seu bônus foi de R$ ' + str(bonus))