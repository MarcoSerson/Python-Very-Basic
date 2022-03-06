hora = input('Digite a hora, sem os minutos: ')

if hora.isdigit():
    if int(hora) > 23:
        print("Digite apenas a hora entre 0 e 23.")
    elif 0 <= int(hora) <= 11:
        print("Bom dia!")
    elif 12 <= int(hora) <= 17:
        print("Boa Tarde!")
    else:
        print("Boa noite!")
else:
    print("Digite apenas a hora entre 0 e 23. Sem minutos e sem letras.")
