from flask import Flask, render_template, request
from face_recognition import capture_and_recognize_face

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/authenticate", methods=["POST"])
def authenticate():
    if capture_and_recognize_face():
        return "Authentication Successful!"
    else:
        return "Authentication Failed!"

if __name__ == "__main__":
    app.run(debug=True)
