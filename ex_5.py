def inverter_string(string):
    return string[::-1]

texto = input("Digite uma string: ")
texto_invertido = inverter_string(texto)
print(f"String invertida: {texto_invertido}")
