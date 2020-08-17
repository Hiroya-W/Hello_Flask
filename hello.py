from flask import Flask, render_template
import pymysql

app = Flask(__name__)


@app.route("/")
def hello():
    # db setting
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        db="testdb",
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor,
    )

    cur = db.cursor()
    sql = "SELECT * FROM MEMBERS"
    cur.execute(sql)
    members = cur.fetchall()

    cur.close()
    db.close()
    return render_template("hello.html", title="Flask Test", name=name)


@app.route("/good")
def good():
    name = "Good"
    return name


if __name__ == "__main__":
    app.run(debug=True)
