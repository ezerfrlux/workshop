# password validator
# No secuencia de numeros
# No secuencia de letras
# Al menos una mayuscula
# Al menos un numero
# Minimo 8 caracteres
print("Ingrese su password:")
password = input()
minLenPassword = 8

haveNumber = any(character.isdigit() for character in password)
haveUpper = any(character.isupper() for character in password)
sequences = [f"{i}{i+1}{i+2}" for i in range(8)]
haveSequences = any(seq in password for seq in sequences)

if len(password) >= minLenPassword and haveNumber and haveUpper and not haveSequences:
    for i, caracter in enumerate(password):
        if i == 0 and i == 1:
            pass
        else:
            if password[i-2] == password[i-1] == password[i]:
                print("Password Invalida, caracteres repetidos: %s" % caracter)
                break
    else:
        print("Password Valida")
else:
    if len(password) < minLenPassword:
        print("Debes usar 8 caracteres")
    else:
        if not haveUpper and not haveNumber:
            print("Debes usar almenos un numero y una mayuscula")
        else:
            print("Weakness Password")

