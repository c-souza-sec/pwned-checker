import tkinter as tk
import requests
import hashlib

janela = tk.Tk()
janela.title("Minha senha foi vazada?")
janela.geometry("700x500")
label = tk.Label(janela, text="Digite sua senha abaixo para verificar se sua senha foi vazada", font=("Arial", 14))
label.pack()
entrada = tk.Entry(janela, width=30)
entrada.pack(pady=10)

def mostrar_texto():
    senha = entrada.get()  
    sha1_hash = hashlib.sha1()
    sha1_hash.update(senha.encode('utf-8'))
    hash_value = sha1_hash.hexdigest()

    prefixo = hash_value[:5]
    sufixo = hash_value[5:].upper()

    resposta = requests.get(f"https://api.pwnedpasswords.com/range/{prefixo}")

    for linha in resposta.text.splitlines():
        partes = linha.split(':')
        hash_linha = partes[0]
        quantidade = partes[1]

        if hash_linha == sufixo:
            resultado.config(text=f"Senha vazada {quantidade} vezes!")
            break
    else:
        resultado.config(text="Senha nao encontrada!")

resultado = tk.Label(janela, text="")
resultado.pack()


botao = tk.Button(janela, text="Enviar", command=mostrar_texto)
botao.pack()
janela.mainloop()