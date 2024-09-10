class EvaluadorCalificacion:
    def __init__(self, calificacion):
        self.calificacion = calificacion
    def obtener_categoria(self):
        if self.calificacion > 9.0:
            return "La calificación es A."
        elif self.calificacion > 8.0:
            return "La calificación es B."
        elif self.calificacion >= 7.5:
            return "La calificación es C."
        else:
            return "La calificación es R."
    def mostrar_categoria(self):
        print(self.obtener_categoria())
def main():
    try:
        calificacion = float(input('Introduce la calificación: '))
        evaluador = EvaluadorCalificacion(calificacion)
        evaluador.mostrar_categoria()
    except ValueError:
        print("Por favor, introduce un número válido.")
if __name__ == "__main__":
    main()