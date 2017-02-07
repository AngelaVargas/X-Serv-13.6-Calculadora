
#! /usr/bin/python3

#13.6. Calculadora

#Ángela Vargas Alba

import sys

try:
	numb_1 = float(sys.argv[2]) 
	numb_2 = float(sys.argv[3])

	function = sys.argv[1]

except ValueError:

	print ("El tipo de argumento no es correcto")
	sys.exit()

except IndexError:
	
	print ("El número de argumentos no es correcto")
	sys.exit()

if function == 'suma':

	print("La suma es:" , numb_1 + numb_2)

elif function == 'resta':

	print("La resta es:" , numb_1 - numb_2)

elif function == 'division':
	
	try:
		print("La división es:" , numb_1 / numb_2)
	except ZeroDivisionError:
		print("No es posible dividir entre 0")

elif function == 'multiplicacion':

	print("La multiplicación es:" , numb_1 * numb_2)
	

sys.exit()
