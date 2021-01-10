from flask import Blueprint,render_template,request,session,flash,url_for,redirect
import os
from catalog.database import *

items = Blueprint("items",__name__,static_folder="static",template_folder="templates")
 
@items.route("/<item_type>")
def items_page(item_type):
    mycursor.execute("""SELECT * FROM Item WHERE type=%s """,(item_type,))
    items=mycursor.fetchall()

    if item_type=="TV":
        tvtab="active"
    else:
        tvtab=None

    if item_type=="Vaccumcleaners":
        vaccumtab="active"
    else:
        vaccumtab=None
    
    if item_type=="computers":
        computerstab="active"
    else:
        computerstab=None

    if "user" in session:
        return render_template("items.html",page_name=item_type,database=items,tvtab=tvtab,vaccumtab=vaccumtab,computerstab=computerstab,foldername=item_type,user= session.get("user",None))
    else:
         return render_template("items.html",page_name=item_type,database=items,tvtab=tvtab,vaccumtab=vaccumtab,computerstab=computerstab,foldername=item_type,user=None)

@items.route("/button/<id>/<item_type>")
def button(id,item_type):
    if "user" in session:
        flash("Item added to basket")
        username = session.get("user",None)
        mycursor.execute("""SELECT ID FROM Users WHERE username= '%s'""" %(username))
        
        UserID = mycursor.fetchone()
        ItemID = id

        mycursor.execute("INSERT INTO BasketItems(UsersID,productID) VALUES (%s,%s)",(*UserID,ItemID))
        db.commit()

        return redirect(url_for(".items_page",item_type=item_type))
     

    else:
        flash("Please make an account or login before purchasing")
        return redirect(url_for("accounts.register_page"))


@items.route("/basket")
def basket_page():
    total_price = 0
    if "user" in session:
        username = session.get("user",None)
        get_id = """SELECT ID FROM Users WHERE username = '%s' """%(username)
        mycursor.execute(get_id)

        id = mycursor.fetchone()
        mycursor.execute("""SELECT Item.name,Item.description,Item.price,Item.picfile,Item.type FROM Item INNER JOIN BasketItems ON Item.itemID = BasketItems.productID WHERE BasketItems.UsersID = '%s'"""%(id))
        basket_items = mycursor.fetchall()
        for item in basket_items:
            total_price +=item[2]
        db.commit()
        return render_template("basket.html",basket_items = basket_items,user=session.get("user",None),total_price = total_price)

    else:
        return render_template("basket.html",user=None)
