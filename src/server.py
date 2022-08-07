from flask import Flask, jsonify, request

app = Flask(__name__)

incomes_r = [{'description': 'r', 'amount': 'AA'}]
incomes_dly = [{'description': 'dly', 'amount': '0.030'}]
incomes_d = [{'description': 'd', 'amount': '0.080'}]

@app.route('/r',methods=["POST", "GET"])
def get_r():
  content = []
  if request.method == "GET":
    content = incomes_r
    # if request.headers.get("accept") == "application/json":
    # content = request.get_json()
  return jsonify(content)


@app.route('/d',methods=["POST", "GET"])
def get_d():
    content = []
    if request.method == "GET":
      content = incomes_d
    return jsonify(content)


@app.route('/dly',methods=["POST", "GET"])
def get_dly():
    content = []
    if request.method == "GET":
      content = incomes_dly
    return jsonify(content)

if __name__ == '__main__':
    app.run(port=5007)
