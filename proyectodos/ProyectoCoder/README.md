Este es un proyecto de una web Intermedia desarrollado con Django. Permite a los usuarios agregar cursos, estudiantes, profesores y entregables, así como realizar búsquedas en la base de datos.

Video explicativo del sitio web: https://clipchamp.com/watch/mNxvexslW5J

Instalación
1. Clona este repositorio en tu máquina local utilizando git clone.

2. Crea un entorno virtual para el proyecto: python -m venv venv

3. Activa el entorno virtual: En Windows: venv\Scripts\activate En macOS y Linux: source venv/bin/activate

4. Instale las dependencias del proyecto: pip install -r requisitos.txt

5. Aplicación de las migraciones: python enable.py migrar

6. Crea un superusuario: python enable.py createsuperuser

7. Inicia el servidor de desarrollo: python Manage.py RunServer

8. Abra su navegador y visite http://127.0.0.1:8000/AppCoder/ para acceder a la aplicación.

9. Ingrese a través del botón Iniciar, con el usuario: mp y contraseña: paz1234. Para desloguearse acceda a http://127.0.0.1:8000/AppCoder/logout

Funcionalidades
- Agregar Estudiante: Permite agregar estudiantes a la base de datos con información como nombre, apellido, email y legajo. 
- Agregar Profesor: permite agregar profesores a la base de datos con información como nombre, apellido, email y profesión. 
- Agregar Entregable: permite agregar entregables a la base de datos con información como materia, comision, legajo y calificación. 
- Función buscar: Realiza búsquedas en la base de datos de comisiones según el numero de camada ingresado. 

- Pestaña Administrador: Acceda a la interfaz de administración de Django para gestionar los datos http://127.0.0.1:8000/admin/

Tecnologías Utilizadas
Django: Framework de desarrollo web en Python. HTML/CSS: Para la estructura y el estilo de las páginas.

Autor
María Paz Müller mpazmuller@gmail.com