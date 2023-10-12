# import library
from flask import Flask, render_template

# inisuaalisasi
app = Flask(__name__)
app.config['SECRET_KEY'] = "3rherfy43rf7y43r83r9"

# Routing
@app.route("/")
def index():
    return render_template("index.html")

# run flask
if __name__ == "__main__":
    app.run(debug=True)
