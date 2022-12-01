def media(i):
    x = 0
    for num in i:
      x = x + num 
    y = x / len(i)    
    return y

quanti = int(input("Quantos números terá a lista?"))
cont = 0
todos =[]
while cont < quanti:
    numero = int(input("Qual o número?"))
    todos.append(numero)
    cont = cont + 1

print(todos)

final = media(todos)
print(final)
