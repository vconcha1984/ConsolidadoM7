from django.shortcuts import get_object_or_404, render, redirect
from .models import Laboratorio, DirectorGeneral, Producto
from .forms import LaboratorioForm

# Create your views here.
def index(request):
    laboratorios = Laboratorio.objects.all()
    directores_generales = DirectorGeneral.objects.all()
    productos = Producto.objects.all()
    if 'visitas' not in request.session:
        request.session['visitas'] = 1
    else:
        request.session['visitas'] += 1
    context = {
        'laboratorios': laboratorios,
        'directores_generales': directores_generales,
        'productos': productos,
        'contador_visitas': request.session['visitas'],
    }
    return render(request, 'laboratorio/index.html', context)

def crear(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('laboratorio:index')
    else:
        form = LaboratorioForm()
    return render(request, 'laboratorio/crear.html', {'form':form})

def edit(request, lab_id):
    lab = get_object_or_404(Laboratorio, id=lab_id)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=lab)
        if form.is_valid():
            form.save()
            return redirect('laboratorio:index')
    else:
        form = LaboratorioForm(instance=lab)
    return render(request, 'laboratorio/edit.html', {'form': form, 'lab':lab})


def delete(request, lab_id):
    lab_delete = get_object_or_404(Laboratorio, id=lab_id)
    
    if request.method == 'POST':
        lab_delete.delete()
        return redirect('laboratorio:index')
    
    return render(request, 'laboratorio/delete.html', {'lab_delete': lab_delete})