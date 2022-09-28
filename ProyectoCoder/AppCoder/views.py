from django.shortcuts import render


def mostrar_inicio(request):
	return render(request, "AppCoder/inicio.html")

