from flask import Blueprint,render_template

home = Blueprint("home",__name__,static_folder="static",template_folder="templates")

@home.route("/")
@home.route("/home")
def home_page():
     return render_template("home.html",hometab="active")

#Extra comment