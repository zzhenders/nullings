import os
from flask import Flask, render_template
from model import connect_to_db, DB_URI, db
from model import Post, PostContent, Page, PageContent

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
    connect_to_db(app, DB_URI)
    app.run(debug=True, host="0.0.0.0")
