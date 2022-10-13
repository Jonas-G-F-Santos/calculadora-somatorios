def SOMA(n):
  soma = 0
  k = 1
  while k <= n:
    soma = soma + k * (-1) ** (k + 1)
    k = k + 1
  return soma

def FIBO(n):
    soma = 0
    k = 1
    n1 = 0
    n2 = 1
    while k <= n:
        n3 = n1 + n2
        n1 = n2        
        n2 = n3
        k = k + 1
        soma = soma + n1
    return soma
  
def PRIMOS(n):
    soma = 0
    num = 1
    k = 1
    while k <= n:
        num += 1
        i = 0
        count = 0
        if num == 2 or num % 2 != 0:
            while i < num and count <= 3:
                if num % (num - i) == 0:
                    count += 1
                i += 1
            if count == 2:
                soma += num
                k += 1
    return soma          

def FATORIAL(n):
    soma = 1
    while n > 1:
        soma = soma * n
        n = n - 1
    return soma

#============== Script Principal
while True:
    print('=============== Escolha a opção desejada ==========')
    print('< 1 > SI   = 1 - 2 + 3 - 4 + ...')
    print('< 2 > SII  = 1 + 1 + 2 + 3 + 5 + 8 + 13 + ...')
    print('< 3 > SIII = 2 + 3 + 5 + 7 + 11 + 13 + ... ')
    print('< 4 > SIV  = 1! + 3! + 5! + 7! + 9! + ...')
    print('< 0 > Sair do programa')
    print('===================================================')
    sucesso = False 
    while not sucesso: 
        try: 
            op = int(input('Digite o número da opção desejada: '))
            while op < 0 or op > 4:
                print('Opção válida entre 0 e 4 inclusive !!')
                op = int(input('Digite o número da opção desejada: '))
            sucesso = True 
        except ValueError: 
            print('Entrada inválida')
    if op == 0:
        print('Encerrando o programa com sucesso....')
        break
    else:
        sucesso = False 
        while not sucesso: 
            try: 
                n = int(input('Quantos termos para o somatório? '))      
                while n <= 0:
                    print('Quantidade TEM que ser POSITIVA!!')
                    n = int(input('Quantos termos para o somatório? '))
                sucesso = True 
            except ValueError: 
                print('Entrada inválida')
        if op == 1:
            s = SOMA(n)
            print('Somatório I vale ',s)
        elif op == 2:
            s = FIBO(n)
            print('Somatório II vale ',s)
        elif op == 3:
            s = PRIMOS(n)
            print('Somatório III vale ',s)
        else:
            s = FATORIAL(n)
            print('Somatório IV vale ',s)
        input('Tecle <ENTER> para continuar...')