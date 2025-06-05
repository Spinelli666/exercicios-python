# os.listdir para navegar em caminhos
# /Users/nome/Desktop/EXEMPLO
# C:\Users\nome\Desktop\EXEMPLO
# caminho = r'C:\\Users\\nome\\Desktop\\EXEMPLO'

import os

caminho = os.path.join('/Users', 'nome', 'Desktop', 'EXEMPLO')

for pasta in os.listdir(caminho):

    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        print('  ', imagem)