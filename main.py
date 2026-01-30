"""
ECHO - A simple web server that echoes back request information
"""
from flask import Flask, request, jsonify, render_template_string
import json
from datetime import datetime

app = Flask(__name__)

# HTML template for the home page
HOME_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ECHO Server</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            border-bottom: 3px solid #4CAF50;
            padding-bottom: 10px;
        }
        .endpoint {
            background-color: #f9f9f9;
            padding: 15px;
            margin: 10px 0;
            border-left: 4px solid #4CAF50;
            border-radius: 4px;
        }
        code {
            background-color: #eee;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }
        .method {
            display: inline-block;
            padding: 4px 8px;
            border-radius: 4px;
            font-weight: bold;
            margin-right: 10px;
        }
        .get { background-color: #61affe; color: white; }
        .post { background-color: #49cc90; color: white; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔊 ECHO Server</h1>
        <p>A simple server that echoes back your requests with detailed information.</p>
        
        <h2>Available Endpoints:</h2>
        
        <div class="endpoint">
            <span class="method get">GET</span>
            <code>/</code> - This page
        </div>
        
        <div class="endpoint">
            <span class="method get">GET</span>
            <code>/echo</code> - Echo back GET request details
        </div>
        
        <div class="endpoint">
            <span class="method post">POST</span>
            <code>/echo</code> - Echo back POST request details and body
        </div>
        
        <div class="endpoint">
            <span class="method get">GET</span>
            <code>/health</code> - Health check endpoint
        </div>
        
        <h2>Example Usage:</h2>
        <pre><code>curl {{ base_url }}/echo?message=hello</code></pre>
        <pre><code>curl -X POST {{ base_url }}/echo -H "Content-Type: application/json" -d '{"text":"hello"}'</code></pre>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    """Home page with documentation"""
    base_url = request.host_url.rstrip('/')
    return render_template_string(HOME_TEMPLATE, base_url=base_url)

@app.route('/echo', methods=['GET', 'POST'])
def echo():
    """Echo endpoint that returns request information"""
    response_data = {
        'timestamp': datetime.utcnow().isoformat() + 'Z',
        'method': request.method,
        'url': request.url,
        'path': request.path,
        'headers': dict(request.headers),
        'args': dict(request.args),
        'remote_addr': request.remote_addr,
    }
    
    # Add body data for POST requests
    if request.method == 'POST':
        if request.is_json:
            response_data['json'] = request.get_json()
        else:
            response_data['data'] = request.get_data(as_text=True)
        response_data['content_type'] = request.content_type
    
    return jsonify(response_data)

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'ECHO',
        'timestamp': datetime.utcnow().isoformat() + 'Z'
    })

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=8080, debug=True)
