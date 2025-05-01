from src.logica.ecuacion_segundo_grado import EcuacionSegundoGrado

if __name__ == "__main__":
    ecuacionSegundoGrado = EcuacionSegundoGrado()

    print("Solución: ax^2 + bx + c")
    try:
        ecuacionSegundoGrado.a = float(input("Parámetro a: "))
        ecuacionSegundoGrado.b = float(input("Parámetro b: "))
        ecuacionSegundoGrado.c = float(input("Parámetro c: "))

        raiz1, raiz2 = ecuacionSegundoGrado.solucionESG()
        print(f"{ecuacionSegundoGrado.a}x^2 + "
              f"{ecuacionSegundoGrado.b}x + "
              f"{ecuacionSegundoGrado.c} --> "
              f"raiz1 = {raiz1}, raiz2 = {raiz2}")
    except ValueError:
        print("Error: Debes ingresar valores numéricos.")
