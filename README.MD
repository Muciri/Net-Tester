# Net Tester

Um script Python para monitoramento e reconexão automática à internet. Este projeto verifica periodicamente se há conexão de rede e, em caso de perda de conexão, tenta reconectar-se automaticamente a uma rede Wi-Fi específica.

## Funcionalidades

- Verifica continuamente se o computador está conectado à internet.
- Em caso de perda de conexão, desconecta e reconecta automaticamente à rede Wi-Fi configurada até restabelecer a conexão.

## Requisitos

- Python 3.x
- Sistema operacional Windows (o script usa comandos `netsh`, específicos para o ambiente Windows).

## Configuração
(como este é um projeto para uso próprio, a idéia é eu mesmo ir no VScode e mudar as variáveis quando for rodar o programa)
1. **Clone o repositório** ou copie o código do script para seu ambiente local.

2. **Edite o código** para incluir o nome da sua rede Wi-Fi:
   ```python
   rede = 'NOME_DA_SUA_REDE'  # Substitua pelo nome da rede à qual deseja se conectar

### observação: este programa não funciona em Linux