from django.shortcuts import render, get_object_or_404
from usuarios import models
import os

# Create your views here.
def perfil(request,id):
	perfil = get_object_or_404(models.Perfil,id=id)

	return render(
		request,
		'usuarios/perfil.html',
		{'perfil':perfil}
		)

def perfil_list(request):
	perfis = models.Perfil.objects.all()

	return render(
		request,
		os.path.join('usuarios','perfil_list.html'),
		{'perfis':perfis}

	)

