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
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: #ffffff;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                color: black;
                text-align: center;
            }
            .container {
                padding: 40px 60px;
                background: gold;
                border-radius: 20px;
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
                min-width: 300px;
            }
            h1 {
                font-size: 3.5rem;
                margin-bottom: 10px;
                letter-spacing: 3px;
                text-transform: uppercase;
                color: red;
            }
            p {
                font-size: 1.8rem;
                font-weight: 600;
                letter-spacing: 2px;
                color: black;
                margin: 0;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hariprasath</h1>
            <p>DevOps Engineer</p>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
