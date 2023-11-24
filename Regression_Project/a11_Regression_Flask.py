from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/hello')

def hello():
    return "Hi"

if __name__ == "__main__":
    print("Flask server starting")
    app.run()
