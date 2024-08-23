from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("""

    <nav>
        <a href="http://127.0.0.1:8000/">Inicio</a>
        <a href="http://127.0.0.1:8000/about">Acerca de</a>
        <a href="http://127.0.0.1:8000/contact">Contacto</a>
    </nav>
    
    <h1>Lorem Ipsum</h1>
    <h4>
        "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, 
        consectetur, adipisci velit..."
    </h4>
    <h5>
        "No hay nadie que ame el dolor mismo, que lo busque, 
        lo encuentre y lo quiera, simplemente porque es el dolor."
    </h5>
    <section>
        <img src="https://hospitalmetropolitano.minsal.cl/wp-content/uploads/2020/07/logo-h_metropolitano180.png">
    </section>
    
""")


def about(request):
    return HttpResponse(
"""
    <nav>
        <a href="http://127.0.0.1:8000/">Inicio</a>
        <a href="http://127.0.0.1:8000/about">Acerca de</a>
        <a href="http://127.0.0.1:8000/contact">Contacto</a>
    </nav>
    <h1>Lorem Ipsum</h1>
    <section>
        <img src="https://hospitalmetropolitano.minsal.cl/wp-content/uploads/2020/07/logo-h_metropolitano180.png">
    </section>
    <section>
        <h4>
            "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, 
            consectetur, adipisci velit..."
        </h4>
        <h5>
            "No hay nadie que ame el dolor mismo, que lo busque, 
            lo encuentre y lo quiera, simplemente porque es el dolor."
        </h5>
    </section>
    <section>
        <h5>¿Qué es Lorem Ipsum?</h5>
        <p>Lorem Ipsum es simplemente el texto de relleno 
            de las imprentas y archivos de texto. 
            Lorem Ipsum ha sido el texto de relleno estándar 
            de las industrias desde el año 1500, cuando 
            un impresor (N. del T. persona que se dedica a 
            la imprenta) desconocido usó una galería de textos 
            y los mezcló de tal manera que logró hacer un 
            libro de textos especimen. No sólo sobrevivió 500 años, 
            sino que tambien ingresó como texto de relleno en 
            documentos electrónicos, quedando esencialmente igual 
            al original. Fue popularizado en los 60s con la creación \
            de las hojas "Letraset", las cuales contenian pasajes de 
            Lorem Ipsum, y más recientemente con software de 
            autoedición, como por ejemplo Aldus PageMaker, 
            el cual incluye versiones de Lorem Ipsum.</p>
    </section>

""")


def contact(response):
    return HttpResponse(
"""
    <nav>
        <a href="http://127.0.0.1:8000/">Inicio</a>
        <a href="http://127.0.0.1:8000/about">Acerca de</a>
        <a href="http://127.0.0.1:8000/contact">Contacto</a>
    </nav>
    <section>
        <img src="https://hospitalmetropolitano.minsal.cl/wp-content/uploads/2020/07/logo-h_metropolitano180.png">
    </section>
    <h2>Formulario de Contacto</h2>
    <form action="/submit_formulario" method="post">
        <label for="nombre">Nombre:</label><br>
        <input type="text" id="nombre" name="nombre" required><br>
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br>
        <label for="mensaje">Mensaje:</label><br>
        <textarea id="mensaje" name="mensaje" rows="4" required></textarea><br>
        <input type="submit" value="Enviar">
    </form>

""")