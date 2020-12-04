from flask import Flask,render_template,redirect,url_for,request,session,flash
import os 
from catalog.second import second,Item
from catalog.objects import *

app = Flask(__name__)
app.register_blueprint(second,url_prefix="/") # We only go on second blueprint if we see "/admin"
#It finds "/" then adds "admin" = "/admin" 

@app.route("/")
@app.route("/home")
def home():
     return render_template("home.html",hometab="active")

   
#Extra comment
if __name__ =="__main__":
    app.run()


        
