from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello():
    #return "Wandering hippos initiate secret karaoke events yearly."
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Process login credentials here (e.g., validate against a database)
        pass

    return render_template("login.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
