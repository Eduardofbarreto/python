import tkinter as tk

def calcular_dobro():
    try:
        numero = int(entrada.get())
        resultado = numero * 2
        label_resultado.config(text=f"O dobro de {numero} é {resultado}.")
    except ValueError:
        label_resultado.config(text="Por favor, instira um número válido.")        

janela = tk.Tk()
janela.title("Calculadora de Dobro")        
janela.geometry("400x300")

entrada = tk.Entry(janela, font=("Arial", 14))
entrada.pack(pady=10)

botao_calcular = tk.Button(janela, text="Calcular", command=calcular_dobro)
botao_calcular.pack(pady=10)

label_resultado = tk.Label(janela, text="", font=("Arial", 14))
label_resultado.pack(pady=10)

janela.mainloop()