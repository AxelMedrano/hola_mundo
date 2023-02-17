print("\n")
print("*")
print("*¿Cuál es tu ISR?")
print("*")

# Con "SB" no estamos refiriendo como se puede observar al Sueldo bruto de la persona.
SB = float(input("Sueldo bruto: "))

# De igual forma con "ND" nos estamos refiriendo al número de dependientes con los cuales restaremos $2000 por cada uno más adelante.
ND = float(input("Número de dependientes: "))

# De acuerdo a las reglas establecidas primero estamos quitando las deducciones antes de sacar el impuesto que es de un 20% por lo que tras quitarle las deducciones lo multiplicamos por 0.2
ISR = (SB - 10000 - (ND * 2000)) * 0.2

print("De acuerdo a nuestro algoritmo, tu pago debe de ser de:", ISR, "\n\n")

print("El nombre de la persona encargada de realizar este algoritmo es Axel André Medrano Cano")
print("La matrícula de la persona encargada de realizar este algoritmo es 2223028520")
print(jaja)
