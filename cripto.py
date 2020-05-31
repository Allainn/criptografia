#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Algoritmo responsavel por criptografar ou descriptografar
textos ou arquivos e gerar um arquivo de saída.

Autor: Allainn Christiam J. Tavares
Data Criação: 25/02/2020
Versão: 0.0.3
"""
import sys
import math

VERSAO='0.0.3'

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
    print("python3 cripto -c -t Teste")
    print("python3 cripto -d -a criptografado.txt")


def Criptografar(text):
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
        
    mat = []
    cont = 0
    fib = 3
    for i in range(num):
        aux=[]
        for j in range(num):
            aux.append(chr(ord(text[cont])+Fibonacci(fib)))
            cont+=1
            fib+=1
            if fib > 8:
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
            oldText+=chr(ord(mat[i][j])-Fibonacci(fib))
            fib+=1
            if fib > 8:
                fib = 3
            
    oldText=oldText.rstrip(' ')
    print("Descriptografado com sucesso")
    return oldText

txt_help='''Uso: python3 cripto.py OPÇÃO(-c | -d) [-a ARQUIVO | -t TEXTO]
Criptografa ou Descriptografa um ARQUIVO ou TEXTO.

  -c, --cripto		criptografar
  -d, --decripto	descriptografar

  -t, --texto		entrada de texto
  -a, --arquivo		entrada de arquivo

  -h, --help		mostra esta ajuda e sai
  -v, --version		informa a versão e sai

Exemplo:
    python3 cripto -c -t Teste
    python3 cripto -d -a criptografado.txt

Autor: Allainn Christiam'''


try:
    param = sys.argv[1]
    if param == '-h' or param == '--help':
        print(txt_help)
    elif param == '-v' or param == '--version':
        print('Cripto 0.0.2')
    elif param=='-c' or param=='--cripto' or param=='-d' or param=='--decripto':
        try:
            param2 = sys.argv[2]
            if param2=='-t' or param2=='--texto':
                try:
                    text = sys.argv[3]
                    text = sys.argv[3:]
                    text = ' '.join(text)
                    if param=='-c' or param=='--cripto':
                        text = Criptografar(text)
                    elif param=='-d' or param=='--decripto':
                        text = Descriptografar(text)
                    print(text)
                except IndexError:
                    print_error()
            elif param2=='-a' or param2=='--arquivo':
                try:
                    nome_arq = sys.argv[3]
                    try:
                        arq = open(nome_arq, 'r')
                    except FileNotFoundError:
                        print('Arquivo ou diretório não encontrado!!')
                        quit()
                    text=arq.read()
                    arq.close()
                    if param=='-c' or param=='--cripto':
                        text = Criptografar(text)
                        arq = open('criptografado.txt', 'w')
                    elif param=='-d' or param=='--decripto':
                        text = Descriptografar(text)
                        arq = open('descriptografado.txt', 'w')
                    arq.write(text)
                    arq.close()
                except IndexError:
                    print_error()
        except IndexError:
            print_error()
except IndexError:
    print_error()
