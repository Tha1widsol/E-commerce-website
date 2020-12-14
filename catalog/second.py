from flask import Blueprint,render_template
import os
from catalog.objects import *

second = Blueprint("second",__name__,static_folder="static",template_folder="templates")

 
@second.route("/TVs")
def tv_page():
    values= "TV"
    mycursor.execute("""SELECT * FROM Item WHERE type=TV""")
    items=mycursor.fetchall()
    
    
    return render_template("items.html",page_name="TV's",database=items,tvtab="active",foldername="tvs")



@second.route("purchased")
def button():
    return "<p> You bought this item </p>"

          



