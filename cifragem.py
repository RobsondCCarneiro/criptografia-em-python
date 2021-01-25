alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


mensagem = "EU GOSTO DOS FILMES DE STEVEN SPIELBERG"
mensagem = mensagem.upper()
data = "18/12/46"

data = data.replace('/','')

a = len(alfabeto)
d = len(data)
m = len(mensagem)

chave = ""
indData = 0
for i in range(0, m):
    if(mensagem[i] == " "):
        chave = chave + " "
    else:
        chave = chave + data[indData]
        if(indData < d - 1):
           indData = indData+1
        else:
            indData = 0
print(chave)

cifrada = ""
indChave=0
for letra in mensagem:
    if(letra == " "):
        cifrada = cifrada + " "
        indChave = indChave + 1
    else:
        indice = alfabeto.index(letra)
        vchave = int(chave[indChave])
        nova_letra = alfabeto[(indice + vchave)%a]
        cifrada = cifrada + nova_letra
        indChave = indChave + 1

print(mensagem)
print(cifrada)
