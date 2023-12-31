from django.urls import path
from AppCoder import views
from django.contrib import admin
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('padre', views.padre),
    path('cursos', views.cursos, name="Cursos"),
    path('entregables', views.entregables, name="Entregables"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('', views.home, name="Home"), 
    path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    path('admin/', admin.site.urls), 
    path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
    path('busquedaCamada', views.busquedaCamada, name="BusquedaCamada"),
    path('buscar/', views.buscar),
    path('leerProfesores', views.leerProfesores, name = "LeerProfesores"),
    path('eliminarProfesor/<profesor_nombre>/', views.eliminarProfesor, name="EliminarProfesor"),
    path('editarProfesor/<profesor_nombre>/', views.editarProfesor, name="EditarProfesor"),
    path('curso/list', views.CursoList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.CursoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.CursoDelete.as_view(), name='Delete'),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
     path('acercaDeMi/', views.acercaDeMi, name='acercaDeMi'),
]
