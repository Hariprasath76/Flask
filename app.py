from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>Hariprasath - DevOps Engineer</title>
        <style>
            body {
                background-color: #f0f4f8;
                color: #333;
                font-family: 'Arial', sans-serif;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                text-align: center;
            }
            h1 {
                color: #2c3e50;
                font-size: 3em;
                margin-bottom: 0.2em;
            }
            p {
                font-size: 1.5em;
                color: #2980b9;
                margin-top: 0;
                margin-bottom: 1em;
            }
            .signature {
                font-weight: bold;
                font-size: 1.2em;
                color: #e67e22;
                border: 2px solid #e67e22;
                padding: 10px 20px;
                border-radius: 8px;
                display: inline-block;
                letter-spacing: 1.2px;
                box-shadow: 0 4px 6px rgba(230, 126, 34, 0.4);
            }
        </style>
    </head>
    <body>
        <h1>Hello, I'm Hariprasath!</h1>
        <p>Welcome to my simple Flask website.</p>
        <div class="signature">DEVOPS ENGINEER</div>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

#if __name__ == '__main__':
 #   app.run(debug=True)
