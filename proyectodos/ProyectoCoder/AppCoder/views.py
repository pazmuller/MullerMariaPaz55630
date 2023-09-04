from django.shortcuts import render

# Create your views here.
from AppCoder.models import Curso, Profesor, Entregable, Estudiante, Avatar
from django.http import HttpResponse
from AppCoder.forms import CursoFormulario, ProfesorFormulario, Entregables, Estudiantes, UserRegisterForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate


def curso(request):
    curso = Curso(nombre="Desarrollo Web", camada="19881")
    curso.save()
    documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"

    return HttpResponse(documentoDeTexto)

def home(request):
    return render(request, "AppCoder/home.html")

def padre(request):
    return render(request, "AppCoder/padre.html")

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def cursos(request):
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return render(request, "AppCoder/home.html")
    else:
        miFormulario = CursoFormulario()
    return render(request, "AppCoder/cursos.html", {"miFormulario": miFormulario})

def cursoFormulario(request):
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return render(request, "AppCoder/home.html")
    else:
        miFormulario = CursoFormulario()
    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario": miFormulario})

def profesorFormulario(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion'])
            profesor.save()
            return render(request, "AppCoder/home.html")
    else:
        miFormulario= ProfesorFormulario()

    return render(request, "AppCoder/profesorFormulario.html", {"miFormulario":miFormulario})

def busquedaCamada(request):
    return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):
    camada = request.GET.get('camada', '')  # Obtén el valor del parámetro 'camada' o establece una cadena vacía por defecto

    if camada:
        cursos = Curso.objects.filter(camada__icontains=camada)  # Corrige 'camada_icontains' a 'camada__icontains'
        return render(request, "AppCoder/resultadosPorBusqueda.html", {"cursos": cursos, "camada": camada})
    else:
        respuesta = "No enviaste datos"
        return render(request, "AppCoder/home.html", {"respuesta": respuesta})
    
def entregables(request):
    if request.method == 'POST':
        miFormulario = Entregables(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            entregable = Entregable(legajo=informacion['legajo'], materia=informacion['materia'], comision=informacion['comision'], calificacion=informacion['calificacion'])
            entregable.save()
            return render(request, "AppCoder/home.html")
    else:
        miFormulario= Entregables()

    return render(request, "AppCoder/entregables.html", {"miFormulario":miFormulario})

def estudiantes(request):
    if request.method == 'POST':
        miFormulario = Estudiantes(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            estudiante = Estudiante(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            estudiante.save()
            return render(request, "AppCoder/home.html")
    else:
        miFormulario= Estudiantes()

    return render(request, "AppCoder/estudiantes.html", {"miFormulario":miFormulario})

def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email} - Profesión {self.profesion}"

def leerProfesores(request):
    print("La vista leerProfesores se está ejecutando")  # Agrega este mensaje de depuración
    profesores = Profesor.objects.all()
    contexto = {"profesores": profesores}
    return render(request, "AppCoder/leerProfesores.html", contexto)

def eliminarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()
    
    # vuelvo al menú
    profesores = Profesor.objects.all() # trae todos los profesores
    contexto = {"profesores": profesores}
    
    return render(request, "AppCoder/leerProfesores.html", contexto)

def editarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)

    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']
            profesor.save()

            return render(request, "AppCoder/home.html")
    else:
        miFormulario = ProfesorFormulario(initial={'nombre': profesor.nombre, 'apellido': profesor.apellido, 'email': profesor.email, 'profesion': profesor.profesion})

    return render(request, "AppCoder/editarProfesor.html", {"miFormulario": miFormulario, "profesor_nombre": profesor_nombre})

class CursoList(ListView):
    model = Curso
    template_name ="AppCoder/cursos_list.html"

class CursoDetalle(DetailView):
    model = Curso
    template_name = "AppCoder/curso_detalle.html"

class CursoCreacion(CreateView):
    model = Curso
    success_url = "/AppCoder/curso/list"
    fields = ['nombre', 'camada']

class CursoUpdate(UpdateView):
    model = Curso
    success_url = "/AppCoder/curso/list"
    fields = ['nombre', 'camada']

class CursoDelete(DeleteView):
    model = Curso
    success_url = "/AppCoder/curso/list"

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                return render(request, "AppCoder/home.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppCoder/home.html", {"mensaje":"Error, datos incorrectos"})
        else:
                return render(request, "AppCoder/home.html", {"mensaje":"Error, formulario erroneo"})
    
    form = AuthenticationForm()
    return render(request, "AppCoder/login.html", {'form':form})

def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "AppCoder/home.html", {"mensaje":"Usuario Creado :)"})
    else:
        #form = UserCreationForm()
        form = UserRegisterForm()

    return render(request, "AppCoder/registro.html", {"form":form})

from django.shortcuts import render

def acercaDeMi(request):
    
    mi_info = {
        'nombre': 'María de la Paz Muller',
        'edad': 25,
        'ocupacion': 'Estudiante de desarrollo de Software',
        'descripcion': 'Soy una apasionada estudiante de desarrollo de software con experiencia en Python',
        
    }
    return render(request, 'AppCoder/acercaDeMi.html', {'mi_info': mi_info})
