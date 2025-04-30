from random import sample
n = sample(range(100),10)
maior = 0
menor = n[0]
for x in n:
    if x > maior:
        maior = x
    if x < menor:
        menor = x 
print(f'os números sorteados:{n}')
print(f'o maior é {maior}')
print(f'o menor é {menor}')

from random import sample
n =  sample(range(100), 20)
par = []
ímpar = []
for x in n:
    if x % 2 == 0:
        par.append(x)
    if x % 2 == 1:
        ímpar.append(x)
print(f'os números sorteados: {n}')
print(f'os números pares: {par}')
print(f'os números ímpares: {ímpar}')


from random import sample
n1 = sample(range(100), 10)
n2 = sample(range(100), 10)
n3 = [] 
for x in zip(n1, n2):
    n3.extend(list(x))
print(f'os sorteados: {n1}')
print(f'os sorteados: {n2}')
print(f'lista intercalada: {n3}')


texto = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you'''.lower()
import string 
for x in string.punctuation:
    texto = texto.replace(x, '')
t = []
for p in texto.split():
    if p[0] in 'python' or p[-1] in 'python':
        t.append(p)
print(t)


texto = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you'''.lower()
import string 
for x in string.punctuation:
    texto = texto.replace(x, '')
def pitônica(palavra):
    for letra in palavra:
        if letra in 'python':
           return True
    return False
t = []
for p in texto.split():
    if pitônica(p) and len(p) > 4:
        t.append(p)
print(t)
    