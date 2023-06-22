# Linguagens Formais

Trabalho Prático

## 1 Descrição

Implementar um Analisador léxico para uma determinada linguagem de programação. O analisador léxico deverá ser implementado de modo que o programa principal fará a leitura de um arquivo texto com o código fonte e realizará a análise léxica do código.
O analisador léxico deve ser implementado em uma função denominada le token(). Nesta etapa, o
programa principal deverá fazer a leitura do arquivo com o código fonte, chamar a função le token()
e escrever o token encontrado até que o final do arquivo seja alcançado. A função le token() deve
implementar o AF definido para especificar o analisador léxico, sendo que, a cada chamada desta
função deve retornar o token corrente do código fonte.

O analisador léxico para uma linguagem deve considerar um subconjunto de estruturas da linguagem (não precisa considerar todas as estruturas da linguagem, mas deve incluir uma de cada item
abaixo):

• Declarações de variáveis considerando os tipos inteiro, real e lógico;

• Comandos leitura e escrita;

• Comandos de atribuição;

• Comando condicional;

• Expressões aritméticas e seus operadores.

## 2 Instruções

Primeiramente deve ser feita uma especificação léxica da linguagem, descrevendo os tokens e padrões
de formação.

Exemplo: Linguagem X

• Token: ID ; Padrão de formação: letra(letra+dígito)*

• Token: Nreal ; Padrão de formação: dígito+.dígito∗

• Token: Nint ; Padrão de formação: dígito+

• Token: Nstring ; Padrão de formação: “(letra + dígito + simbolo)∗”

• Token: op ; Padrão de forma¸c˜ao: ‘+’ + ‘-’ + ‘*’ + ‘/’ + ‘=’

Obs.: espaços em branco e quebras de linha devem ser descartados durante o reconhecimento dos
tokens.

## 3 Entrega

O trabalho poderá ser realizado em grupos de até 4 componentes, na linguagem de programação que o
grupo escolher. Obs.: não é permitido usar nenhuma biblioteca pronta na linguagem de programação
escolhida.

A entrega será feita pelo Moodle até o dia 10/07/2023 às 18h00min. Deverá ser entregue:

• O código do trabalho;

• especificação léxica de acordo com a linguagem escolhida;

• dois arquivos de teste;

• manual de como executar o programa.

A apresentação será realizada para a turma no mesmo dia, durante a aula.

## 4 Avaliação

A avaliação será feita tanto na parte prática, a partir dos códigos elaborados e da execução dos
mesmos, quanto da parte teórica, observando conhecimento de conceitos e estrutura estudadas.
A nota será computada nos trabalhos assíncronos (TA), que consta no plano de ensino, com um
peso 6 nessa média.

5 Linguagens

• Fortran

• C

• Java

• Pascal

• Python

• PHP

• Haskell

• Prolog

Bom trabalho!!!
