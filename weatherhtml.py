# -*- coding: utf-8 -*-
import requests
import json
from jinja2 import Template
import webbrowser

f = open('plantilla.html','r')

html = ' '

for linea in f:
	html += linea

plantilla = Template(html)

def direccionviento(direccion):
	"""Funcion que calcula la direccion del
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
		
ciudades = ["Almeria","Cadiz","Cordoba","Granada","Huelva","Jaen","Malaga","Sevilla","Dos Hermanas"]
tempe_min = []
tempe_max = []
viento_vel = []
viento_direc = []

for i in xrange(0,8):
	respuesta = requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':'%s,spain' % ciudades[i]})
	dicc = json.loads(respuesta.text)

	tempemin = round(dicc["main"]["temp_min"] - 273,1)
	tempemax = round(dicc["main"]["temp_max"] - 273,1)
	viento = round(dicc["wind"]["speed"] * 1.61,1)
	direccion = dicc["wind"]["deg"]
	i + 1

	tempe_min.append(tempemin)
	tempe_max.append(tempemax)
	viento_vel.append(viento)
	viento_direc.append(direccionviento(direccion))

tiempo = plantilla.render(ciudad=ciudades,temp_max=tempemax,temp_min=tempemin,speed=viento,direccion=direccionviento(direccion))
fichero = open('tiempo.html','w')
fichero.write(tiempo)
fichero.close()
webbrowser.open("tiempo.html")

