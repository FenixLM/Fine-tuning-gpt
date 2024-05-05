
## FINE TUNING CON PYTHON

El Fine-tuning se refiere al proceso de realizar pequeños ajustes o refinamientos a algo con el fin de mejorar su rendimiento o efectividad. En diversos contextos, el fine-tuning puede implicar ajustar parámetros, configuraciones o ajustes para optimizar el resultado o lograr un resultado deseado.

#### APLICADO A CHATGPT:
Fine-tuning mejora la respuesta desea, al ser entrenado con ejemplos, lo cual permite mejores resultados

#### ¿COMO FUNCIONA?
Existen diferentes casos de uso:
-	Atención a la cliente personalizada.
-	Asistencia en la toma de decisiones.
-	Automatización de tareas repetitivas

En este caso lo utilizaremos para un asistente que nos dé una respuesta en formato JSON, siguiendo ciertos parámetros.

#### REQUERIMIENTOS:
-	Tener una apikey de OpenIa
-	Editor de código como visual code
-	Tener Python instalado.

#### VAMOS AL CODIGO:
Aplicamos estos comandos en la terminal, ruta donde esta nuestro proyecto.

**1. crearmos una carpteta venv:**:
```bash
  py -3 -m venv venv
```

**2. activamos los ambientes virtuales con:**:
```bash
  . venv/scripts/activate
```

**3. intalamos las librerias requeridas:**:
```bash
  pip install -r requirements.txt
```


**EXTRA: si no quieres intalar las librerias requeridas puedes solo intalar flask y las librerías openia y langChain:**:
```bash
  pip install Flask openia langchain
```




#### LEVANTAR EL PROYECTO:

Para levantar el proyecto necesitamos estas variables de entorno, en este caso estoy usando la terminal de git en Windows usamos export

Nota: si se cierra vsCode, tendremos que activar el ambiente virtual, descrito en el paso anterior: venv/scripts/actívate

Para Windows se cambia export por 
```shell
  $env:FLASK_APP = "index.py"
  $env: OPENAI_API_KEY=sk-###########
  flask run
```


Con terminal de GIT
```shell
  export FLASK_APP=index.py 
  export OPENAI_API_KEY=sk-###########
  flask run
```


## API Referencias

#### Crear formato 

Nos creara el formato que nos pide chatgpt tomando como fuente nuestro JSON.

```http
  GET /format-file
```

#### Cargar data

Nos retornara el ID de nuestro dataset, aquí es importante tener al menos 10 ejemplos a enviar y esperar el id que nos retorne

```http
  GET /charge-data
```

#### Crear trabajo

Aquí utilizamos el id que nos retorno el end  point pasado, aquí nos retornara una serie de datos sobre la afinación de nuestro modelo y tendremos que esperar a que los servidores de OpenIa nos dé el nombre de nuestro nuevo modelo.

```http
  GET /create-job
```

#### Probar modelo

Aquí probamos nuestro nuevo modelo

```http
  GET /test-job
```
