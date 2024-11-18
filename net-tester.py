import os
import time
import socket

rede = 'nome-da-sua-rede' #nome da rede da sua internet
tempo = 2 #tempo de espera para realizar novo teste (em minutos)
contador = 0 # contador para quantas vezes a internet foi reconectada

#exibe a interface principal do programa
def exibir_interface():
    os.system('cls')
    print("""
███╗   ██╗███████╗████████╗     ████████╗███████╗███████╗████████╗███████╗██████╗ 
████╗  ██║██╔════╝╚══██╔══╝     ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██╔██╗ ██║█████╗     ██║           ██║   █████╗  ███████╗   ██║   █████╗  ██████╔╝
██║╚██╗██║██╔══╝     ██║           ██║   ██╔══╝  ╚════██║   ██║   ██╔══╝  ██╔══██╗
██║ ╚████║███████╗   ██║           ██║   ███████╗███████║   ██║   ███████╗██║  ██║
╚═╝  ╚═══╝╚══════╝   ╚═╝           ╚═╝   ╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
""")
    print('----------------------------------------------------------------------------------')
    print('conexão estável')
    print(f'Reconexões feitas até o momento: {contador} \n')

#função para verificar se o computador está conectado à internet
def esta_conectado():
    try:
        socket.create_connection(("www.google.com", 80), timeout=5) # Tenta se conectar ao servidor do Google (IP e porta 80 - HTTP)
        return True 
    except OSError:
        return False 

#loop que desconecta, e conecta de novo o computador com a internet a cada 10 segundos, para que a conexão volte
def reconectar(rede):
    global contador
    while True:
        print('desconectando rede...')
        os.system('netsh wlan disconnect')
        time.sleep(10)
        print('conectando rede...')
        os.system(f'netsh wlan connect name="{rede}"')
        time.sleep(10)

        if esta_conectado():
            contador += 1
            break
        else:
            continue

#loop principal
while True:
    if not esta_conectado():
        print('conexão perdida, iniciando procedimentos...')
        reconectar(rede)
    exibir_interface()
    time.sleep(tempo * 60)