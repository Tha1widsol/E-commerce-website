from flask import Blueprint,render_template
import os
from catalog.objects import *

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


    return render_template("items.html",page_name=name,database=items,tvtab=tvtab,vaccumtab=vaccumtab,computerstab=computerstab,foldername=name)


@second.route("<id>/<purchased>")
def button(id,purchased):
    return "<p> You bought this item </p>"


          



