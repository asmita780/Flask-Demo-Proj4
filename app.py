from flask import Flask, render_template,request

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/submit", methods=["POST"])
def submit(): 
    username=request.form.get("username")
    password=request.form.get("password")

    details={
        "asmi123":"pass123",
        "jhon": "4563",
        "Ram":"sita123"
    }

    if username in details and password in details[username]:
        return render_template("home.html")
    else:
         return "Invalid-cradential"


@app.route("/contect")
def contect():
    return render_template("contect.html")



if __name__=="__main__":
    app.run()