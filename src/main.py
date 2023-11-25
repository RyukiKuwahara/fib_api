from flask import Flask, request, jsonify
import fibonacci as fib

app = Flask(__name__)

@app.route('/fib', methods=['GET'])
def fibonacci():

    content_type = request.headers.get('Content-Type')

    if content_type != 'application/json':
        return jsonify({"status": 415, "message": "Unsupported Media Type"}), 415

    n = request.args.get('n')

    if n is None or not n.isdigit() or n == "0":
        return jsonify({"status": 400, "message": "Bad request."}), 400

    n = int(n)
    result = fib.calculate_fibonacci(n)
    response = jsonify({"result": result}), 200

    return response


if __name__ == '__main__':
    app.run(debug=True)
