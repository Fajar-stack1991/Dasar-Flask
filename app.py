# import library
from flask import Flask, render_template, url_for, redirect

# inisuaalisasi
app = Flask(__name__)
app.config['SECRET_KEY'] = "3rherfy43rf7y43r83r9"

# Routing
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/project")
def project():
    return render_template("project.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/redirect-about")
def redirect_about():
    return redirect(url_for("about"))

@app.route("/redirect-project")
def redirect_project():
    return redirect(url_for("project"))

@app.route("/redirect-contact")
def redirect_contact():
    return redirect(url_for("contact"))

# run flask
if __name__ == "__main__":
    app.run(debug=True)
