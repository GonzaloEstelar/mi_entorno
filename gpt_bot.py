import openai
from config import openai_api_key  # Importamos la clave desde config.py

openai.api_key = openai_api_key

print("Importación de OpenAI exitosa.")
print("Clave API configurada.")

try:
    print("Realizando solicitud a OpenAI...")
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt="Dime algo interesante sobre astrología.",
        max_tokens=50
    )
    print("Respuesta de OpenAI:", response['choices'][0]['text'].strip())
except Exception as e:
    print("Error al hacer la solicitud:", str(e))
