from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, World! 🚀</h1><p>This is your first Flask app.</p>"

if __name__ == '__main__':
    app.run(debug=True)
