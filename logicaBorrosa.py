#Archivo: logicaBorrosa.py
#
#Funciones de Membresia
#
def fxBool(x,y):
	"""
		Funcion de membresia boleana.
		Solo retorna dos valores 1,0
	"""
	if x<=y:
		return 0
	else:
		return 1

def fxBoolInversa(x,y):
	"""
		Funcion inverda de la funcion de membresia boleana.
		Solo retorna dos valores 1,0
	"""
	return 1-fxBool(x,y)

def fxGrado(x,y,z):
	"""
		Funcion de membresia de grado.
	"""
	if x<=y:
		return 0.0
	elif x>y and x<z:
		return (x/(z-y))-(y/(z-y))
	else:
		return 1.0

def fxGradoInversa(x,y,z):
	"""
		Funcion de membresia de grado.
	"""
	if x<=y:
		return 1.0
	elif x>y and x<z:
		return -(x/(z-y))+(z/(z-y))
	else:
		return 0.0

def fxTriangulo(x,x0,x1,x2):
	"""
		funcion de membresia Triangulo
	"""
	if x<=x0:
		return 0.0
	elif x>x0 and x<=x1:
		return (x/(x1-x0))-(x0/(x1-x0))
	elif x>x1 and x<=x2:
		return -(x/(x2-x1))+(x2/(x2-x1))
	else:
		return 0.0

def fxTrapezoide(x,x0,x1,x2,x3):
	"""
		funcion de membresia Trapezoide
	"""
	if x<=x0:
		return 0.0
	elif x>x0 and x<=x1:
		return (x/(x1-x0))-(x0/(x1-x0))
	elif x>x1 and x<=x2:
		return 1.0
	elif x>x2 and x<=x3:
		return -(x/(x3-x2))+(x3/(x3-x2))
	else:
		return 0.0

#
# Operadores Borroso
#
def OperadorAnd(x,y):
	return min(x,y)
def OperadorOR(x,y):
	return max(x,y)
def OperadorNOT(x):
	return 1-x
