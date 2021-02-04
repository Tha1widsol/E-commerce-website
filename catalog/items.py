from flask import Blueprint,render_template,request,session,flash,url_for,redirect
import os
from catalog.database import *

items = Blueprint("items",__name__,static_folder="static",template_folder="templates")


@items.route("/<item_type>",methods=["POST","GET"])
def items_page(item_type):
    mycursor.execute("""SELECT * FROM Item WHERE type=%s """,(item_type,))
    items=mycursor.fetchall()
    
    if request.method=="POST" and "user" in session:
        quantity = request.form.get("dropdown")
        session["quantity"] = quantity

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
        return render_template("items.html",page_name=item_type,database=items,tvtab=tvtab,vaccumtab=vaccumtab,computerstab=computerstab,foldername=item_type,user= session.get("user",None),items_in_basket = session.get("items_in_basket",None))
    else:
        return render_template("items.html",page_name=item_type,database=items,tvtab=tvtab,vaccumtab=vaccumtab,computerstab=computerstab,foldername=item_type,user=None)


@items.route("/button/<id>/<item_type>")
def button(id,item_type):
    items_in_basket=0
    if "user" in session:
        flash("Item added to basket")
        
        username = session.get("user",None)
        mycursor.execute("""SELECT ID FROM Users WHERE username= '%s'""" %(username))
        UserID = mycursor.fetchone()
        ItemID = id

        session["itemid"] = ItemID
        session["userid"] = UserID
        quantity = session.get("quantity",None)
        
        mycursor.execute("INSERT INTO BasketItems(UsersID,productID,quantity) VALUES (%s,%s,%s)",(*UserID,ItemID,quantity))
        mycursor.execute("SELECT * FROM BasketItems")
        for item in mycursor.fetchall():
                items_in_basket+=1

        session["items_in_basket"] = items_in_basket
        if "quantity" in session:
            session.pop("quantity",None)

        db.commit()

        return redirect(url_for(".items_page",item_type=item_type))
        

    else:
        flash("Please make an account or login before purchasing")
        return redirect(url_for("accounts.register_page"))

      

@items.route("/basket",methods=["POST","GET"])

def basket_page():
    total_price = 0
    username = session.get("user",None)
    get_id = """SELECT ID FROM Users WHERE username = '%s' """%(username)
    mycursor.execute(get_id)
    id = mycursor.fetchone()

    session["userid"] = id
    mycursor.execute("""SELECT Item.name,Item.description,Item.price,Item.picfile,Item.type,Item.itemID,BasketItems.quantity AS q FROM Item INNER JOIN BasketItems ON Item.itemID = BasketItems.productID WHERE BasketItems.UsersID = '%s'"""%(id))
    basket_items = mycursor.fetchall()
    for item in basket_items:
        try:
            total_price +=(item[2]*item[6])
        except:
            total_price +=(item[2]*1)
         
    db.commit()
    if request.method =="POST":
        credit_card_num = request.form.get("cn")
        address = request.form.get("ad")

    return render_template("basket.html",basket_items = basket_items,user=session.get("user",None),total_price = round(total_price,2))
        

@items.route("/done")
def done():
     mycursor.execute("TRUNCATE TABLE BasketItems")
     db.commit()
     if "items_in_basket" in session:
          session.pop("items_in_basket",None)
     return redirect(url_for("home.home_page"))

@items.route("/remove/<id>")
def remove(id):
    userid = session.get("userid",None)
    mycursor.execute("""DELETE FROM BasketItems WHERE productID = (%s) AND UsersID = (%s)""",(id,*userid))
    flash("Item removed from basket")
    return redirect(url_for(".basket_page"))



