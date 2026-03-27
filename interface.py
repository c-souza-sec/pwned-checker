import tkinter as tk
import requests
import hashlib

janela = tk.Tk()
janela.eval('tk::PlaceWindow . center')
janela.title("Minha senha foi vazada?")
janela.geometry("700x500")
janela.configure(bg="#1e1e1e")

label = tk.Label(
    janela,
    text="Digite sua senha abaixo",
    font=("Arial", 14),
    bg="#1e1e1e",
    fg="white"
)
label = tk.Label(janela, text="Digite sua senha abaixo para verificar se foi vazada", font=("Arial", 14))
label.pack(pady=20)

entrada = tk.Entry(janela, width=30, show="*", font=("Arial", 12))
entrada.pack(pady=10)

resultado = tk.Label(janela, text="", font=("Arial", 12), bg="#1e1e1e", fg="white")
resultado.pack(pady=20)

def mostrar_texto():
    resultado.config(text="")
    senha = entrada.get()  
    if senha == "":
        resultado.config(text="Digite uma senha!")
        return
    sha1_hash = hashlib.sha1()
    sha1_hash.update(senha.encode('utf-8'))
    hash_value = sha1_hash.hexdigest()

    prefixo = hash_value[:5]
    sufixo = hash_value[5:].upper()

    resultado.config(text="Verificando...")
    janela.update()

    try:
        resposta = requests.get(f"https://api.pwnedpasswords.com/range/{prefixo}")
    except:
        resultado.config(text="Erro ao conectar com a API", fg="orange")
        return


    for linha in resposta.text.splitlines():
        partes = linha.split(':')
        hash_linha = partes[0]
        quantidade = partes[1]

        if hash_linha == sufixo:
            resultado.config(text=f"Senha vazada {quantidade} vezes!", fg="red")
            break
    else:
        resultado.config(text="Senha nao encontrada!", fg="lightgreen")

botao = tk.Button(
    janela,
    text="Verificar",
    command=mostrar_texto,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12),
    padx=10,
    pady=5,
    bd=0
)
botao.pack(pady=10)
janela.mainloop()