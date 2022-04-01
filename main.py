from flask import Flask, render_template
from discover_last_weekly import main


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    # if request.method == "POST":
    #     DLW()
    return render_template("index.html")

@app.route("/sheesh",methods=["GET", "POST"])
def DLW_through():
    main()
    return render_template("sheesh.html")


