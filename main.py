from flask import Flask, request
from src import fibonacci as fib
import json

app = Flask(__name__)

@app.route('/fib', methods=['GET'])
def fibonacci():
    n = request.args.get('n')

    if n is None or not n.isdigit():
        return {"status": 400, "message": "Bad request."}

    n = int(n)


    result = fib.calculate_fibonacci(n)
    response = {"result": result}

    return response


if __name__ == '__main__':
    app.run(debug=True)
