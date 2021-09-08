from flask import Flask,Blueprint,render_template,redirect,url_for,request,session,flash
from catalog.database import *
from werkzeug.security import check_password_hash, generate_password_hash
from flask_wtf import FlaskForm
from wtforms import  PasswordField,StringField

accounts = Blueprint("accounts",__name__,static_folder="static",template_folder="templates")

class RegistrationForm(FlaskForm):
    email = StringField()
    password = PasswordField()
    confirm = PasswordField()

class LoginForm(FlaskForm):
    email = StringField()
    password = PasswordField()

def check_data(*args):
    for data in args:
        if len(data)>0:
            return True
        else:
            return False
   #and any(char.isupper() for char in password) and any(char.isdigit() for char in password) and any(char in symbols for char in password):
def check_password(password):
    valid = True
    symbols = ["!","£","$","%","^","&","*","(",")"]
    if len(password) < 12:
       flash("Password must be atleast 9 characters long")
       valid = False
    
    if not(any(char.isupper() for char in password)):
       flash("Password must contain atleast one uppercase character")
       valid = False


    if not(any(char.isdigit() for char in password)):
       flash("Password must contain atleast one digit")
       valid = False


    if not(any(char in symbols for char in password)):
       flash("Password must contain atleast one symbol")
       valid = False
    
    return valid
    

@accounts.route("/register",methods=["POST","GET"])
def register_page():
    form = RegistrationForm(request.form)
    if request.method =="POST" and form.validate():
        email = form.email.data
        password = form.password.data
        confirmpass = form.confirm.data

        if check_data(email,password,confirmpass):
            if check_password(str(password)):
                if password == confirmpass:
                    try:
                        hashed = generate_password_hash(password)
                        new_user = Users(email=email,password = hashed)
                        db.session.add(new_user)
                        new_user = Users.query.filter_by(email = email).first()
                        new_basket = Basket(user_id=new_user.id)
                        new_wishlist = wishlist(user_id= new_user.id)
                        db.session.add(new_wishlist)
                        db.session.add(new_basket)
                        db.session.commit()
                        session["user"] = email

                    except:
                        flash("Email already exists")
                        return redirect(url_for(".register_page"))
                        
                else:
                    flash("Passwords don't match")
                    return redirect(url_for(".register_page"))

                flash("Account successfully created")
                return redirect(url_for("items.home_page"))

            else:
                return redirect(url_for(".register_page"))
                    
        else:
            flash("Invalid details. Please try again")
            return redirect(url_for(".register_page"))


    else:
        if "user" in session:
            return redirect("items.home_page")
        else:
            return render_template("register.html",registertab="active",user=None,form = form)

@accounts.route("/login",methods=["POST","GET"])
def login_page():
    
    if "user" in session:
         return redirect("items.home_page")

    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        if check_data(email,password):
            found_user = get_user(email)

            if found_user:
                    if check_password_hash(found_user.password,password):
                        session["user"] = email
                        flash("Logged in successfully")
                        return redirect(url_for("items.home_page"))

                
            flash("Username or password is incorrect")
            return redirect(url_for(".login_page"))

        else:
            flash("Invalid details. Please try again")
            return redirect(url_for(".login_page"))

    else:
        return render_template("login.html",logintab="active",user=None,form = form)

@accounts.route("/logout")
def logout():
    if "user" in session:
         session.pop("user",None)
         flash("Logged out successfully")
         return redirect(url_for("items.home_page"))
    
    else:
        flash("You are not logged in")
        return redirect(url_for("items.home_page"))
