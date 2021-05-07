from flask import Flask,render_template,redirect,url_for,request,session,flash
from base.Home import *
from catalog.items import *
from admin.accounts import *
from catalog.database import *

app.register_blueprint(items,url_prefix="/") 

app.register_blueprint(home,url_prefix="/")
app.register_blueprint(accounts,url_prefix="/")

if __name__ =="__main__":
    app.run(debug=True)


        