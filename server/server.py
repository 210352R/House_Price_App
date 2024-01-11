from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route("/get_location_names", methods=["GET"])
def get_location_names():
    response = jsonify({"locations": util.get_location_names()})
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


@app.route("/predict_home_price", methods=["POST"])
def predict_home_price():
    total_sqft = float(request.form["total_sqft"])
    location = request.form["location"]
    bhk = int(request.form["bhk"])
    bath = int(request.form["bath"])

    response = jsonify(
        {"estimated_price": util.get_estimated_price(location, total_sqft, bhk, bath)}
    )
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


@app.route("/user/<username>")
def show_user_profile(username):
    print(username)
    myresponse = jsonify({"username": username})
    return myresponse


if __name__ == "__main__":
    util.load_saved_artifacts()
    print("Python Flask server running in http://localhost:5000/")
    app.config["DEBUG"] = True
    app.run()
