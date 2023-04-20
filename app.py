from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import akoben_main
from akoben_main import response

app = Flask(__name__)


# CORS(app)


@app.route("/")
def hello_world():
    return render_template("ako_UI.html")


@app.post("/predict")
def predict():
    text = request.get_json().get("msg")

    response = akoben_main.response(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)



