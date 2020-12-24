from flask import Blueprint,render_template,request,session
from admin.register import *
home = Blueprint("home",__name__,static_folder="static",template_folder="templates")

@home.route("/")
@home.route("/home")
def home_page():
     if "user" in session:
        user = session["user"]
        return render_template("home.html",hometab="active",user=user)
     else:
         return render_template("home.html",hometab="active",user=None)




#Extra comment