from fastapi import FastAPI, Form, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
import os 
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()

# Enable CORS for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# WhatsApp API configuration
api_key = os.getenv('API_KEY')
url = 'https://app.rapiwa.com/api/send-message'
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/send-message/")
async def send_message(
    phoneNumbers: str = Form(...),
    messageDescription: str = Form(...)
):
    phone_list = [num.strip() for num in phoneNumbers.split(",")]
    results = []

    for number in phone_list:
        payload = {
            'number': number,
            "message_type": "text",
            'message': messageDescription
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            results.append({
                "number": number,
                "status": "success",
                "response": response.json()
            })
        else:
            results.append({
                "number": number,
                "status": "failed",
                "error": response.text
            })

    return {"results": results}

