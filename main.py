from flask import Flask,render_template,redirect,url_for,request,session,flash

from admin.second import second

app = Flask(__name__)
app.register_blueprint(second,url_prefix="/admin") # We only go on second blueprint if we see "/admin"
#It finds "/" then adds "admin" = "/admin" 

@app.route("/")
@app.route("/home")
def home():
     return render_template("home.html")

@app.route("/items")
def items():
    return render_template("items.html")
   
#
if __name__ =="__main__":
    app.run()
