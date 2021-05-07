from flask import Blueprint,render_template,request,session,flash,url_for,redirect
import os
from catalog.database import *


items = Blueprint("items",__name__,static_folder="static",template_folder="templates")

def get_ascending_order(item_type):
    return Item.query.filter_by(Type=item_type).order_by("price")

def get_descending_order(item_type):
     return Item.query.filter_by(Type=item_type).order_by(desc("price"))

def get_items(item_type):
    return Item.query.filter_by(Type=item_type)

@items.route("/<item_type>",methods=["POST","GET"])
def items_page(item_type):
    if item_type=="laptops" or item_type=="computers":
        if session.get("order",None)=="1":
            items=get_ascending_order(item_type)
            
        elif session.get("order",None)=="2":
            items=get_descending_order(item_type)

        else:
            items= get_items(item_type)

        if item_type=="computers":
            computerstab="active"
        else:
            computerstab=None

            
        if item_type=="laptops":
            laptopstab="active"
        else:
            laptopstab=None

        if "user" in session:
            return render_template("items.html",page_name=item_type,database=items,computerstab=computerstab,laptopstab= laptopstab,user= session.get("user",None))
        else:
            return render_template("items.html",page_name=item_type,database=items,computerstab=computerstab,laptopstab= laptopstab,user=None)
    else:
        if request.method=="POST" and "user" in session:
            quantity = request.form.get("dropdown")
            session["quantity"] = quantity

        item = Item.query.filter_by(id=item_type).first()
        return render_template("product.html",item=item,user= session.get("user",None))


@items.route("<item_type>/<change>")
def order(item_type,change):
    session["order"]= change
    return redirect(url_for(".items_page",item_type=item_type))

@items.route("/button/<id>/<item_type>")
def add_to_basket(id,item_type):
    if "user" in session:
        flash("Item added to basket")
        email = session.get("user",None)
        UserID = Users.query.filter_by(email = email).first()

        quantity = session.get("quantity",None)

        basket = Basket.query.filter_by(user_id=UserID.id).first()
        basket_item = BasketItems(basket_id=basket.id, product_id=id, quantity=quantity)
        db.session.add(basket_item)
        db.session.commit()

        if "quantity" in session:
            session.pop("quantity",None)

        return redirect(url_for(".items_page",item_type=item_type))
        

    else:
        flash("Please make an account or login before purchasing")
        return redirect(url_for("accounts.register_page"))


      

@items.route("/basket")
def basket_page():
    subtotal = 0 
    email = session.get("user",None)
    User = Users.query.filter_by(email = email).first()
    products = Item.query.all()
    shoppingDict = {}
    items = BasketItems.query.filter_by(basket_id=User.id).all()

    for item in items:
        product = Item.query.filter_by(id=item.product_id).first()
        if product.id in shoppingDict.keys():
            list = shoppingDict[product.id]
            quant = int(list[1]) + item.quantity
            subtotal = int(quant * product.price)
            shoppingDict[product.id] = [product.name, quant, product.price, subtotal, product.picfile, item.id,product.description,product.Type]
    
        else:
            subtotal = int(item.quantity * product.price)
            shoppingDict[product.id] = [product.name, item.quantity, product.price, subtotal, product.picfile, item.id,product.description,product.Type]
  

    if request.method =="POST":
        credit_card_num = request.form.get("cn")
        address = request.form.get("ad")


    return render_template("basket.html", products=products,cart=shoppingDict,subtotal=subtotal,user=session.get("user",None),basket_tab = "active")
        

@items.route("/done")
def done():
    email = session.get("user",None)
    User = Users.query.filter_by(email = email).first()
    clear_basket(User.id)
    return redirect(url_for("home.home_page"))

@items.route("/remove/<product_id>")
def remove(product_id):
    email = session.get("user",None)
    User = Users.query.filter_by(email = email).first()
    try:
        basket_product = BasketItems.query.filter_by(id=product_id, basket_id=User.id).first()
        db.session.delete(basket_product)
        db.session.commit()
        flash("Item removed from basket")

    except:
        clear_basket(User.id)
        flash("All items are cleared from basket")

    return redirect(url_for(".basket_page"))



