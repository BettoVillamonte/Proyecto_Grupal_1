valor_1 = int(input("Introduzca el primer valor: "))
valor_2 = int(input("Introduzca el segundo valor: "))
print("Elegir la operacion que requiere")
print("+ = suma")
print("- = resta")
print("/ = division")
print("* = multiplicacion")

op = input("Elije tu operacion: ")
if op == "+":   
  print("La respuesta es: ", valor_1 + valor_2)
elif op == "-":
  print("La respuesta es: ", valor_1 - valor_2)
elif op == "/":
  print("La respuesta es :", valor_1 / valor_2)
elif op == "*":
  print("La respuesta es: ", valor_1 * valor_2)
else:
  print("Operador invalido. Por favor ingrese +, -, / o *.")