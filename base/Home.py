from flask import Blueprint,render_template,request,session

home = Blueprint("home",__name__,static_folder="static",template_folder="templates")

@home.route("/")
@home.route("/home_page")
def home_page():
     if "user" in session:
        return render_template("home.html",hometab="active",user=session.get("user",None))
     else:
         return render_template("home.html",hometab="active",user=None)




#Extra comment