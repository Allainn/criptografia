<div align="center">
   <h1 align="center">
   Algoritmo de Criptografia e Descriptografia
  </h1>
<img src="https://img.icons8.com/cute-clipart/64/000000/lock.png"/>
  <img src="https://img.icons8.com/dusk/150/000000/hacker.png"/>
<img src="https://img.icons8.com/cute-clipart/64/000000/unlock.png"/>
</div>

Algoritmo responsável por criptografar ou descriptografar textos ou arquivos, em caso de criptografar/descriptografar um arquivo, é gerado um arquivo de saída, ao criptografar/descriptografar um texto, a mensagem é exibida no terminal.

- [x] Algoritmo responsável por 🔒criptografar ou 🔓descriptografar textos inseridos diretamente pelo terminal e retornar o texto no mesmo. Além disso é possível realizar a criptografia ou descriptografia de um arquivo. A saída pode ser armazenada em um arquivo texto com o nome desejado.

🧠 A criptografia utilizada faz o uso de transposição matricial e a criptografia de cezar utilizando como chave uma sequência de Fibonacci.

## ✋🏻 Pré-requisitos

1.  Python 3.6
2.  Editor de texto, exemplo vscode.

## 🔥 Instalação e execução

1.  Faça um clone desse repositório:
    `git clone https://github.com/Allainn/criptografia.git`
2.  Entre na pasta `cd master`;
    Na pasta ` criptografia` execute no terminal `$ python3 cripto.py [-c] [-d] [-t TEXTO] [-a ARQUIVO] [-s ARQUIVO] [-v] [-h]`

- Na duvida consulta o **help**:

      $ pyhton3 cripto.py -h
        Criptografa ou Descriptografa um ARQUIVO ou TEXTO.
          Argumentos:
            -c, --cripto                     Criptografar
            -d, --decripto                   Descriptografar
            -t TEXTO, --texto TEXTO          Entrada de texto
            -a ARQUIVO, --abrir ARQUIVO      Entrada de arquivo
            -s ARQUIVO, --salvar ARQUIVO     Salvar no arquivo
            -v, --version                    Exibe a versão.
            -h, --help                       Mostra esta mensagem.

📝**Exemplo**:
`python3 cripto -c -t Teste`
`python3 cripto -d -a criptografado.txt`

## 📒 Documentação

🔶 [Documentação do projeto](https://allainn.github.io/criptografia/build/html/)

<div align="center">
   <h2 align="center">
   🔒 Algoritmo de Criptografia 🔒
  </h2>
<img src="./docs/img/criptografia.png"/>
</div>

<div align="center">
   <h2 align="center">
   🔓 Algoritmo de Descriptografia 🔓
  </h2>
<img src="./docs/img/criptografia.png"/>
</div>

## ⚡ Como contribuir

- Faça um `fork` desse repositório;
- Cria uma branch com a sua feature: `git checkout -b minha-feature`;
- Faça commit das suas alterações: `git commit -m 'feat: Minha nova feature'`;
- Faça push para a sua branch: `git push origin minha-feature`.

Depois que o `merge` da sua `pull request` for feito, você pode deletar a sua `branch`.

## 👨🏼‍💻 Desenvolvedores

<h4>Allainn Christiam</h4>
<a href="https://github.com/Allainn"><img alt="Twitter" src="https://img.shields.io/badge/github-%23100000.svg?&style=for-the-badge&logo=github&logoColor=white"></a>
<a href="https://www.linkedin.com/in/allainn/"><img alt="Linkedin" src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white"></a>

<h4>Marcos Alexandre</h4>
<a href="https://github.com/MarcosAnjos"><img alt="Twitter" src="https://img.shields.io/badge/github-%23100000.svg?&style=for-the-badge&logo=github&logoColor=white"></a>
<a href="https://www.linkedin.com/in/marcos-alex/"><img alt="Linkedin" src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white"></a>
