from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Python App Deployment</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                background: #f4f4f4;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                font-family: Arial, sans-serif;
            }

            .card {
                background: white;
                width: 480px;
                padding: 30px;
                border-radius: 16px;
                text-align: center;
                box-shadow: 0 4px 14px rgba(0, 0, 0, 0.15);
                animation: slideUp 0.7s ease;
            }

            h1 {
                color: #0078ff;
                margin-bottom: 10px;
            }

            p {
                color: #333;
                font-size: 16px;
                margin-bottom: 20px;
            }

            ul {
                text-align: left;
                margin: 0 auto;
                padding-left: 18px;
                max-width: 300px;
            }

            li {
                margin-top: 5px;
                color: #444;
                font-size: 15px;
            }

            .version {
                margin-top: 15px;
                background: #0078ff;
                padding: 8px 12px;
                color: #fff;
                display: inline-block;
                border-radius: 10px;
                font-weight: bold;
            }

            @keyframes slideUp {
                from { transform: translateY(40px); opacity: 0; }
                to { transform: translateY(0); opacity: 1; }
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 Deployment Successful</h1>
            <p>Your Python Flask application is up and running!</p>

            <h3 style="margin-top: 20px;">Deployment Pipeline Used:</h3>
            <ul>
                <li>Python (Flask Framework)</li>
                <li>Docker Containerization</li>
                <li>Jenkins Declarative Pipeline</li>
                <li>GitHub Webhook (Automated CI/CD)</li>
            </ul>

            <div class="version">Version: 2.0</div>
        </div>
    </body>
    </html>
    """

@app.route('/hi')
def hell():
    return '<h1 style="text-align:center; margin-top:40px;">👋 Hello from Flask & Docker!</h1>'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
