import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# primeiro_numero = int(input('Por favor digite o primeiro número: '))
# segundo_numero = int(input('Por favor digite o segundo número: '))
# divisao = primeiro_numero // segundo_numero
# print(divisao)
    

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
##raio_do_curculo = float(input("Por favor digite o raio: "))
##area_do_circulo = math.pi * raio_do_curculo ** 2
##print(f'{area_do_circulo:.2f}')



# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# data_digitada = input('Por favor digite uma data no formato "dd/mm/aaa": ')
# lista_de_dia_mes_ano = data_digitada.split('/')
# print(f"O elemento 1 é o: {lista_de_dia_mes_ano[0]}")
# print(f"O elemento 2 é o: {lista_de_dia_mes_ano[1]}")
# print(f"O elemento 2 é o: {lista_de_dia_mes_ano[2]}")


# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# try:
#     celsius = float(input('Por favor digite o Celsius para ser convertido: '))
#     conversao = (celsius * 9/5) + 32
#     print(f'O Valor Celsius digitado, convertido para Fahrenheit é de {conversao}F.')
# except ValueError:
#     print('Por favor digite um valor em Celsius válido')


# 22: Verificador de Palíndromo
palavra_ou_frase = input("Por favor digite uma palavra ou frase para verificação: ")
if isinstance(palavra_ou_frase, str) and not palavra_ou_frase.isdigit():
    formatado = palavra_ou_frase.replace(" ", "").lower()
    if formatado == formatado[::-1]:
        print('É um palíndromo.')
    else: 
        print('Não é um palíndromo.')
else:
    print('A variável não é uma string')
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
