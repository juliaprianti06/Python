n = float(input('digite uma nota(0,10): '))
while n < 0 or n > 10:
    print('nota inválida')
    n = float(input('digite uma nota(0,10): '))
print('nota válida')


u = str(input('digite seu usuário: '))
s = str(input('digite sua senha: '))
while u == s:
    print('usuário não pode ser igual a senha')
    u = str(input('digite seu usuário: '))
    s = str(input('digite sua senha: '))
print('login válido')


a = 80000
b = 200000
s = 0
while a <= b:
    a = a + a * 0.03
    b = b + b * 0.015
    s = s + 1
print(s)

n = int(input('digite um número: '))
f1 = 1
f2 = 1
f3 = 2
while f3 <= n - 1:
    f1, f2 = f2, f1 + f2
    f3 = f3 + 1
print(f2)



n1 = int(input('digite o primeiro número: '))
n2 = int(input('digite o segundo número: '))
while n1 % n2 != 0:
    n1, n2 = n2, n1%n2
print(f'o mdc é {n2}')

