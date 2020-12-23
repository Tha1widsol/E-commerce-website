from flask import Flask,Blueprint,render_template,redirect,url_for,request,session,flash

register = Blueprint("register",__name__,static_folder="static",template_folder="templates")

@register.route("/register",methods=["POST","GET"])
def register_page():
    if request.method =="POST":
        email = request.form.get("em")
        username = request.form.get("nm")
        password = request.form.get("ps")
        return redirect(url_for('.user',usr=username))

    else:
        return render_template("register.html",registertab="active")

@register.route("/<usr>")
def user(usr):
    return "<h1> Welcome </h1>"
    