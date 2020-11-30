from flask import Blueprint,render_template

second = Blueprint("second",__name__,static_folder="static",template_folder="templates")

@second.route("/register")

def register():
    return render_template("register.html")





