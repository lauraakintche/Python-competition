from flask import Flask, render_template, request

app = Flask("MyApp")

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/index.html")
def ret_index():
    return render_template("index.html")


@app.route("/<name>")
def hello_someone(name):
    return render_template("hello.html", name=name.title())

@app.route("/about.html")
def about():
    return render_template("about.html")



@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form

    return "Thank you: " +form_data["email"] + " !"

app.run (debug=True)
