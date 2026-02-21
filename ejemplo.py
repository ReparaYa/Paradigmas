
# Calculadora de Nota Definitiva
print("Calculadora de Nota Definitiva");

# Solicitar al usuario que ingrese las notas del primer corte
print("Digite las notas del primer corte:");

# Solicitar al usuario que ingrese la primer nota
nota1 = float(input("Nota 1: "));

# Solicitar al usuario que ingrese la segunda nota
nota2 = float(input("Nota 2: "));

# Solicitar al usuario que ingrese la tercer nota
nota3 = float(input("Nota 3: "));

# Solicitar al usuario que ingrese la nota del parcial
Parcial = float(input("Nota del Parcial: "));

# Función para calcular la nota definitiva
def calcular_definitiva(nota1, nota2, nota3, Parcial):

    # Calcular la nota definitiva segun el porcentaje de cada nota en la nota definitiva
    definitiva = float(nota1 * 0.2) + float(nota2 * 0.2) + float(nota3 * 0.2) + float  (Parcial * 0.4)

    # Devolver la nota definitiva
    return definitiva

# Imprimir la nota definitiva
print("La nota definitiva es:", calcular_definitiva(nota1, nota2, nota3, Parcial));

# Verificar si el estudiante ha aprobado o no el curso
if calcular_definitiva(nota1, nota2, nota3, Parcial) >= 3.0:
    print("¡Felicidades! Has aprobado el curso.")
else:    print("Lo siento, no has aprobado el curso. ¡Sigue esforzándote!")
