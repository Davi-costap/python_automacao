# Passo a passo do projeto:

# 1- Abrir o sistema da empresa
# 2- Fazer login
# 3- Abrir/Importar a base de dados de produtos para cadastrar
# 4- Cadastrar um produto
# 5- Repetir isso tudo até acabar a lista de produtos

# A base de dados encontra-se no link: https://drive.google.com/drive/folders/1zQW4W9_L600WEBm0-4C-3I68eDJymF18?usp=sharing

# -----------------------------------------------------------------------------

# pyautogui.click -> clica com o mouse
# pyautogui.write -> escreve um texto
# pyautogui.press -> pressiona uma tecla do teclado
# pyautogui.hotkey -> aperta um conjunto de teclas


import pyautogui as pa
import pandas as pd
import time

pa.PAUSE = 0.5 #Espera 0.5 segundos a cada comando


#Abrir o navegador Chrome:
pa.press("win")
pa.write("Chrome")
pa.press("enter")

#Entrar no link:
pa.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") #Link disponibilizado
pa.press("enter")

time.sleep(3) #Espera 3 segundos para carregador o site

#Fazer login
pa.click(x=702,y=466)
pa.write("davicosta15@gmail.com")
pa.press("tab")
pa.write("#GMSTd52")
pa.press("enter")

time.sleep(3)

#Importar base de dados de produtos para cadastrar
tabela = pd.read_csv("produtos.csv") #Se nao tivesse na mesma pasta eu teria que colocar o caminho do caminho do arquivo


for linha in tabela.index: #As linhas das tabelas no pandas são chamadas de index
    #Cadastrar um produto
    codigo = str(tabela.loc[linha,"codigo"]) #codigo é o nome da coluna. Localizamos o valor que esta na tabela
    #Clicar no campo do código do produto
    pa.click(x=689, y=323)
    #Preencher o código
    pa.write(codigo)
    pa.press("tab")
    #marca
    marca = str(tabela.loc[linha,"marca"])
    pa.write(marca)
    pa.press("tab")
    #tipo
    tipo = str(tabela.loc[linha,"tipo"])
    pa.write(tipo)
    pa.press("tab")
    #categoria
    categoria = str(tabela.loc[linha,"categoria"])
    pa.write(categoria)
    pa.press("tab")
    #preço
    preco_unitario = str(tabela.loc[linha,"preco_unitario"])
    pa.write(preco_unitario)
    pa.press("tab")
    #custo
    custo = str(tabela.loc[linha,"custo"])
    pa.write(custo)
    pa.press("tab")
    #obs
    obs = str(tabela.loc[linha,"obs"])
    if obs == "nan":
        print("")
    else:
        pa.write(obs)
    pa.press("tab")
    #enviar
    pa.press("enter")
    #voltar para cima
    pa.scroll(5000)
    
    # Repetir o processo de cadastro até o fim