from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/get', methods=["GET"])
def get():
    jsonReturn = {"Response": "OK"}
    return jsonify(jsonReturn), 200


@app.route('/get/senha', methods=['GET'])
def get2():
    senha = request.args.get("senha")
    print(senha)
    if senha == "1234":
        jsonReturn = {"response": "OK, acesso permitido"}
        return jsonify(jsonReturn), 200
    else:
        jsonReturn = {"Error": "Senha invalida"}
        return jsonify(jsonReturn), 401


if __name__ == "__main__":
    app.run(host="localhost", debug=True)
