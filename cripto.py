#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/python3
"""
Este módulo é responsável por criptografar ou descriptografar textos inseridos 
diretamente pelo terminal e retornar o texto no mesmo. Além disso é possível realizar a 
criptografia ou descriptografia de um arquivo. A saída pode ser armazenada em um arquivo 
texto com o nome desejado.

Autores: Allainn Tavares e Marcos Anjos       

Data Criação: 25/02/2020

Versão: 0.1.3

Este módulo é executado diretamente no terminal ou por meio do Shell Script passando como 
argumentos a opção de criptografar ou descriptografar e a opção se o método escolhido será 
aplicado em  um arquivo ou texto, acompanhado pelo nome do arquivo ou o texto. Também pode
ser passado o argumento se deseja salvar a saída em um arquivo acompanhado com o nome do 
arquivo a ser gerado.

Exemplos:

Criptografando um texto direto do terminal:

.. code-block:: shell
    
    $ python3 cripto.py --cripto --texto peso
    Criptografado com sucesso:
    hpuU

Descriptografando um texto direto do terminal:

.. code-block:: shell
    
    $ python3 cripto.py --decripto -t hpuU
    Descriptografado com sucesso:
    Peso

Criptografando um arquivo de texto:

.. code-block:: shell
    
    $ python3 cripto.py -c --arquivo texto.txt
    Criptografado com sucesso:
    (¾"`j¦"qÍ{ìh
    -5PiWs-gfTvcÈ(
              Wn|#Bínnd¦rcWy°#à}Ï"uù-u¤%


Descriptografando um arquivo de texto:

.. code-block:: shell
    
    $ python3 cripto.py -d -a texto_cripto.txt
    Descriptografado com sucesso:
    Um exemplo de texto em um arquivo a ser criptografado!

Também é possível salvar a saída em um arquivo de texto, basta utilizar o '-s' ou '-\-salvar', 
podendo ser utilizado em conjunto de com um texto direto do terminal ou proveniente de um 
arquivo:

.. code-block:: shell
    
    $ python3 cripto.py -c -a texto.txt --salvar texto_cripto.txt
    Criptografado com sucesso:
    Salvo no arquivo texto_cripto.txt

.. code-block:: shell
    
    $ python3 cripto.py -c -a texto_cripto.txt -s texto_des.txt
    Descriptografado com sucesso:
    Salvo no arquivo texto_des.txt

Para mais informações pode se utilizar o '-h' ou '--help':

.. code-block:: shell
    
    $ python3 cripto.py -h
    usage: cripto.py [-c] [-d] [-t TEXTO] [-a ARQUIVO] [-s ARQUIVO] [-v] [-h]

    Criptografa ou Descriptografa um ARQUIVO ou TEXTO.

    Argumentos:
    -c, --cripto          Criptografar
    -d, --decripto        Descriptografar
    -t TEXTO, --texto TEXTO
                            Entrada de texto
    -a ARQUIVO, --abrir ARQUIVO
                            Entrada de arquivo
    -s ARQUIVO, --salvar ARQUIVO
                            Salvar no arquivo
    -v, --version         Exibe a versão.
    -h, --help            Mostra esta mensagem.

"""
import sys
import math
import argparse

VERSAO='0.1.3'

def Fibonacci(n): 
    """
    Método responsável em buscar o valor de Fibonacci de uma determiada posição que é
    recebida por parâmetro.

    O método utiliza de recursividade para encontrar o valor desejado.

    :param n: Posição que se deseja para obter o valor de Fibonacci
    """
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
    """
    Método responsável em informar ao usuário o modo de uso do módulo acompanhado por 
    exemplos. A mensagem é exibida em caso de erro ao tentar executá-lo.

    Está mensagem poderá ser exebida em caso de não passar o parâmetro de criptografia ou
    descriptografia, ou mesmo passar ambos os parâmetros. 
    
    Também pode ocorrer está mensagem no caso de haver corretamente o parâmetro de 
    criptografia ou descriptografia, mas está faltando o parâmetro de texto ou arquivo, ou
    mesmo foi passado os dois parâmetros.
    """
    print("\nUso: python3 cripto.py [-c] [-d] [-t TEXTO] [-a ARQUIVO] [-s ARQUIVO] [-v] [-h]")
    print("\nExemplo:")
    print("python3 cripto.py -c -t Peso")
    print("python3 cripto.py -d -a texto.txt")


def Criptografar(texto):
    """
    Método responsável em realizar a criptografia de um texto recebido por parâmetro.

    A criptografia é realizada seguindo os seguintes passos:
    
    * Inverte o texto
    * Troca as letras utilizando o Fibonacci de 3 a 15 como chave:
        
        * Soma o valor de Fibonacci a letra
        * Obtém o resto da divisão do resultado por 254
        * O resultado é a nova letra

    * Transpõe o novo texto utilizando uma matriz quadrada: 

        * O texto é adicionado na matriz
        * Percorre a matriz em zig-zag gerando o texto final

            * Sobe nas colunas pares e desce nas colunas ímpares.

    * O texto final é retornado

    :param texto: Texto a ser criptografado

    :returns: Texto criptografado 
    """
    tam=len(texto)
    texto = texto[::-1]
    x=math.sqrt(tam)
    if x>int(x):
        num=int(x)+1
    else:
        num=int(x)

    x=num**2
    if x > tam:
        x-=tam
        comp=x*' '
        texto+=comp
        
    mat = []
    cont = 0
    fib = 3
    for i in range(num):
        aux=[]
        for j in range(num):
            aux.append(chr((ord(texto[cont])+Fibonacci(fib)) % 254))
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

    print("Criptografado com sucesso:")
    return newText


def Descriptografar(texto):
    """
    Método responsável em realizar a descriptografia de um texto recebido por parâmetro. 

    A descriptografia é realizada seguindo os seguintes passos:
    
    * Transpõe o novo texto utilizando uma matriz quadrada: 

        * O texto é adicionado na matriz em zig-zag

            * Adiciona subindo nas colunas pares e descendo nas colunas ímpares
        
    * Percorre a matriz normalmente gerando o novo texto
    * Troca as letras utilizando o Fibonacci de 3 a 15 como chave:
        
        * Subtrai o valor de Fibonacci a letra
        * Obtém o resto da divisão do resultado por 254
        * O resultado é a nova letra
    
    * Inverte o novo texto
    * O texto final é retornado

    :param texto: Texto a ser descriptografado

    :returns: Texto descriptografado 
    """
    tam=len(texto)
    x=math.sqrt(tam)
    if x>int(x):
        num=int(x)+1
    else:
        num=int(x)

    x=num**2
    if x > tam:
        x-=tam
        comp=x*' '
        texto+=comp
    
    cont=0
    mat = [ [0 for i in range(num)] for j in range(num)]
    for j in range(num):
        if j%2==0:
            for i in range(num-1, -1, -1):
                mat[i][j]=texto[cont]
                cont+=1
        else:
            for i in range(num):
                mat[i][j]=texto[cont]
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
    print("Descriptografado com sucesso:")
    return oldText

def main():
    """
    Método responsável em validar os argumentos provenientes da chamada do módulo via
    terminal.

    É realizado a criação dos argumentos e a validação dos mesmos, de modo que é preciso ter
    o argumento de criptografia ou descriptografia (não pode ambos) e o argumento de texto 
    ou arquivo (não pode ambos). O argumento de salvar pode ser também passado pelo usuário.

    Caso o argumentos sejam de criptografar e texto, o valor do texto é obtido e este método
    redireciona para o método Criptografar passando o texto. Caso for descriptografar, a
    única diferença é a chamada do método, que neste caso é o método Descriptografar.

    Quando se trata em realizar a criptografia ou descriptografia de um arquivo, 
    primeiramente o arquivo é aberto e capturado seu texto, para então ser chamado o método
    Criptografar ou Descriptografar.

    Se não houver o parâmetro de salvar em um arquivo, a criptografia ou a descriptografia é
    exibida diretamente no terminal. Caso se deseja salvar, é capturado o nome do arquivo 
    passado e então é gerado o arquivo com o conteúdo da saída.

    No interior deste método, há um método chamado validar, que recebe como parâmetro uma
    função. Este método é responsável em validar os argumentos de texto e arquivo, 
    verificando se foi passado apenas um destes argumentos e então realizando a tarefa 
    escolhida, texto ou arquivo. A função recebida pode ser Criptografar ou Descriptografar, 
    de modo que há validação é realiza por fora da função, e a mesma só tem a obrigação de 
    executar a função passada no contexto validado como descrito.
    """
    parser = argparse.ArgumentParser(description="Criptografa ou "
                            +"Descriptografa um ARQUIVO ou TEXTO.", 
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
        """
        Método verificar
        """
        if args.texto and not(args.abrir):
            return func(args.texto)
        elif not(args.texto) and args.abrir:
            try:
                arq = open(args.abrir, 'r')
            except FileNotFoundError:
                print('Arquivo ou diretório não encontrado!!')
                quit()
            texto=arq.read()
            arq.close()
            return func(texto)
        else:
            print("Error!")
            print("Não foi passado o argumento de texto ou "
                +"arquivo, ou foi passado ambos os argumentos!")
            print_error()
            quit()

    if args.cripto and not(args.decripto):
        texto = verificar(Criptografar)
    elif args.decripto and not(args.cripto):
        texto = verificar(Descriptografar)
    else:
        print("Error!")
        print("Não foi passado o argumento de criptografia ou "
            +"descriptografia, ou foi passado ambos os argumentos!")
        print_error()
        quit()

    if args.salvar:
        arq = open(args.salvar, 'w')
        arq.write(texto)
        arq.close()
        print("Salvo no arquivo " + args.salvar) 
    else:
        print(texto)

if __name__ == "__main__":
    main()