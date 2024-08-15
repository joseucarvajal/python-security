from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/echo', methods=['GET'])
def echo():
    param = request.args.get('param', default='', type=str)
    return jsonify({'response': param})

if __name__ == '__main__':
    app.run(debug=True)