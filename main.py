from pyscript import document

# Pegando a área do resultado na tela
elemento_resultado = document.getElementById('resultado')


elemento_resultado = document.getElementById('resultado')

def somar(event):
    try:
        n1 = float(document.getElementById('num1').value)
        n2 = float(document.getElementById('num2').value)
    








# -------------------------------------------------------
# Integrante 2: Implementar a Subtração
# -------------------------------------------------------
def subtrair(event):
    # Integrante 2, coloque sua lógica aqui
    pass

# -------------------------------------------------------
# Integrante 3: Implementar a Multiplicação
# -------------------------------------------------------
def multiplicar(event):
    # Integrante 3, coloque sua lógica aqui
    pass

# -------------------------------------------------------
# Integrante 4: Implementar a Divisão
# -------------------------------------------------------
def dividir(event):
    try:
        n1 = float(document.getElementById('num1').value)
        n2 = float(document.getElementById('num2').value)
        
        if n2 == 0:
            elemento_resultado.innerText = "Erro: Divisão por 0"
            return
            
        resultado = n1 / n2
        elemento_resultado.innerText = str(resultado)
    except ValueError:
        elemento_resultado.innerText = "Erro: Digite números válidos"
