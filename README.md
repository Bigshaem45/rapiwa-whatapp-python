# Rapiwa WhatsApp Messenger

A production-ready FastAPI application that enables automated WhatsApp message sending through the Rapiwa API. This project demonstrates seamless integration between a modern web interface and WhatsApp's messaging infrastructure, allowing bulk message delivery to multiple recipients.

<img width="959" height="422" alt="image" src="https://github.com/user-attachments/assets/4e463ea7-0a53-40cd-aaf2-a8f70cce5bbd" />


## Features

- **Bulk Messaging**: Send WhatsApp messages to multiple recipients simultaneously
- **Clean UI**: Modern, responsive interface built with vanilla JavaScript and CSS
- **Real-time Feedback**: Instant success/failure notifications for each message sent
- **Form Validation**: Built-in validation for phone numbers and message content
- **Error Handling**: Comprehensive error management with detailed logging
- **CORS Enabled**: Ready for frontend-backend separation in production

## Architecture

This application follows a clean architecture pattern:

- **Backend**: FastAPI serves as the REST API layer, handling HTTP requests and communication with Rapiwa's API
- **Frontend**: Static HTML/CSS/JavaScript provides an intuitive user interface
- **Integration**: Environment-based configuration ensures secure API key management

## 📋 Prerequisites

Before running this application, ensure you have:

- Python 3.8 or higher
- A Rapiwa API account and API key
- pip (Python package manager)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/rapiwa-whatsapp-python.git
   cd rapiwa-whatsapp-python
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install fastapi uvicorn python-dotenv requests jinja2 python-multipart
   ```

4. **Configure environment variables**
   
   Create a `.env` file in the project root:
   ```env
   API_KEY='your_rapiwa_api_key_here'
   ```

## 🎯 Usage

1. **Start the server**
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the application**
   
   Open your browser and navigate to: `http://127.0.0.1:8000`

3. **Send messages**
   - Enter recipient phone numbers (comma-separated, with country codes)
   - Type your message in the description field
   - Click "Send Message"
   - View success notifications for each recipient

## 📁 Project Structure

```
rapiwa-whatsapp-python/
├── main.py                 # FastAPI application and API routes
├── templates/
│   └── index.html         # Frontend interface
├── static/
│   └── style.css          # Application styling
├── .env                   # Environment variables (not tracked)
├── .gitignore            # Git ignore rules
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies (create this)
```

## 🔑 API Endpoints

### `GET /`
Serves the main application interface.

### `POST /send-message/`
Sends WhatsApp messages to specified recipients.

**Request Body** (Form Data):
- `phoneNumbers`: Comma-separated list of phone numbers with country codes
- `messageDescription`: Message content to send

**Response**:
```json
{
  "message": "Processing complete",
  "recipients": ["+2349400390290", "+2349977587623"],
  "results_detail": [...]
}
```

## 🛠️ Technical Stack

- **Backend Framework**: FastAPI
- **HTTP Client**: Requests
- **Template Engine**: Jinja2
- **Configuration**: python-dotenv
- **Server**: Uvicorn (ASGI)
- **Frontend**: Vanilla JavaScript, HTML5, CSS3

## 🔐 Security Considerations

- API keys are stored in environment variables, not hardcoded
- `.env` file is excluded from version control via `.gitignore`
- CORS is configured (adjust for production deployment)
- Input validation on both frontend and backend

## 🚧 Future Enhancements

- [ ] Add message templates
- [ ] Implement message scheduling
- [ ] Support for media attachments (images, documents)
- [ ] Message delivery tracking and analytics
- [ ] User authentication system
- [ ] Database integration for message history
- [ ] Rate limiting implementation
- [ ] Docker containerization

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/rapiwa-whatsapp-python/issues).

## 📧 Contact

https://github.com/Bigshaem45

Project Link: https://github.com/Bigshaem45/rapiwa-whatapp-python

## 🙏 Acknowledgments

- [Rapiwa](https://rapiwa.com) for providing the WhatsApp API
- [FastAPI](https://fastapi.tiangolo.com/) for the excellent web framework
- The Python community for continuous support
