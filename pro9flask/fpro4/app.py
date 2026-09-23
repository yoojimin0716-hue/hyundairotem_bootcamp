from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/condition")
def condition():
    score = 85
    return render_template("condition.html", score =score)

@app.route("/loop")
def loop():
    users = ["김우진","민규보","유지민"]
    return render_template("loop.html",users=users)


@app.route("/filter")
def filter():
    message = "hello flask jinja2"
    price = 12345
    return render_template("filter.html", message=message,price = price)

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port = 5000)