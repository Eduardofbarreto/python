import tkinter as tk

def calcular_tripo():
    try:
        numero = int(entrada.get())
        resultado = numero * 3
        label_resultado.config(text=f"O triplo de {numero} é {resultado}.")
    except ValueError:
        label_resulatdo.config(text="Por favor, insira um número válido.")        
        
janela = tk.Tk()
janela.title("Calculadora de Triplo")        

largura = 400
altura = 200
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
x = (largura_tela // 2) - (largura // 2)
y = (altura_tela // 2) - (altura // 2)

janela.geometry(f"{largura}x{altura}+{x}+{y}")

label_instrucao = tk.Label(janela, text="Digite um número para calcular o triplo: ", font=("Arial", 12))
label_instrucao.pack(pady=10)

entrada = tk.Entry(janela, font=("Arial", 14))
entrada.pack(pady=10)  

botao_calcular = tk.Button(janela, text="Calcular", command=calcular_tripo)
botao_calcular.pack(pady=10)

label_resultado = tk.Label(janela, text="", font=("Arial", 14))
label_resultado.pack(pady=10)

janela.mainloop()
