from flask import Flask,render_template,redirect,url_for,request,session,flash
from catalog.second import *
from base.Home import *
from admin.accounts import *



app = Flask(__name__)

app.register_blueprint(second,url_prefix="/") # We only go on second blueprint if we see "/admin"
#It finds "/" then adds "admin" = "/admin" 
app.register_blueprint(home,url_prefix="/")
app.register_blueprint(accounts,url_prefix="/")
app.config['SECRET_KEY'] = "helsgddo"


if __name__ =="__main__":
    app.run(debug=True,use_reloader=False)


        
