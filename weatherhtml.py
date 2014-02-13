# -*- coding: utf-8 -*-
import requests
import json
from jinja2 import Template

f = open('plantilla.html','r')

html = ''

for linea in f:
	hmtl += linea

plantilla = Template('plantilla.html')

plantilla.render(temp_min=tempeminreal,temp_max=tempemaxreal,
def direccionviento(direccion):
	"""Función que calcula la dirección del
	viento dada por grados"""
	for grado in str(direccion):
		if direccion >= 337.5 and direccion < 22.5:
			return "N"
		elif direccion >= 22.5 and direccion < 67.5:
			return "NE"
		elif direccion >= 67.5 and direccion < 112.5:
			return "E"
		elif direccion >= 112.5 and direccion < 157.5:
			return "SE"
		elif direccion >= 157.5 and direccion < 202.5:
			return "S"
		elif direccion >= 202.5 and direccion < 247.5:
			return "SO"
		elif direccion >= 247.5 and direccion < 292.5:
			return "O"
		elif direccion >= 292.5 and direccion < 337.5:
			return "NO"
		
ciudades = ["Almería","Cádiz","Córdoba","Granada","Huelva","Jaén","Málaga","Sevilla","Dos Hermanas"]

respuesta = requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':'%s,spain' % ciudades[1]})

dicc = json.loads(respuesta.text)

tempemin = dicc["main"]["temp_min"]
tempemax = dicc["main"]["temp_max"]
viento = dicc["wind"]["speed"]
direccion = dicc["wind"]["deg"]

tempminreal = round(tempemin - 273,1)
tempmaxreal = round(tempemax - 273,1)
vientoreal = round(viento * 1.61,1)

print "La temperatura mínima actual de %s es de %s grados centígrados, la máxima es de %s, y el viento tiene una velocidad de %s km/h dirección %s" % (ciudades[1],tempminreal,tempmaxreal,vientoreal,direccionviento(direccion))

# print respuesta.text
