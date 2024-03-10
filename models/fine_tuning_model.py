import json
from openai import OpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage


class FineTuningModel:

    # iniciamos la clase definiendo nuestro client
    def __init__(self):
        self.client = OpenAI()

    # Este metodo nos sirve para guardar el archivo JSON ya estructurado(como lo pide OPENIA) en nuestro proyecto
    # recibe como primer parametro el conjunto de datos o el array, seguido del nombre del archivo
    def save_to_jsonl(dataset,file_path_name):
        with open(file_path_name, 'w', encoding='utf-8') as file:
            for ejemplo in dataset:
                print(ejemplo)
                json_line = json.dumps(ejemplo, ensure_ascii=False)
                file.write(json_line + '\n')



    # aqui creamos nuestro archivo el cual servira luego para subir a los servidores de OPENIA 
    # y empiece con los trabajos de fineTuning
    def format_file():
        try:
            with open('files/fine_tuning_example.json', 'r', encoding='utf-8') as f:
                # Carga el contenido del archivo en un objeto Python
                data = json.load(f)
                #role_system es el mensaje o promp inicial, que estara en cada uno de nuestros ejemplos
                role_system="""Eres YIR, un asistente virtual diseñado para facilitar la planificación de viajes. Tu tarea es generar un itinerario de varios días para los viajeros. Cada día debe incluir la siguiente información:
                        -Lugar: Indica el nombre del lugar o la atracción turística que se visitará.
                        -Descripción: Proporciona una breve descripción del lugar, destacando sus principales características o atractivos.
                        -Día: Indica el día del itinerario.
                        -Horas: Indica el rango de horas en el que se realizará la actividad.
                        -Duración: Especifica el tiempo estimado que se dedicará a visitar ese lugar."""
                
                muestra_final=[]

            # Este for esta adapatado para esta estructura de JSON del archivo, si tienes algun ejemplo en JSON, adaptalo a tu archivo

            for itinerario in data["itinerarios"]:
                user = itinerario["user"]
                assistant = itinerario["assistant"]

                messagess = []

                system_message = {
                        "role": "system",
                        "content": role_system
                    }
                
                messagess.append(system_message)

                if user.get("lugar") is not None:
                    user_message = {
                        "role": "user",
                        "content": json.dumps(user)
                    }
                    messagess.append(user_message)
                
                if assistant.get("dias") is not None:
                    assistant_message = {
                        "role": "assistant",
                        "content": json.dumps(assistant)
                    }
                    messagess.append(assistant_message)
                
                muestra_message = {
                    "messages": messagess
                }

                muestra_final.append(muestra_message)
            

            FineTuningModel.save_to_jsonl(muestra_final, 'fine_tuning_train_full.jsonl')
            return muestra_final

        except FileNotFoundError:
            print("El archivo no fue encontrado.")
        except PermissionError:
            print("No tienes permiso para acceder al archivo.")
        except Exception as e:
            print("Ocurrió un error:", e)


    # IMPORTANTE: se necesita minimo 10 ejemplos
    # Aqui enviamos nuestra data a los servidores de OpenIA
    # Nos retonara un ID que utilizaremos en el siguiente end point
    # Tendra el siguiwente formato: file-############
            
    def charge_data(selft):
        train_full_response_file = selft.client.files.create(
            file=open('fine_tuning_train_full.jsonl','rb'),
            purpose='fine-tune'
        )

        return train_full_response_file.id
    

    # IMPORTANTE: Al enviarse y estrar todo OK, nos llegara un correo con el nombre del modelo que utilizaremos para nuestras consultas
    # Creamos nuestro modelo con el id que nos dio el endpoint anterior
    # Model: nos apoyaremos en el modelo que queramos trabajar
    # El suffix nos ayudara a mantener un cierto orden en los modelos creados
    # hyperparameters - n_epochs: significa que lo entrenara durante x recorridos que se le dara n_epochs: 4 (4 iteraciones)

    def create_fine_tunig_job(self):
        id_fine_tuning_training = "file-#####"
        response = self.client.fine_tuning.jobs.create(
            training_file= id_fine_tuning_training,
            model="gpt-3.5-turbo",
            suffix='turismo-vprueba',
            hyperparameters={'n_epochs': 4}
        )
        response_message = f'response: {response}'
        print(response_message)
        return response_message


    # IMPORTANTE: Aqui introducimos el nombre de nuestro nuevo modelo
    # Aqui testeamos nuestro fine tuning
    # En el model_name ponemos el nombre del modelo que nos vino en el correo deberia tener ese formato
    def test_fine_tuning():
        
        model_name = "ft:gpt-3.5-turbo-0125:personal:turismo-vprueba:####"
        chat = ChatOpenAI(model=model_name, temperature=0.0)
        role_system="""Eres YIR, un asistente virtual diseñado para facilitar la planificación de viajes. Tu tarea es generar un itinerario de varios días para los viajeros. Cada día debe incluir la siguiente información:
                        -Lugar: Indica el nombre del lugar o la atracción turística que se visitará.
                        -Descripción: Proporciona una breve descripción del lugar, destacando sus principales características o atractivos.
                        -Día: Indica el día del itinerario.
                        -Horas: Indica el rango de horas en el que se realizará la actividad.
                        -Duración: Especifica el tiempo estimado que se dedicará a visitar ese lugar."""

        messages = [
            SystemMessage(content=role_system),
            HumanMessage(content="{\"lugar\": \"Puno, Per\\u00fa\", \"dias\": 3}")
        ]

        response = chat(messages)

        print(response.content)
        return response.content
        



    


   
    


    