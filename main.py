from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route("/", methods=["GET"])
def landing_page():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)