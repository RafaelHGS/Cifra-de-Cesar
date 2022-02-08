# Cifra-de-Cesar
Teste sobre Cifra de Cesar, com algumas modificações


# O que é e proposta do código:
  A Cifra de César é basicamente um método de Criptografia antigo, na qual consiste em embaralhar as letras do alfabeto por meio de "equivalência de letras", na qual antigametne eram usados dois discos, um externo e um interno, onde dependendo da rotação dos discos, era gerado a criptografia do texto. Para exemplo disso, quando a rotação de um disco era de duas rotações, significa que a letra "A", passava à ser a 3ªLetra adiante dela, ou seja, a letra "D", e assim sucessivamente com todas as seguintes letras.
  O código implementado tem essa funcionalidade/conceito e um pouco mais além da cifra comum, o código apresenta as "Key's" (chaves, que são a representação do número das rotações dos discos), ou seja, como as letras de uma frase/texto ficarão embaralhados, não só isso como o uso de "múltiplas Keys", enquanto muitas das Cifras apresentam apenas uma única key, ou seja, a mesma movimentação para todas as letras (se a Key é 1, é uma rotação para todas as letras), no código há a funcionalidade de usar múltiplas keys por letras, deixando essa "criptografia" um pouco mais dinâmica, na qual a cada letra é uma rotação diferente da Key.
  ```
  Ex:
  texto = aaaa
  keys usadas = 1 7 5
  frase final = Bhfb
  ```
 
# Funcionalidades do código:
  O código apresenta 3 funções básicas, sendo elas a Criptografia, a Descriptografia e um gerador de keys.
  - Na Criptografia podemos adicionar um texto e colocar neles quantas Key's quisermos para serem usadas no texto (na qual é mantido os espaços, mesmo "alterando a letra" em cada espaço, simbolos também não são alterados, apenas as letras comuns do nosso alfabeto)
  - Na Descriptografia, ao colocarmos o mesmo texto gerado na criptografia, com a mesma Key, ele irá devolver o texto original
  - No Gerador de keys, podemos gerar randomicamente num arquivo .txt uma key à ser usada na aba de criptografia, tendo duas funcionalidades, a primeira é utilizar gerar uma "quantidade específica de key's", ou seja, será perguntado "quantas keys você deseja utilizar", se sua resposta for "10", serão gerados 10 números aleatórios para serem usados como Key's no arquivo .txt. A segunda opção é gerar uma key por caractere de frase, sim, isso mesmo, você irá colocar uma frase nesse gerador e ele irá te devolver uma key diferente e randômica por caractere no texto, ou seja, se seu texto tiver 600 caracteres, serão geradas 600 keys para cada um deles, para ser usada na aba "criptografia" do código.

# Bugs não resolvidos
  - Key por letra, independente do espaço. O código não diferencia Espaços de letras, portanto sempre quando há um espaço, em teoria ele está "trocando o espaço por uma letra", ou seja, os espaços contam na hora da criptografia.
 ```
 Ex:
 Frase original: a aa
 Keys para criptografia: 2 1 2
 Resposta esperada: C BC (trocando apenas as letras)
 Resposta obtida: C CC (pois teoricametne ele trocou o espaço com a rotação de Key = 1)
```
# Sugestões
  Aceito sugestões e ajuda para a melhora do código, incluindo ajuda para a codificação também de números e simbolos, e também para ignorar o espaço e trocar somente a key por letra.
