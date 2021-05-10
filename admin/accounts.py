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

@accounts.route("/register",methods=["POST","GET"])
def register_page():
    if request.method =="POST":
        email = request.form.get("em")
        password = request.form.get("ps").encode("utf-8")
        confirmpass = request.form.get("cps").encode("utf-8")
        if check_data(email,password,confirmpass):
                if password == confirmpass:
                        try:
                            mumbojumbo = bcrypt.hashpw(password,bcrypt.gensalt())
                            new_user = Users(email=email,password = mumbojumbo)
                            db.session.add(new_user)
                            new_user = Users.query.filter_by(email = email).first()
                            new_basket = Basket(user_id=new_user.id)
                            new_wishlist = wishlist(user_id= new_user.id)
                            db.session.add(new_wishlist)
                            db.session.add(new_basket)
                            db.session.commit()
                            session["user"] = email
                            
                        
                        except:
                              flash("Email already exists. Please try again")
                              return redirect(url_for(".register_page"))

                        flash("Account successfully created")
                        return redirect(url_for("items.home_page"))
                
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
    if request.method=="POST":
        email = request.form.get("em")
        password = request.form.get("ps").encode("utf-8")
        if check_data(email,password):
            found_user = Users.query.filter_by(email=email)
            if found_user:
                for i in found_user:
                    if bcrypt.checkpw(password,i.password):
                        session["user"] = email
                        flash("Logged in successfully")
                        return redirect(url_for("items.home_page"))
                
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
         flash("Logged out successfully")
         return redirect(url_for("items.home_page"))
    
    else:
        flash("You are not logged in")
        return redirect(url_for("items.home_page"))
