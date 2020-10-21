#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/python3
"""
Este Componente abre um arquivo em formato .csv, intitulado 
pckgCount. Este arquivo possui a série temporal referente à 
contagem dos pacotes trafegados por cada IP em cada intervalo 
de tempo. Ainda é responsável por agrupar os IPs com 
características semelhantes (quantidade de pacotes trafegados), 
com o objetivo de reduzir o conjunto de IPs a serem analisados 
e salva os dados em um novo arquivo com o mesmo nome do 
argumento de entrada.

Este componente é chamado diretamente no terminal ou por meio do 
Shell Script passando como parâmetro o nome do arquivo .csv 
contendo a quantidade de pacotes, segue o seguinte exemplo:

.. code-block:: shell
    
    python3 clustering.py pckgCount.csv
"""
"""
Este componente é responsável por criptografar ou descriptografar 
textos inseridos diretamente pelo terminal e retornar o texto no
mesmo. Além disso é possível realizar a criptografia ou
descriptografia de um arquivo, a saída é armazenada em um arquivo
txt com o nome de criptografia ou descriptografia.

Autores: Allainn Christiam J. Tavares
         Marcos Alexandre dos Anjos       
Data Criação: 25/02/2020
Versão: 0.1.2

Este componente é chamado diretamente no terminal ou por meio do 
Shell Script passando como parâmetro a opção de criptografar ou
descriptografar e a opção se o método escolhido será aplicado em 
um arquivo ou texto, acompanhado pelo nome do arquivo ou o texto.

Exemplos:

.. code-block:: shell
    
    $ python3 cripto.py -c -t peso

.. code-block:: shell
    
    $ python3 cripto.py -d -t hpuU

.. code-block:: shell
    
    $ python3 cripto.py -c -t peso

.. code-block:: shell
    
    $ python3 cripto.py -c -t peso
"""
import sys
import math
import argparse

VERSAO='0.1.2'

"""

"""
def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==1: 
        return 0
    # Second Fibonacci number is 1 
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2)

def print_error():
    print("Os argumentos fornecidos não são suficientes!")
    print("\nUso: python3 cripto.py OPÇÃO(-c | -d) [-a ARQUIVO | -t TEXTO]")
    print("\nExemplo:")
    print("python3 cripto.py -c -t Teste")
    print("python3 cripto.py -d -a criptografado.txt")


def Criptografar(text):
    """
    Método responsável em realizar a criptografia

    :param text: Texto a ser criptografado
    """
    tam=len(text)
    text = text[::-1]
    x=math.sqrt(tam)
    if x>int(x):
        num=int(x)+1
    else:
        num=int(x)

    x=num**2
    if x > tam:
        x-=tam
        comp=x*' '
        text+=comp
        
    mat = []
    cont = 0
    fib = 3
    for i in range(num):
        aux=[]
        for j in range(num):
            aux.append(chr((ord(text[cont])+Fibonacci(fib)) % 254))
            cont+=1
            fib+=1
            if fib > 15:
                fib = 3
        mat.append(aux)
        
    newText=''
    for j in range(num):
        if j%2==0:
            for i in range(num-1, -1, -1):
                newText+=mat[i][j]
        else:
            for i in range(num):
                newText+=mat[i][j]

    print("Criptografado com sucesso")
    return newText


def Descriptografar(text):
    """
    Método responsável em realizar a descriptografoa

    :param text: Texto a ser descriptografado
    """
    tam=len(text)
    x=math.sqrt(tam)
    if x>int(x):
        num=int(x)+1
    else:
        num=int(x)

    x=num**2
    if x > tam:
        x-=tam
        comp=x*' '
        text+=comp
    
    cont=0
    mat = [ [0 for i in range(num)] for j in range(num)]
    for j in range(num):
        if j%2==0:
            for i in range(num-1, -1, -1):
                mat[i][j]=text[cont]
                cont+=1
        else:
            for i in range(num):
                mat[i][j]=text[cont]
                cont+=1
                
    oldText=''
    fib = 3
    for i in range(num):
        for j in range(num):
            oldText+=chr((ord(mat[i][j])-Fibonacci(fib)) % 254)
            fib+=1
            if fib > 15:
                fib = 3
            
    oldText=oldText.rstrip(' ')[::-1]
    print("Descriptografado com sucesso")
    return oldText

def main():
    parser = argparse.ArgumentParser(description="Criptografa ou Descriptografa um ARQUIVO ou TEXTO.", 
                                    add_help=False)

    optional = parser.add_argument_group('Argumentos')
    optional.add_argument('-c', '--cripto', action='store_true',
                        help="Criptografar")
    optional.add_argument('-d', '--decripto', action='store_true',
                        help="Descriptografar")

    optional.add_argument('-t', '--texto', 
                        help="Entrada de texto")
    optional.add_argument('-a', '--abrir', metavar='ARQUIVO',
                        help="Entrada de arquivo")
    optional.add_argument('-s', '--salvar', metavar='ARQUIVO', 
                        help="Salvar no arquivo")

    optional.add_argument("-v", "--version", action="version",
                        help="Exibe a versão. ", 
                        version='Cripto - '+VERSAO)
    optional.add_argument('-h', '--help', action='help', 
                        default=argparse.SUPPRESS,
                        help='Mostra esta mensagem.')

    args = parser.parse_args()

    def verificar(func):
        if args.texto and not(args.abrir):
            print(args.texto)
            return func(args.texto)
        elif not(args.texto) and args.abrir:
            try:
                arq = open(args.abrir, 'r')
            except FileNotFoundError:
                print('Arquivo ou diretório não encontrado!!')
                quit()
            text=arq.read()
            arq.close()
            return func(text)
        else:
            print("Error!")
            print("Não foi passado o argumento de texto ou "
                +"arquivo, ou foi passado ambos os argumentos!")
            quit()

    if args.cripto and not(args.decripto):
        text = verificar(Criptografar)
    elif args.decripto and not(args.cripto):
        text = verificar(Descriptografar)
    else:
        print("Error!")
        print("Não foi passado o argumento de criptografia ou "
            +"descriptografia, ou foi passado ambos os argumentos!")
        quit()

    if args.salvar:
        arq = open(args.salvar, 'w')
        arq.write(text)
        arq.close()
        print("Salvo no arquivo " + args.salvar) 
    else:
        print(text)

if __name__ == "__main__":
    main()