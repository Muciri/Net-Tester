import os
import time
import socket

rede = 'nome-da-sua-rede' #nome da rede da sua internet
tempo = 6 #tempo de espera para realizar novo teste (em minutos)
tempo *= 60 #o comando "time.sleep" recebe o parâmetro de tempo em segundos, por isso é necessário converter para minutos

#faz um letreiro estiloso para o programa 
def exibir_letreiro():
    print("""
███╗   ██╗███████╗████████╗     ████████╗███████╗███████╗████████╗███████╗██████╗ 
████╗  ██║██╔════╝╚══██╔══╝     ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██╔██╗ ██║█████╗     ██║           ██║   █████╗  ███████╗   ██║   █████╗  ██████╔╝
██║╚██╗██║██╔══╝     ██║           ██║   ██╔══╝  ╚════██║   ██║   ██╔══╝  ██╔══██╗
██║ ╚████║███████╗   ██║           ██║   ███████╗███████║   ██║   ███████╗██║  ██║
╚═╝  ╚═══╝╚══════╝   ╚═╝           ╚═╝   ╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
""")
#função para verificar se o computador está conectado à internet
def esta_conectado():
    try:
        socket.create_connection(("www.google.com", 80), timeout=5) # Tenta se conectar ao servidor do Google (IP e porta 80 - HTTP)
        return True 
    except OSError:
        return False 

#loop que desconecta, e conecta de novo o computador com a internet a cada 10 segundos, para que a conexão volte
def testar_conexao(rede):
    while True:
        print('desconectando rede...')
        os.system('netsh wlan disconnect')
        time.sleep(10)
        print('conectando rede...')
        os.system(f'netsh wlan connect name="{rede}"')
        time.sleep(10)
        
        if esta_conectado():
            break
        else:
            continue

#programa principal
while True:
    if esta_conectado():
        os.system('cls')
        exibir_letreiro()
        print('conexão estável')
    else:
        print('conexão perdida, iniciando procedimentos...')
        testar_conexao(rede)
    time.sleep(tempo)