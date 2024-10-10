from time import time
from fastapi import FastAPI, __version__
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import joblib
import os


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

html = f"""
<!DOCTYPE html>
<html>
    <head>
        <title>FastAPI on Vercel</title>
        <link rel="icon" href="/static/favicon.ico" type="image/x-icon" />
    </head>
    <body>
        <div class="bg-gray-200 p-4 rounded-lg shadow-lg">
            <h1>Hello from FastAPI@{__version__}</h1>
            <ul>
                <li><a href="/docs">/docs</a></li>
                <li><a href="/redoc">/redoc</a></li>
            </ul>
            <p>Powered by <a href="https://vercel.com" target="_blank">Vercel</a></p>
        </div>
    </body>
</html>
"""

# Cargar el modelo y el vectorizador
model_path = os.path.join(os.path.dirname(__file__), 'model', 'Modelo_Clasificacion_Spam.pkl')
vectorizer_path = os.path.join(os.path.dirname(__file__), 'model', 'CountVectorizer_Spam.pkl')
model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

# Define un modelo de datos para la entrada
class Email(BaseModel):
    email: str

# Endpoint para clasificar el correo
@app.post("/classify")
async def classify_email(email: Email):
    # Procesar y predecir
    correo_vectorizado = vectorizer.transform([email.email])
    prediccion = model.predict(correo_vectorizado)
    probabilidad = model.predict_proba(correo_vectorizado)

    # Resultado de la predicción
    resultado = {
        "resultado": "Spam" if prediccion[0] == 1 else "No Spam",
        "probabilidad_spam": probabilidad[0][1],
        "probabilidad_no_spam": probabilidad[0][0]
    }

    return resultado

# Ruta raíz para verificar que el servidor está en funcionamiento
@app.get("/")
async def read_root():
    return {"message": "API de Clasificación de Spam en funcionamiento"}