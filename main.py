from pyscript import document
from js import document as js_document

# Pegando a área do resultado na tela
elemento_resultado = document.getElementById('resultado')

# Áudio
som = js_document.getElementById("somResultado")

def tocar_som():
    try:
        som.currentTime = 0
        # Em alguns navegadores play() retorna uma Promise
        som.play()
    except Exception:
        pass

def somar(event):
    try:
        n1 = float(document.getElementById('num1').value)
        n2 = float(document.getElementById('num2').value)
        resultado = n1 + n2
        elemento_resultado.innerText = str(resultado)
    except ValueError:
        elemento_resultado.innerText = "Erro: Digite números válidos"
        
# -------------------------------------------------------
# Integrante 2: Implementar a Subtração
# -------------------------------------------------------
def subtrair(event):
    try:
        n1 = float(document.getElementById("num1").value)
        n2 = float(document.getElementById("num2").value)

        resultado = n1 - n2

        elemento_resultado.innerText = str(resultado)

        tocar_som()

    except ValueError:
        elemento_resultado.innerText = "Erro: Digite números válidos"

# -------------------------------------------------------
# Integrante 3: Implementar a Multiplicação
# -------------------------------------------------------
def multiplicar(event):
    try:
        
        #obtem os valores digitados
        
        n1 = float(document.getElementById("num1").value)
        n2 = float(document.getElementById("num2").value)
        
        #Realiza a multiplicação
        
        resultado = n1 * n2
        elemento_resultado.innerText = str(resultado)

    except ValueError:
        elemento_resultado.innerText = "Erro: Digite números válidos"

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
