# SAMS API

## sentiment analysis for speeches from the monarchs in Spain.


RECAP 

Elegir estructura base datos (SQL/Mongo. SQL puede ser más útil al ser relacional y evitar la duplicidad de datos)
Cargar la BBDD a mano
Hacer un endpoint de GET (el resto vienen solos)
Hacer más endpoints
Hacer endpoints de POST
Borrar la BBDD y utilizar esos endpoints de POST para añadirla a través de la API
Hacer sentiment analysis & visualización"

### @GET

#### GET examples:

"""
urlbase = "http://localhost:5000/"
- resp_base = requests.get(urlbase)
- resp_base.content

urlspeeches = "http://localhost:5000/speeches"

urlyear = "http://localhost:5000/speeches/<year>"
- year = 2012
- end = f"speeches/{year}"
- endpoint=urlbase+end
- resp_year = requests.get(endpoint).json()
- resp_year

"""


### @POST

### POST examples:

"""
urladd = "http://localhost:5000/speeches/new"
show = requests.post(urladd, data=juanq_dic)
show.content
"""
