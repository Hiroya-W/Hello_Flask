from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語文字化け対策
app.config["JSON_SORT_KEYS"] = False  # ソートをそのまま


@app.route("/hello")
def hello(name=None):
    data = [{"name": "山田"}, {"age": 30}]
    return jsonify({"status": "OK", "data": data})


@app.route("/good")
def good():
    name = "Good"
    return name


if __name__ == "__main__":
    # curl -X "POST" "127.0.0.1:5000/hello" -d "name=hiro"
    app.run(debug=True)
