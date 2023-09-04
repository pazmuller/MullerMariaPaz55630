from django.http import HttpResponse
from django.template import loader

def saludo(request):
	return HttpResponse('Hola Django - Coder')

def segunda_vista(request):
	return HttpResponse('<br><br>Ya entendimos esto - es muy simple')

import datetime
from django.http import HttpResponse

def diaDeHoy(request):
	dia = datetime.datetime.now()
	documentoDeTexto = f"Hoy es dia: <br> {dia}"

	return HttpResponse(documentoDeTexto) 

from django.template import Template, Context 

def probandoTemplate(self):
	nom = "Nicolas"
	ap = "Perez"
	diccionario = {"nombre":nom, "apellido":ap}
	#miHtml = open(r"C:\Users\mpazm\OneDrive\Documentos\proyectodos\Proyecto1\Proyecto1\plantillas\template1.html")
	#plantilla = Template(miHtml.read()) 
	#miHtml.close()
	#miContexto = Context(diccionario)
	#documento = plantilla.render(miContexto)
	plantilla = loader.get_template('template1.html')
	documento = plantilla.render(diccionario)
	return HttpResponse(documento)


