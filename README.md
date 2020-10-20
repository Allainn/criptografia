# Algoritmo de criptografia e descriptografia

Algoritmo responsavel por criptografar ou descriptografar textos ou arquivos, em caso de criptografar/descriptografar um arquivo, é gerado um arquivo de saída, ao criptografar/descriptografar um texto, a mensagem é exibida no terminal.

Quando é criptografado um arquivo é gerado como saída o arquivo criptografado.txt.

Quando é descriptografado um arquivo é gerado como saída o arquivo descriptografado.txt.

A criptografia utilizada faz o uso de transposição matricial e a criptografia de cezar utilizando como chave uma sequência de Fibonacci.

	Uso: python3 cripto.py OPÇÃO(-c | -d) [-a ARQUIVO | -t TEXTO]
	
		-c, --cripto		criptografar
		-d, --decripto	descriptografar

		-t, --texto		entrada de texto
		-a, --arquivo		entrada de arquivo

		-h, --help		mostra esta ajuda e sai
		-v, --version		informa a versão e sai
	
	Exemplo:
		python3 cripto -c -t Teste
		python3 cripto -d -a criptografado.txt
