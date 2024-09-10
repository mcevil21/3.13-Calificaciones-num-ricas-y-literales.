from Calificaciones import EvaluadorCalificacion
if __name__ == "__main__":
        calificacion = float(input('Introduce la calificación: '))
        evaluador = EvaluadorCalificacion(calificacion)
        evaluador.mostrar_categoria()