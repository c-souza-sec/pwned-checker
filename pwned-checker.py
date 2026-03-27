import requests
import hashlib

senha = input("Digite sua senha: ")

sha1_hash = hashlib.sha1()
sha1_hash.update(senha.encode('utf-8'))
hash_value = sha1_hash.hexdigest()

prefixo = hash_value[:5]
sufixo = hash_value[5:].upper()

try:
    resposta = requests.get(f"https://api.pwnedpasswords.com/range/{prefixo}")

    for linha in resposta.text.splitlines():
        partes = linha.split(':')
        hash_linha = partes[0]
        quantidade = partes[1]

        if hash_linha == sufixo:
            print(f"Senha vazada {quantidade} vezes")
            break
    else:
        print("Senha nao encontrada!")

except requests.exceptions.RequestException:
    print("Erro ao conectar com a API")