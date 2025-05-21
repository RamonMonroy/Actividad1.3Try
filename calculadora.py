class Calculadora:
    def __init__(self):
        self.num1 = None
        self.num2 = None
        self.operacion = None

    def pedir_datos(self):
        while True:
            try:
                self.num1 = float(input("Ingresa el primer número: "))
                break
            except ValueError:
                print("⚠️ Entrada inválida. Por favor, ingresa un número válido.")

        while True:
            self.operacion = input("Ingresa la operación (+, -, *, /): ")
            if self.operacion in ('+', '-', '*', '/'):
                break
            else:
                print("⚠️ Operación inválida. Intenta con +, -, * o /.")

        while True:
            try:
                self.num2 = float(input("Ingresa el segundo número: "))
                if self.operacion == '/' and self.num2 == 0:
                    raise ZeroDivisionError
                break
            except ValueError:
                print("⚠️ Entrada inválida. Por favor, ingresa un número válido.")
            except ZeroDivisionError:
                print("⚠️ No se puede dividir entre cero. Ingresa otro número.")

    def calcular(self):
        if self.operacion == '+':
            return self.num1 + self.num2
        elif self.operacion == '-':
            return self.num1 - self.num2
        elif self.operacion == '*':
            return self.num1 * self.num2
        elif self.operacion == '/':
            return self.num1 / self.num2

    def mostrar_resultado(self):
        resultado = self.calcular()
        print(f"✅ Resultado: {self.num1} {self.operacion} {self.num2} = {resultado}")


if __name__ == "__main__":
    while True:
        calc = Calculadora()
        calc.pedir_datos()
        calc.mostrar_resultado()

        continuar = input("¿Deseas realizar otra operación? (s/n): ").lower()
        if continuar != 's':
            print("👋 ¡Gracias por usar la calculadora!")
            break