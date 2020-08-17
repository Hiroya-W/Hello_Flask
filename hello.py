from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/hello")
def hello(name=None):
    name = request.args.get("name")
    return render_template("hello.html", title="Flask Test", name=name)


@app.route("/good")
def good():
    name = "Good"
    return name


if __name__ == "__main__":
    # curl -X "POST" "127.0.0.1:5000/hello" -d "name=hiro"
    app.run(debug=True)
