a = int(input('digite o lado a: '))
b = int(input('digite o lado b: '))
c = int(input('digite o lado c: '))
if a > b + c or b > a + c or c > a + b:
    print('isso não é um triângulo')
elif a == b == c:
    print('é um triângulo equilátero')
elif a == b or b == c or c == a:
    print('é um triângulo isóceles')
else:
    print('é um triângulo escaleno')


a = int(input('digite o ano: '))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('o ano é bissexto')
else:
    print('o ano não é bissexto')



pp = int(input('digite o peso: '))
if pp > 50:
    excesso = pp - 50
    multa = excesso * 4
    print(f'você excedeu o peso, sua multa será de {multa:.2f} reais')
else:
    multa = excesso = 0
    print('o peso está certo')


n1 = int(input('digite o primeiro número: '))
n2 = int(input('digite o segundo número: '))
n3 = int(input('digite o terceiro número: '))
if n1 > n2 and n1 > n3:
    print('o primeiro número é o maior')
if n2 > n1 and n2 > n3:
    print('o segundo número é o maior')
if n3 > n1 and n3 > n2:
    print('o terceiro número é o maior')



n1 = int(input('digite o primeiro número: '))
n2 = int(input('digite o segundo número: '))
n3 = int(input('digite o terceiro número: '))
if n1 > n2 and n1 > n3:
    print('o número {} é o maior'.format(n1))
if n2 > n1 and n2 > n3:
    print('o número {} é o maior'.format(n2))
if n3 > n1 and n3 > n2:
    print('o número {} é o maior'.format(n3))
if n1 < n2 and n1 < n3:
    print('o número {} é o menor'.format(n1))
if n2 < n1 and n2 < n3:
    print('o número {} é o menor'.format(n2))
if n3 < n1 and n3 < n2:
    print('o número {} é o menor'.format(n3))



h = int(input('quanto você ganha por hora?: '))
n = int(input('quantas horas você trabalha no mês? '))
sb = h * n
ir = sb * 0.11
i = sb * 0.08
s = sb * 0.05
desconto = sb - ir - i - s
sl = desconto
print(f'o seu salário bruto é R$ {sb:.2f}')
print(f'o valor do Imposto de Renda é R$ {ir:.2f}')
print(f'o valor do INSS é R$ {i:.2f}')
print(f'o valor do Sindicato é R$ {s:.2f}')
print(f'o seu salário líquido é R$ {sl:.2f}')


a = int(input('digite a área a ser pintada: '))
if a % 54 == 0:
   latas = a / 54
else:
    latas = int(a / 54) + 1
    p = latas * 80
print(f'o número de latas a ser comprado é {latas:} e o preço será de R$ {p:.2f}') 
