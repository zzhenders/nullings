import os
from flask import Flask, render_template

DIRECTORY = os.path.dirname(__file__)
CLIENT = DIRECTORY + "/../client/build"

app = Flask(
    __name__, static_folder=f"{CLIENT}/static", template_folder=f"{CLIENT}"
)

# Serve React
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path):
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
