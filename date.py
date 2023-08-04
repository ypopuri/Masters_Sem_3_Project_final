# importing Flask and other modules
from flask import Flask, request, render_template

# Flask constructor
app = Flask(__name__)

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
        Date = request.form.get("Date")
        return "Your name is "+Date
    return render_template("date.html")

if __name__=='__main__':
    app.run()