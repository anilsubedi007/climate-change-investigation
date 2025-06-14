from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    print("Starting simple Flask test...")
    app.run(debug=True, host='127.0.0.1', port=8000)

