from flask import Blueprint,render_template,request,session
from admin.register import session_data
home = Blueprint("home",__name__,static_folder="static",template_folder="templates")

@home.route("/")
@home.route("/home")
def home_page():
     if session_data("user"):
        return render_template("home.html",hometab="active",user=session_data("user")[0],user_in_session=session_data("user")[1])
     else:
         return render_template("home.html",hometab="active",user=None)




#Extra comment