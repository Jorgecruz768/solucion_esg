import cmath


class EcuacionSegundoGrado:
    def __init__(self):
        self._a = 0.0
        self._b = 0.0
        self._c = 0.0

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("El valor de 'a' debe ser numérico.")
        self._a = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("El valor de 'b' debe ser numérico.")
        self._b = value

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("El valor de 'c' debe ser numérico.")
        self._c = value

    def solucionESG(self):
        if self._a == 0:
            raise ZeroDivisionError("El coeficiente 'a' no puede ser cero.")

        discriminante = (self._b ** 2) - (4 * self._a * self._c)
        raiz1 = (-self._b + cmath.sqrt(discriminante)) / (2 * self._a)
        raiz2 = (-self._b - cmath.sqrt(discriminante)) / (2 * self._a)
        return raiz1, raiz2
