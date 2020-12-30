from flask import Flask,Blueprint,render_template,redirect,url_for,request,session,flash
from catalog.database import *
accounts = Blueprint("accounts",__name__,static_folder="static",template_folder="templates")


def check_data(*args):
    for data in args:
        if len(data)>0:
            return True
        else:
            return False
            
@accounts.route("/register",methods=["POST","GET"])
def register_page():
    if request.method =="POST":
        email = request.form.get("em")
        username = request.form.get("nm")
        password = request.form.get("ps")
        confirmpass = request.form.get("cps")
    
        if check_data(email,username,password,confirmpass):
            if password == confirmpass:
                    session["user"] = username
                    mycursor.execute("INSERT INTO Users (email,username,password) VALUES (%s,%s,%s)",(email,username,password))
                    db.commit()
                    flash("Account successfully created")
                    return redirect(url_for("home.home_page"))
                    

            else:
                flash("Passwords don't match. Please try again","info")
                return redirect(url_for(".register_page"))
        else:
            flash("Invalid details. Please try again")
            return redirect(url_for(".register_page"))


    else:
        if "user" in session:
            return render_template("register.html",registertab="active",user= session.get("user",None))
        else:
            return render_template("register.html",registertab="active",user=None)

@accounts.route("/login",methods=["POST","GET"])
def login_page():
   # if request.method=="POST":
    pass



@accounts.route("/logout")
def logout():
    if "user" in session:
         session.pop("user",None)
         return redirect(url_for("home.home_page"))
    
    else:
        flash("You are not logged in")
        return redirect(url_for("home.home_page"))
