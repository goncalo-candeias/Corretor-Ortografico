import re


# Carrega o ficheiro vocabulário 
# Devolve uma lista, ordenada lexicograficamente, e sem repetições
def carregarVocabulario(filename):
  dic = set()
  for line in open(filename, 'r', encoding='utf8'):
    dic.add(line.rstrip().lower())
  return sorted(dic)


# Recebe um texto e devolve uma lista com todas as palavras encontradas.
# Remove números, pontuação e símbolos.
def gerarPalavras(texto):
    return [palavra for palavra in re.split(r'[\W\d]+', texto) if palavra != '']


# Devolve a diferença entre o tamanho da maior palavra dada e o número de letras iguais nas mesmas posições entre as duas palavras
def mmLetras(palavra1, palavra2):
    letras_iguais = 0
    maior_tamanho = max(len(palavra1), len(palavra2))

    for x in range(min(len(palavra1), len(palavra2))):
        if palavra1[x] == palavra2[x]:
            letras_iguais += 1
    
    return maior_tamanho - letras_iguais


# Devolve o número mínimo de operações de edição necessárias para transformar uma palavra na outra
def edicoes(palavra1, palavra2):
    m = len(palavra1)
    n = len(palavra2)
    matriz = [[0]*(n+1) for zeros in range(m+1)]
    
    for i in range(m+1):
        matriz[i][0] = i

    for j in range(n+1):
        matriz[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if palavra1[i-1] == palavra2[j-1]:
                matriz[i][j] = matriz[i-1][j-1]
            else:
                inserir = matriz[i][j-1] + 1
                remover = matriz[i-1][j] + 1
                substituir = matriz[i-1][j-1] + 1
                matriz[i][j] = min(inserir, remover, substituir)
    
    return matriz[i][j]


# Devolve uma lista ordenada de sugestões de palavras do vocabulário mais próximas da palavra dada, usando a função de distância fornecida
# Em caso de ter de se escolher uma de duas palavras com a mesma distância, opta-se pela com menor ordem lexicográfica
def sugerir(dic, palavra, distancia, maxSugestoes=5):
    distancia_palavras = [(distancia(vocabulario, palavra), vocabulario) for vocabulario in dic]
    distancia_palavras_ordenado = sorted(distancia_palavras)
    sugestoes = [palavra for vocabulario, palavra in distancia_palavras_ordenado[:maxSugestoes]]
    resultado = sorted(sugestoes)
    return resultado


# Recebe um texto e imprime as palavras não reconhecidas juntamente com as sugestões de correção
def corretor(dic, texto, distancia, maxSugestoes=5): 
    palavras = gerarPalavras(texto)
    for vocabulario in palavras:
        if vocabulario not in dic:
            print(f"{vocabulario} --> {sugerir(dic, vocabulario, distancia, maxSugestoes)}")

