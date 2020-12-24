from flask import Flask,Blueprint,render_template,redirect,url_for,request,session,flash

register = Blueprint("register",__name__,static_folder="static",template_folder="templates")


def session_data(*args):
    for data in args:
     if data in session:
        data = session[data]
        return data,True
    
     else:
        return None
        
@register.route("/register",methods=["POST","GET"])
def register_page():
        if request.method =="POST":
            email = request.form.get("em")
            username = request.form.get("nm")
            password = request.form.get("ps")
            session["user"] = username
            return redirect(url_for("home.home_page"))

        else:
            if session_data("user"):
              return render_template("register.html",registertab="active",user_in_session=session_data("user")[1])
            else:
                 return render_template("register.html",registertab="active")


@register.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for(".register_page"))
