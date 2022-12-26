x = '^'
y = ' '
n = 0

while n < 10:
    if n == 0:
        print('Árvore de Natal em Python!\n         *')

    else:
        print((y*(10 - n)) + ((n + (n - 1)) * x))

    n = n + 1

print('  Feliz Natal!!!!')

