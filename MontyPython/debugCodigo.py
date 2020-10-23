#!/usr/bin/env python
# -*- coding: utf-8 -*-

# inicializa la lista vacía para contener la entrada del usuario
# y el valor de suma en cero
user_list = []
list_sum = 0

# busca la entrada del usuario para 10 números
for i in range(10):

    correcto = False
    number = -1

    while not correcto:
        userInput = input("Enter any 2-digit number[{:2}]: ".format(i+1))

        try:
            number = int(userInput)
            if number >= 10 and number <= 99:
                correcto = True
            else:
                print("El numero tiene que ser de 2 digitos.")
        except ValueError:
            print("Valor incorrecto. Eso no es un int!")

# verifica si el número es par y, en caso de ser afirmativo lo agrega a la lista list_sum
# imprime la advertencia de valor incorrecto cuando se produce la excepción ValueErrort

    user_list.append(number)
    if number % 2 == 0:
        list_sum += number

print("\nuser_list: {}".format(user_list))
print("La suma de los números pares en user_list es: {}.".format(list_sum))
