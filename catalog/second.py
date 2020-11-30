from flask import Blueprint,render_template
import os

second = Blueprint("second",__name__,static_folder="static",template_folder="templates")


@second.route("/button")         
def button():
     return "<p> You Bought this vaccum cleaner!</p>"



