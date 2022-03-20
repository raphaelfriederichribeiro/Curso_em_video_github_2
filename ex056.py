rep = 0
imaior = 0
nvelho = ''
mu20 = 0
for q in range(1, 5):
    print(f'{q}ª PESSOA!!')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    rep += idade
    sexo = str(input('[M] Masculino [F] Feminino: ')).strip().upper()
    med = rep/q
    if q == 1 and sexo in 'M':
        imaior = idade
        nvelho = nome
    if sexo in 'M' and idade > imaior:
        imaior = idade
        nvelho = nome
    if idade < 20 and sexo in 'F':
        mu20 += 1
print(f'\033[1;32mA soma das idades das 4 pessoas: {rep} e a média: {med}\033[m')
print(f'\033[1;31mO mais homem mais velho é {nvelho} com {imaior} anos.\033[m')
print(f'\033[1;30mAo todo são {mu20} mulheres abaixo de 20 anos.\033[m')
