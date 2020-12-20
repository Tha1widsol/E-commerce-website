from flask import Flask,Blueprint,render_template,redirect,url_for,request,session,flash

register = Blueprint("register",__name__,static_folder="static",template_folder="templates")

@register.route("/register")
def register_page():
    return render_template("register.html",registertab="active")