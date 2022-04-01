from flask import Flask,render_template
import discover_last_weekly

app = Flask(__name__)

#rendering the HTML page which has the button
@app.route('/')
def main():
    return render_template('index.html')

#background process happening
@app.route('/sheesh', methods=['GET','POST'])
def run_DLW():
    discover_last_weekly.main()
    return render_template('sheesh.html')