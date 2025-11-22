from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'message':'Bienvenidos al Gestor de Tareas'}
    return render(request,'index.html',context)