from flask import Flask,Blueprint,render_template,redirect,url_for,request,session,flash

register = Blueprint("register",__name__,static_folder="static",template_folder="templates")


def check_data(*args):
    for data in args:
        if len(data)>0:
            return True
        else:
            return False
            
@register.route("/register",methods=["POST","GET"])
def register_page():
    if request.method =="POST":
        email = request.form.get("em")
        username = request.form.get("nm")
        password = request.form.get("ps")
        confirmpass = request.form.get("cps")
        if check_data(email,username,password,confirmpass):
            if password == confirmpass:
                    session["user"] = username
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


@register.route("/logout")
def logout():
    if "user" in session:
         session.pop("user",None)
         return redirect(url_for("home.home_page"))
    
    else:
        flash("You are not logged in")
        return redirect(url_for("home.home_page"))
