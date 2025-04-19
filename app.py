from flask import Flask, request, jsonify
import itertools

app = Flask(__name__)

# ... [Rest of the code remains the same] ...

if __name__ == '__main__':
    app.run(debug=True)
