def calcular_suma( txt_num1, txt_num2, txt_resultado):
    try:
        num1 = float(txt_num1.value.strip())
        num2 = float(txt_num2.value.strip())
        resultado = num1 + num2
        txt_resultado.value = f"Resultado: {resultado}"
    except ValueError:
        txt_resultado.value = "Error: Ingresa valores correctos"
        