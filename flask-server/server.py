from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
# Enable cors requests
CORS(app)

# Members API route


@cross_origin(origin="*", headers=["Content-Type"])
@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
