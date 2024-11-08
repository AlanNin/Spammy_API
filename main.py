from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import joblib
import os


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

html = f"""
<!DOCTYPE html>
<html>
    <head>
        <title>Spammy API</title>
        <link rel="icon" href="/static/favicon.ico" type="image/x-icon" />
    </head>
    <body>
        <div class="bg-gray-200 p-4 rounded-lg shadow-lg">
            <h1>Hello from Spammy API</h1>
            <ul>
                <li><a href="/docs">/docs</a></li>
                <li><a href="/redoc">/redoc</a></li>
            </ul>
        </div>
    </body>
</html>
"""

@app.get("/")
async def read_root():
    return {"message": "API de Clasificación de Spam en funcionamiento"}

# Cargar el modelo y el vectorizador
model_path = os.path.join(os.getcwd(), 'model', 'Modelo_Clasificacion_Spam.pkl')
vectorizer_path = os.path.join(os.getcwd(), 'model', 'CountVectorizer_Spam.pkl')
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

@app.get("/health")
async def health_check():
    return {"status": "ok"}
