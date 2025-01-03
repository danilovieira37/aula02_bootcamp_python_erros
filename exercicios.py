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
# palavra_ou_frase = input("Por favor digite uma palavra ou frase para verificação: ")
# if isinstance(palavra_ou_frase, str) and not palavra_ou_frase.isdigit():
#     formatado = palavra_ou_frase.replace(" ", "").lower()
#     if formatado == formatado[::-1]:
#         print('É um palíndromo.')
#     else: 
#         print('Não é um palíndromo.')
# else:
#     print('A variável não é uma string')

# 23: Calculadora Simples
# try:
#     primeiro_numero = float(input('Por favor digite o primeiro número: '))
#     operador = input('Por favor digite um operador: ')
#     segundo_numero = float(input('Por favor digite o segundo número: '))
#     if isinstance(primeiro_numero, float) and isinstance(segundo_numero, float):
#         if operador == '+':
#             print(primeiro_numero + segundo_numero)
#         elif operador == '-':
#             print(primeiro_numero - segundo_numero)
#         elif operador == '*':
#             print(primeiro_numero * segundo_numero)
#         elif operador == '/':
#             print(primeiro_numero / segundo_numero)
#         else:
#             print('Por favor digite um operador matemático válido.')
#     else:
#         print('O valor digitado não é um número.')
# except ZeroDivisionError:
#     print('Divisão por zero não é permitido')
# except ValueError:
#     print('O valor digitado não é um número')

# 24: Classificador de Números
# try:
#     numero_digitado = int(input('Por favor digite um número para clasificação: '))
#     if isinstance(numero_digitado, int):
#         if numero_digitado > 0 and numero_digitado % 2 == 0:
#             print('O número é positivo e é Par')
#         elif numero_digitado < 0 and numero_digitado % 2 == 0:
#             print('O número é Negativo e é Par')
#         elif numero_digitado == 0:
#             print('O número é Zero e Neutro')
#         elif numero_digitado > 0:
#             print('O número é positivo e é Impar')
#         elif numero_digitado < 0:
#             print('O número é Negativo e é Impar')
#     else:
#         print('O valor digitado não é um número.')
# except ValueError:
#     print('O valor digitado não é um número')

# 25: Conversão de Tipo com Validação

numeros = input('Por favor digite a lista de números separando eles por ",": ')
numeros_str = numeros.split(",")
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print('Lista de inteiros:', numeros_int)
except ValueError:
    print('Erro: certifique-se de que todos os elementos são números inteiros válidos.')
