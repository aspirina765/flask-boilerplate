# from flask import Flask, request, jsonify
# from pymongo import MongoClient

# app = Flask(__name__)


# def get_db():
#     client = MongoClient('mongodb://db:27017/', connect=False)
#     return client.application_database


# @app.route("/ping")
# def ping():
#     return "pong"


# # to check DB connection:
# @app.route("/users", methods=['GET', 'POST'])
# def users_route():
#     try:
#         if request.method == 'GET':
#             users = []
#             for user in get_db().users.find():
#                 users.append(user.get("name", ""))
#             return jsonify({"status": "success", "payload": users}), 200
#         elif request.method == 'POST':
#             try:
#                 name = request.form["name"]
#             except KeyError:
#                 return jsonify({"status": "failed", "payload": "Please insert a name"}), 400
#             user_id = get_db().users.insert_one({'name': name}).inserted_id
#             return jsonify({"status": "success", "payload": str(user_id)}), 200
#     except Exception:
#         return (
#             jsonify({"status": "failed", "payload": "An internal server error happened. Please try again later"}),
#             500
#         )


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", debug=True)

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
    app.run(host="0.0.0.0", debug=True)
    #app.run(port=5007)
