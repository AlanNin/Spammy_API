# Spammy API - Email Spam Detection Service

**Spammy API** is an API built with FastAPI that provides an AI-powered spam detection service for emails. This API uses a pre-trained machine learning model to classify emails as spam or not spam. It is designed to integrate seamlessly with applications like **Spammy**, a web app for email classification, but can be used in any service that needs spam detection capabilities.

The API is deployed on **Render** for high availability and performance.

## Features

### 1. **Email Spam Classification**

- The API accepts email content and classifies it as **Spam** or **Not Spam** using a trained machine learning model.
- Model is serialized using `.pkl` (Pickle) files for efficient loading and inference.

### 2. **Fast and Scalable**

- Built with **FastAPI**, ensuring asynchronous processing for high-speed performance.
- Scalable deployment on **Render**, handling multiple concurrent requests.

### 3. **Model Details**

- Uses a Logistic Regression classifier trained on a large dataset of emails.
- The model is loaded from `.pkl` files stored on the server for quick inference.

### 4. **Secure API**

- Supports HTTPS to ensure secure data transmission between clients and the server.
- CORS configured for safe cross-origin requests.

## Technology Stack

- **API Framework**: FastAPI (Python)
- **Machine Learning**: scikit-learn for model creation and classification
- **Model Files**: Pickle (`.pkl`) files for model persistence
- **Deployment**: Render
- **Data Format**: JSON for API requests and responses

## API Endpoints

### `POST /classify`

This endpoint accepts email content in the request body and returns whether the email is classified as spam or not.

#### Request

- **URL**: `/classify`
- **Method**: POST
- **Content-Type**: `application/json`

#### Request Body Example:

```json
{
  "email": "Congratulations! You have won a free iPhone. Claim your prize now."
}
```

#### Response Example:

```json
{
  "resultado": "Spam",
  "probabilidad_spam": 0.95,
  "probabilidad_no_spam": 0.05
}
```

- **`resultado`**: Indicates if the email is classified as `Spam` or `Not Spam`.
- **`probabilidad_spam`**: The model's probability of the email being spam (between 0 and 1).
- **`probabilidad_no_spam`**: The model's probability of the email being not spam (between 0 and 1).

### `GET /health`

A health check endpoint to verify that the API is running and available.

#### Response Example:

```json
{
  "status": "ok"
}
```

## How to Use the API

### 1. Base URL

The base URL for the API is:

```
https://spammy-api.onrender.com
```

### 2. Example Request

Here’s how to send a request using `curl`:

```bash
curl -X POST "https://spammy-api.onrender.com/classify" \
-H "Content-Type: application/json" \
-d '{"email": "Your email content here."}'
```

Or, using Python’s `requests` library:

```python
import requests

url = "https://spammy-api.onrender.com/classify"
data = {"email": "Your email content here."}

response = requests.post(url, json=data)
print(response.json())
```

## Running Locally

### Prerequisites

- Python 3.8+
- FastAPI and required dependencies
- Pickle (`.pkl`) model files

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/AlanNin/Spammy_API.git
   cd spammy_api
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Place the pre-trained `.pkl` files in the appropriate directory (e.g., `model/`) if not already done.

4. Run the FastAPI application locally:

   ```bash
   uvicorn main:app --reload
   ```

5. The API will be available at `http://127.0.0.1:8000`.

### Testing Locally

You can test the API locally by sending POST requests to `http://127.0.0.1:8000/classify` using the same request format mentioned above.

## Model Details

- **Algorithm**: Logistic Regression classifier trained on a dataset of spam and non-spam emails.
- **Serialized Model**: The model is stored in a `.pkl` file, allowing for quick loading and execution during API requests.

## Deployment

The API is deployed on **Render**, providing a cloud-based solution for hosting FastAPI services. The deployment pipeline is automatically triggered on repository changes, ensuring seamless updates.

For deploying to Render, the following steps were followed:

1. Set up the Render account and connect the repository.
2. Configure the FastAPI service for the Render platform.
3. Upload model files and configure environment variables (if necessary).
4. Deploy the service and verify using health checks.

## Future Improvements

- **Improved Model**: Further optimize the machine learning model with more training data.
- **Batch Processing**: Add support for batch classification of multiple emails in one request.
- **Authentication**: Implement API key-based authentication for more secure usage.

## Contact

For any inquiries, feel free to reach me out at [alanbusinessnin@gmail.com](alanbusinessnin@gmail.com).
