#!/usr/bin/env python
#Archivo: ventiladorBorroso.py

import logicaBorrosa
import random

def borroso(objY,posY):
	distancia = objY-posY

	centrado	=logicaBorrosa.fxTriangulo   (distancia,-10.0,0.0,10.0)
	cercaA		=logicaBorrosa.fxTrapezoide  (distancia,10.0,80.0,120.0,180.0)
	normalA     =logicaBorrosa.fxTrapezoide  (distancia,120.0,160.0,240.0,280.0)
	lejosA		=logicaBorrosa.fxGrado	     (distancia,240.0,300.0)
	cercaB		=logicaBorrosa.fxTrapezoide  (distancia,-180.0,-120.0,-80.0,-10.0)
	normalB		=logicaBorrosa.fxTrapezoide  (distancia,-280.0,-240.0,-160.0,-120.0)
	lejosB		=logicaBorrosa.fxGradoInversa(distancia,-300,-240)

	tmp =(centrado*9.8+cercaA*4.0+normalA*2.0+lejosA*1.0+cercaB*14.0+normalB*15.5+lejosB*18.0)
	div = (centrado+cercaA+normalA+lejosA+cercaB+normalB+lejosB)
	try:
		tmp /= div
	except:
		pass

	return tmp

gravedad = 9.81

velY = 0.0
posY= random.randrange(150.0,450.0)
ventilador = random.randrange(1.0,120.0)/10.0
objY=300

while True:
	caos = 0.0
	ventilador = borroso(objY,posY) # Llevamos a cabo el calculo borroso
	caos = (random.randrange(-50,50))/10.0
	velY = ((gravedad-ventilador+caos)*0.01)
	posY +=velY
	print posY
