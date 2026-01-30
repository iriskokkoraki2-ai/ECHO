# ECHO

A simple web server that echoes back request information. This application was migrated from Replit to GitHub.

## Features

- 🔊 Echo back HTTP request details (headers, query params, body, etc.)
- 🌐 RESTful API endpoints
- 💚 Health check endpoint
- 📱 Simple web interface with documentation

## Installation

### Prerequisites
- Python 3.11 or higher
- pip

### Setup

1. Clone the repository:
```bash
git clone https://github.com/iriskokkoraki2-ai/ECHO.git
cd ECHO
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Server

```bash
python main.py
```

The server will start on `http://0.0.0.0:8080`

### API Endpoints

#### GET /
Home page with documentation

#### GET /echo
Echo back GET request details
```bash
curl http://localhost:8080/echo?message=hello&test=123
```

#### POST /echo
Echo back POST request details and body
```bash
curl -X POST http://localhost:8080/echo \
  -H "Content-Type: application/json" \
  -d '{"text": "hello world", "number": 42}'
```

#### GET /health
Health check endpoint
```bash
curl http://localhost:8080/health
```

### Example Response

```json
{
  "timestamp": "2026-01-30T22:00:00.000000Z",
  "method": "GET",
  "url": "http://localhost:8080/echo?message=hello",
  "path": "/echo",
  "headers": {
    "Host": "localhost:8080",
    "User-Agent": "curl/7.68.0"
  },
  "args": {
    "message": "hello"
  },
  "remote_addr": "127.0.0.1"
}
```

## Running on Replit

This project includes Replit configuration files (`.replit` and `replit.nix`). Simply:
1. Import this repository to Replit
2. Click "Run"

## Development

The application uses Flask, a lightweight Python web framework.

### Project Structure
```
ECHO/
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
├── .replit             # Replit configuration
├── replit.nix          # Replit Nix configuration
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## License

This project is open source and available for educational purposes.