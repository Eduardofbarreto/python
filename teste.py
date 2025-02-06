import tkinter as tk

def calcular_soma():
    try:
        numero1 = float(entrada1.get())
        numero2 = float(entrada2.get())
        
        soma = numero1 + numero2
        label_resultado.config(text=f"A soma de {numero1} e {numero2} é {soma}.")
    except ValueError:
        label_resultado.config(text="Por favor, insira números válidos.")        

janela = tk.Tk()
janela.title("Calculadora de soma")        
janela.geometry("400x300")

label1 = tk.Label(janela, text="Digite o primeiro número: ")
label1.pack(pady=5)
entrada1 = tk.Entry(janela)
entrada1.pack(pady=5)

label2 = tk.Label(janela, text="Digite o segundo número: ")
label2.pack(pady=5)
entrada2 = tk.Entry(janela)
entrada2.pack(pady=5) 

botao_calcular = tk.Button(janela, text="Calcular soma", command=calcular_soma)
botao_calcular.pack(pady=10)

label_resultado = tk.Label(janela, text="", font=("Arial", 14))
label_resultado.pack(pady=10)

janela.mainloop()