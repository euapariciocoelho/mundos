string = "Aparicio Nascimento"
'''vai do indice 2 até o 3'''
print(string[2:4])
'''vai do indice 2 até o 8 de 2 em 2'''
print(string[2:9:2])
'''começa do inicio e vai até o 5'''
print(string[:5])
'''vai até o final'''
print(string[1:])
'''começa em 0 : : vai até o final de 2 em 2'''
print(string[0::2])
'''tamanho da string'''
print(len(string))
'''contar caractere'''
print(string.count('o'))
'''indicar onde começa, quando não existir retorna -1'''
print(string.find('ricio'))
'''começa a procurar de trás para frente e retorna a posição'''
print(string.rfind('o'))
''' Palavra in string, in informa se existe com True'''
'''Trocar palavra'''
teste = string.replace("Nascimento", "Coelho")
print(teste)
'''string.upper() deixa maiuscula, string.lower() deixa minusculo'''
'''string.captalize() deixa tudo me minusculo, só a primeira letra da frase em maiusuculo'''
'''strting.tittle() deixa cada letra da palavra após espaço em maiusculo'''
'''string.strip() remove espaços inuteis antes do inicio e após o fim'''
'''string.rstrip() tira da direita, string.lstrip() da esquerda'''

'''string.split() dividir uma string em palavras em uma lista'''
'''  ' '.join(string)  com o split separa em palavras, com join junta  '''

print("""It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).""")

'''vai retirar os espaços'''
'''palavra = str(input("Palavra")).strip()'''
nome = str(input("Nome: "))
lista_nomes = nome.split()
print(lista_nomes)
print("primeiro nome {} e ultimo nome {}".format(
    lista_nomes[0], lista_nomes[len(lista_nomes)-1]))
