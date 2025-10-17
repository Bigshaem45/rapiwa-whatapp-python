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
    # Collect successful recipients to return to the frontend
    successful_recipients = [] 

    for number in phone_list:
        payload = {
            'number': number,
            "message_type": "text",
            'message': messageDescription
        }
        # Use an async HTTP client (like httpx) in FastAPI for better performance
        # For this example, we'll keep requests, but be aware of the blocking nature
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            results.append({
                "number": number,
                "status": "success",
                "response": response.json()
            })
            # Add the number to the successful list
            successful_recipients.append(number) 
        else:
            results.append({
                "number": number,
                "status": "failed",
                "error": response.text
            })
            
    return {
        "message": "Processing complete",
        "recipients": successful_recipients,  # This is what the frontend expects!
        "results_detail": results             # Keep the detailed results for debugging
    }