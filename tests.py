from main import *

# Carregar o vocabulário a partir do ficheiro
dic = carregarVocabulario('vocabulario.txt')


print("---- TESTE VOCABULÁRIO ----")
print(f"Número de palavras: {len(dic)}")
print()


# Texto de exemplo para testar a separação em palavras
print("---- TESTE FUNÇÃO gerarPalavras ----")
texto = """
Em 2020 observamos, e catalogamos (com fotografias), os barcos que chegaram ao Porto! 
Até breve.
"""

for p in gerarPalavras(texto):
    print(p)

print()


# Teste para o cálculo da distância mmLetras entre palavras
print("---- TESTES FUNÇÃO mmLetras ----")
print(f"promessa vs promessa -> {mmLetras('promessa', 'promessa')}")
print(f"promessa vs passagem -> {mmLetras('promessa', 'passagem')}")
print(f"antes vs depois -> {mmLetras('antes', 'depois')}")
print()


# Teste para o cálculo da distância de edição entre palavras
print("---- TESTES FUNÇÃO edicoes ----")
print(f"promessa vs promessa -> {edicoes('promessa', 'promessa')}")
print(f"promessa vs passagem -> {edicoes('promessa', 'passagem')}")
print(f"antes vs depois -> {edicoes('antes', 'depois')}")
print()


# Teste para verificar as sugestões de palavras próximas pelo critério mmLetras
print("---- TESTE FUNÇÃO sugerir COM CRITÉRIO DE DISTÂNCIA mmLetras ----")
print(f"promeessa -> {sugerir(dic, 'promeessa', mmLetras, 2)}")
print()


# Teste para verificar as sugestões de palavras próximas pelo critério edicoes
print("---- TESTE FUNÇÃO sugerir COM CRITÉRIO DE DISTÂNCIA edicoes ----")
print(f"promeessa -> {sugerir(dic, 'promeessa', edicoes)}")
print()


# Teste que mostra as palavras erradas e as sugestões pelo critério mmLetras
print("---- TESTE FUNÇÃO corretor COM CRITÉRIO DE DISTÂNCIA mmLetras ----")
teste = 'Este paragrafo teem moito ero de excrita.'
print(f"texto a corrigir: {teste}")
print()
corretor(dic, teste, mmLetras, 5)
print()


# Teste que mostra as palavras erradas e as sugestões pelo critério edicoes
print("---- TESTE FUNÇÃO corretor COM CRITÉRIO DE DISTÂNCIA edicoes ----")
print(f"texto a corrigir: {teste}")
print()
corretor(dic, teste, edicoes, 5)
print()