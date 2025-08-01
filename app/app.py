from flask import Flask, render_template, request, redirect, flash, url_for, session


import mysql.connector


app = app = Flask(
    __name__,
    template_folder="C:\\Users\\kouss\\coding\\AppleZone\\app\\templates",
)

app.secret_key = "AppleZone_secret_key2025_18_20_08_04_ 05"


database = mysql.connector.connect(
    host="localhost", user="root", password="Bluemoon 1894", database="AppleZone"
)

cursor = database.cursor()


@app.route("/")
def home_page():
    return render_template("home_page.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        sql = "SELECT * FROM clients WHERE email = %s"
        cursor.execute(sql, (email,))
        client = cursor.fetchone()

        if client and client[5] == password:
            session["email"] = email
            return redirect(url_for("home_page"))
        else:
            return "Connexion échouée. Essayez encore."

    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        nom = request.form["nom"]
        prenom = request.form["prenom"]
        email = request.form["email"]
        telephone = request.form["telephone"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            return "Les mots de passes ne correspondent pas"

        sql = "insert into Clients(nom, prenom,email,telephone,password) values(%s,%s,%s,%s,%s)"
        val = (nom, prenom, email, telephone, password)

        cursor.execute(sql, val)

        database.commit()

        # Inscription réussie ! Bienvenue sur Apple Zone 🍎

        return redirect(url_for("home_page"))

    return render_template("signup.html")


@app.route("/iPhone")
def iPhone():
    return render_template("iPhone.html")


@app.route("/macBook")
def macBook():
    return render_template("macBook.html")


@app.route("/airPod")
def method_name():
    return render_template("airPod.html")


if __name__ == "__main__":
    app.run(debug=True)
