from main import *


# dic será uma lista com todas as palavras que estão no respetivo ficheiro
dic = carregarVocabulario('vocabulario.txt')

# Devolve o número de palavras no ficheiro vocabulário
print(len(dic))


# Teste da função gerarPalavras
# Verifica se o texto é corretamente dividido em palavras
texto = """
Em 2020 observamos, e catalogamos (com fotografias), os barcos que chegaram ao Porto! 
Até breve.
"""
for p in gerarPalavras(texto):
 print(p)


# Testes da função mmLetras
# Compara palavras iguais e diferentes
print( mmLetras('promessa', 'promessa') ) 
print( mmLetras('promessa', 'passagem') ) 
print( mmLetras('antes', 'depois') )  


# Testes da função edicoes
# Mede a distância de edição entre palavras
print( edicoes('promessa', 'promessa') ) 
print( edicoes('promessa', 'passagem') ) 
print( edicoes('antes', 'depois') ) 


# Testes da função sugerir
# Verifica sugestões de palavras próximas
print(sugerir(dic, 'promeessa', mmLetras, 2))
print(sugerir(dic, 'promeessa', edicoes))


# Testes da função corretor
# Mostra palavras erradas e sugestões
teste = 'Este paragrafo teem moito ero de excrita.'
corretor(dic, teste, mmLetras, 5)
teste = 'Este paragrafo teem moito ero de excrita.'
corretor(dic, teste, edicoes, 5)