import random 

pin = []
tamanho_pin = 0
contador_caracteres = 0

while tamanho_pin <= 0:
    tamanho_pin = int(input('Digite a quantidade de caracteres para um pin: '))
    if tamanho_pin <= 0:
        print('O número deve ser maior que 0')
        

while contador_caracteres < tamanho_pin: 
    numero_aleatorio = random.randint(0, 9)
    pin.append(numero_aleatorio)
    contador_caracteres += 1

print(f'A série de PIN gerada foi: {pin}')
