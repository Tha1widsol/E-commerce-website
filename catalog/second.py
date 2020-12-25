from flask import Blueprint,render_template,request,session,flash,url_for,redirect
import os
from catalog.objects import *
from admin.register import session_data

second = Blueprint("second",__name__,static_folder="static",template_folder="templates")

 
@second.route("/<name>")
def items_page(name):
    mycursor.execute("""SELECT * FROM Item WHERE type=%s """,(name,))
    items=mycursor.fetchall()

    if name=="TV":
        tvtab="active"
    else:
        tvtab=None

    if name=="Vaccumcleaners":
        vaccumtab="active"
    else:
        vaccumtab=None
    
    if name=="computers":
        computerstab="active"
    else:
        computerstab=None

    if session_data("user"):
        return render_template("items.html",page_name=name,database=items,tvtab=tvtab,vaccumtab=vaccumtab,computerstab=computerstab,foldername=name,user=session_data("user"))
    else:
         return render_template("items.html",page_name=name,database=items,tvtab=tvtab,vaccumtab=vaccumtab,computerstab=computerstab,foldername=name,user=None)

@second.route("<name>/<id>/<purchased>")
def button(name,id,purchased):
    if session_data("user"):
      return "<p> You bought this item </p>"
    else:
        flash("Please make an account or login before purchasing")
        return redirect(url_for("register.register_page"))




          



