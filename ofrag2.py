# -*- coding: utf-8 -*-
"""
Spyder Editor

Name: Marco Lanza SERSON
"""

n = int(input("Digite um número inteiro: "))

if (n == 2):
        print("2 é primo.")
       

elif (n > 1 and n != 2):
        for i in range(2, n):
            if n % i == 0:
               print(n, "não é primo!")
               break
            else:
                print(n, "é primo!")
                break
else:
    print(n, "não é primo!")
                