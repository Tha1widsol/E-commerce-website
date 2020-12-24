from flask import Flask,Blueprint,render_template,redirect,url_for,request,session,flash
from base.Home import *
register = Blueprint("register",__name__,static_folder="static",template_folder="templates")


@register.route("/register",methods=["POST","GET"])
def register_page():
        if request.method =="POST":
            email = request.form.get("em")
            username = request.form.get("nm")
            password = request.form.get("ps")
            session["user"] = username
            return redirect(url_for("home.home_page"))

        else:
            return render_template("register.html",registertab="active")

 

@register.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for(".register_page"))

    