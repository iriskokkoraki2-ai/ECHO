const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON bodies
app.use(express.json());
app.use(express.text());
app.use(express.urlencoded({ extended: true }));

// Root endpoint - welcome message
app.get('/', (req, res) => {
  res.send(`
    <html>
      <head><title>ECHO Server</title></head>
      <body>
        <h1>Welcome to ECHO Server!</h1>
        <p>This is a simple echo server that returns whatever you send to it.</p>
        <h2>Usage:</h2>
        <ul>
          <li>GET /echo?message=your_message - Returns your message</li>
          <li>POST /echo - Returns the request body</li>
          <li>GET /health - Health check endpoint</li>
        </ul>
      </body>
    </html>
  `);
});

// GET endpoint with query parameter
app.get('/echo', (req, res) => {
  const message = req.query.message || 'No message provided';
  res.json({
    echo: message,
    timestamp: new Date().toISOString()
  });
});

// POST endpoint that echoes back the body
app.post('/echo', (req, res) => {
  res.json({
    echo: req.body,
    timestamp: new Date().toISOString()
  });
});

// Health check endpoint
app.get('/health', (req, res) => {
  res.json({
    status: 'healthy',
    uptime: process.uptime(),
    timestamp: new Date().toISOString()
  });
});

// Start the server
app.listen(PORT, '0.0.0.0', () => {
  console.log(`Echo server is running on port ${PORT}`);
  console.log(`Visit http://localhost:${PORT} for usage information`);
});
