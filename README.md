# ECHO

A simple Node.js echo server application that can run on Replit and GitHub.

## Description

ECHO is a lightweight HTTP server that echoes back the data you send to it. It's perfect for testing APIs, webhooks, or learning about HTTP requests and responses.

## Features

- 🔄 Echo GET requests with query parameters
- 📮 Echo POST requests with request body
- 💚 Health check endpoint
- 🚀 Easy to deploy on Replit
- 📦 Simple setup with Node.js and Express

## Quick Start

### Running on Replit

1. Click the "Run" button in Replit
2. The server will start automatically
3. Visit the URL provided by Replit

### Running Locally

1. Install dependencies:
   ```bash
   npm install
   ```

2. Start the server:
   ```bash
   npm start
   ```

3. Open your browser to `http://localhost:3000`

## API Endpoints

### GET /
Welcome page with usage instructions

### GET /echo?message=your_message
Returns the message you provide as a query parameter.

**Example:**
```bash
curl "http://localhost:3000/echo?message=Hello+World"
```

**Response:**
```json
{
  "echo": "Hello World",
  "timestamp": "2026-01-30T22:00:00.000Z"
}
```

### POST /echo
Echoes back the request body.

**Example:**
```bash
curl -X POST http://localhost:3000/echo \
  -H "Content-Type: application/json" \
  -d '{"test": "data"}'
```

**Response:**
```json
{
  "echo": {"test": "data"},
  "timestamp": "2026-01-30T22:00:00.000Z"
}
```

### GET /health
Health check endpoint for monitoring.

**Response:**
```json
{
  "status": "healthy",
  "uptime": 123.456,
  "timestamp": "2026-01-30T22:00:00.000Z"
}
```

## Configuration

The server uses the `PORT` environment variable if available, otherwise defaults to port 3000.

## License

MIT