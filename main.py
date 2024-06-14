#janela 
#titulo 
#campos para selecionar as moedas de origem e destino 
#botão para coverter 
#lista de exibição com os nomes das moedas 


import customtkinter

#importar biblioteca que vai fazer a janea
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

janela = customtkinter.CTk()
janela.geometry("500x500")
#criar e configurar a janela

#criar os botões, textos e demais elementos 
titulo = customtkinter.CTkLabel(janela, text="Convertor de Moedas", font=("Times new roman",20))
texto_moedas_origem= customtkinter.CTkLabel(janela, text="Selecione a moeda de origem", font=("Times new roman",16))
texto_moeda_destino= customtkinter.CTkLabel(janela, text="Selecione a moedada de destino", font=("Times new roman",16))
campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values= ["USD", "EUR", "BRL", "BTC"])
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values= ["USD", "EUR", "BRL", "BTC"])

def converter_moeda():
    print("Converter Moeda")

botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda)

lista_moedas = customtkinter.CTkScrollableFrame(janela)

moedas_disponiveis = ["USD: DolarAmericano", "EUR ; Euro", "BRL: Real Brasileiro", "BTC: Bitcoin"]

for moeda in moedas_disponiveis:
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=moeda)
    texto_moeda.pack()

#moeda1 = customtkinter.CTkLabel(lista_moedas, text="USD: Dolar Americano")
#moeda2 = customtkinter.CTkLabel(lista_moedas, text="EUR: Euro")
#moeda3 = customtkinter.CTkLabel(lista_moedas, text="BRL: Real Brasileiro")
#moeda4 = customtkinter.CTkLabel(lista_moedas, text="BTC: Bitcoin")
#moeda1.pack()
#moeda2.pack()
#moeda3.pack()
#moeda4.pack()


#colocar os elementos criados na tela 
titulo.pack(padx=10, pady=10)
texto_moedas_origem.pack(padx=10, pady=10)
campo_moeda_origem.pack(padx=10, pady=10)
texto_moeda_destino.pack(padx=10, pady=10)
campo_moeda_destino.pack(padx=10, pady=10)
botao_converter.pack(padx=10, pady=10)
lista_moedas.pack(padx=10, pady=10)


#rodar a janela 
janela.mainloop()