from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get('name', 'world')
    return jsonify(message=f'Hello, {name}!')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)