from flask import Flask,Blueprint,render_template,redirect,url_for,request,session,flash
from catalog.database import *
import bcrypt
accounts = Blueprint("accounts",__name__,static_folder="static",template_folder="templates")


def check_data(*args):
    for data in args:
        if len(data)>0:
            return True
        else:
            return False
            
def exists(username,email):
    q = """SELECT username,email FROM Users"""
    mycursor.execute(q)
    for data in mycursor.fetchall():
       data = list(data)
       if username in data[0] or email ==data[1]:
          return True

    return False


@accounts.route("/register",methods=["POST","GET"])
def register_page():
    if request.method =="POST":
        email = request.form.get("em")
        username = request.form.get("nm")
        password = request.form.get("ps").encode("utf-8")
        confirmpass = request.form.get("cps").encode("utf-8")
        if check_data(email,username,password,confirmpass):
          if not(exists(username,email)):
            if password == confirmpass:
                    session["user"] = username
                    mumbojumbo = bcrypt.hashpw(password,bcrypt.gensalt())
                    insert = 'INSERT INTO Users (email,username,password) VALUES (%s,%s,%s)'
                    mycursor.execute(insert,[(email),(username),(mumbojumbo)])
                    db.commit()
                    flash("Account successfully created")
                    return redirect(url_for("home.home_page"))
            
            else:
                flash("Passwords don't match. Please try again","info")
                return redirect(url_for(".register_page"))
                    
          else:
              flash("Username or email already exists. Please try again")
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
    if request.method=="POST":
        username = request.form.get("nm")
        password = request.form.get("ps").encode("utf-8")
        if check_data(username,password):
            mycursor.execute("""SELECT username,password FROM Users""")
            user = mycursor.fetchall()
            for data in user:
                if username== data[0] and bcrypt.checkpw(password,data[1].encode("utf-8")):
                    session["user"] = username
                    flash("Logged in successfully")
                    return redirect(url_for("home.home_page"))
            
            flash("Username or password is incorrect")
            return redirect(url_for(".login_page"))

        else:
            flash("Invalid details. Please try again")
            return redirect(url_for(".login_page"))


    else:
        return render_template("login.html",logintab="active",user=None)

@accounts.route("/logout")
def logout():
    if "user" in session:
         session.pop("user",None)
         return redirect(url_for("home.home_page"))
    
    else:
        flash("You are not logged in")
        return redirect(url_for("home.home_page"))
