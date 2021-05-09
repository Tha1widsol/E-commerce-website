from flask import Blueprint,render_template,request,session,flash,url_for,redirect
import os
from catalog.database import *


items = Blueprint("items",__name__,static_folder="static",template_folder="templates")
    
@items.route("/",methods=["POST","GET"])
@items.route("/home",methods=["POST","GET"])
def home_page():
    no_items = ""
    search_value=session.get("search",None)
    if search_value==None:
        search_value=""
        
    if session.get("order",None)=="desc":
       desktops =  Item.query.filter(Item.name.contains(search_value),Item.Type.contains("computers")).order_by(desc("price")).all()
       laptops =   Item.query.filter(Item.name.contains(search_value),Item.Type.contains("laptops")).order_by(desc("price")).all()
    
    elif session.get("order",None)=="asc":
         desktops =  Item.query.filter(Item.name.contains(search_value),Item.Type.contains("computers")).order_by("price").all()
         laptops =   Item.query.filter(Item.name.contains(search_value),Item.Type.contains("laptops")).order_by("price").all()
    
    else:
        if "search" in session:
            session.pop("search")

        desktops =  Item.query.filter_by(Type="computers")
        laptops =  Item.query.filter_by(Type="laptops")

    if request.method=="POST":
        form = request.form 
        search_value = form['search_string']
        session["search"] = search_value
        desktops = Item.query.filter(Item.name.contains(search_value),Item.Type.contains("computers")).all()
        laptops = Item.query.filter(Item.name.contains(search_value),Item.Type.contains("laptops")).all()

    if not(desktops) and not(laptops):
        no_items="No items found"
            
    if "user" in session:
        return render_template("items.html",desktops=desktops,laptops=laptops,no_items=no_items,user= session.get("user",None),hometab="active")
   
    return render_template("items.html",desktops=desktops,laptops=laptops,no_items=no_items,user=None,hometab="active")

@items.route("/<product_id>",methods=["POST","GET"])
def product_view(product_id):
    if request.method=="POST":
        session["quantity"] = request.form.get("dropdown")
    return render_template("product.html",item=Item.query.filter_by(id=product_id).first(),user= session.get("user",None))

@items.route("/order/<change>")
def order(change):
    session["order"]= change
    return redirect(url_for("items.home_page"))

@items.route("/search",methods=["POST","GET"])
def search():
    

    return redirect(url_for("items.home_page"))
        
   

@items.route("/button/<product_id>/<item_type>")
def add_to_basket(product_id,item_type):
    if "user" in session:
        flash("Item added to basket")
        email = session.get("user",None)
        User = Users.query.filter_by(email = email).first()
        quantity = session.get("quantity",None)
        basket = Basket.query.filter_by(user_id=User.id).first()
        basket_item = BasketItems(basket_id=basket.id, product_id=product_id, quantity=quantity)
        db.session.add(basket_item)
        db.session.commit()

        if "quantity" in session:
            session.pop("quantity",None)

        return redirect(url_for("items.home_page",item_type=item_type))

    else:
        flash("Please make an account or login before purchasing")
        return redirect(url_for("accounts.register_page"))

@items.route("/wishlist/<product_id>/<item_type>")
def add_to_wishlist(product_id,item_type):
    if "user" in session:
        email = session.get("user",None)
        User = Users.query.filter_by(email = email).first()
        Wishlist = wishlist.query.filter_by(user_id=User.id).first()
        try:
            wishlist_item = WishListItems(wishlist_id=Wishlist.id, product_id=product_id)
            db.session.add(wishlist_item)
            
            db.session.commit()
            flash("Item added to wishlist")
        
        except:
            flash("Item is already added to wishlist")
        

        return redirect(url_for("items.home_page"))

    else:
        flash("Please make an account or login before adding to wishlist")
        return redirect(url_for("accounts.register_page"))

@items.route("/wishlist")  
def wishlist_page():
    wishlistDict = {}
    if "user" in session:
        email = session.get("user",None)
        User = Users.query.filter_by(email = email).first()  
        items = WishListItems.query.filter_by(wishlist_id=User.id).all()
        for item in items:
            product = Item.query.filter_by(id=item.product_id).first()
            
            if product.id in wishlistDict.keys():
                list = wishlistDict[product.id]
                wishlistDict[product.id] = [product.name, product.picfile, item.id,product.description,product.Type,product.id]

        
            else:
                wishlistDict[product.id] = [product.name, product.picfile, item.id,product.description,product.Type,product.id]

        return render_template("wishlist.html",cart = wishlistDict,user=session.get("user",None),wishlist_tab="active",n = len(wishlistDict))
    
    else:
        flash("Please log in or register to access wishlist page")
        return redirect(url_for("accounts.register_page"))

   



@items.route("/basket")
def basket_page():
    shoppingDict = {}
    subtotal = 0
    products = Item.query.all()
    if "user" in session:
        email = session.get("user",None)
        User = Users.query.filter_by(email = email).first()
        items = BasketItems.query.filter_by(basket_id=User.id).all()

        for item in items:
            product = Item.query.filter_by(id=item.product_id).first()
            if product.id in shoppingDict.keys():
                list = shoppingDict[product.id]
                quant = int(list[1]) + item.quantity
                subtotal += float(quant * product.price)
                shoppingDict[product.id] = [product.name, quant, product.price,  product.picfile, product.id,product.description,product.Type]
        
            else:
                subtotal += float(item.quantity * product.price)
                shoppingDict[product.id] = [product.name, item.quantity, product.price,product.picfile, product.id,product.description,product.Type]

        return render_template("basket.html",cart=shoppingDict,products=products,subtotal=round(subtotal,2),user=session.get("user",None),basket_tab = "active")
    
    else:
        flash("Please register or login before accessing basket page")
        return redirect(url_for("accounts.register_page"))
        

@items.route("/done")
def done():
    email = session.get("user",None)
    User = Users.query.filter_by(email = email).first()
    clear_basket(User.id)
    return redirect(url_for("items.home_page"))

@items.route("/basket/<product_id>")
def remove_from_basket(product_id):
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


@items.route("/wishlist/<product_id>")
def remove_from_wishlist(product_id):
    email = session.get("user",None)
    User = Users.query.filter_by(email = email).first()
    try:
        wishlist_product = WishListItems.query.filter_by(id=product_id, wishlist_id=User.id).first()
        db.session.delete(wishlist_product)
        db.session.commit()
        flash("Item removed from wishlist")

    except:
        clear_wishlist(User.id)
        flash("All items are cleared from wishlist")

    return redirect(url_for(".wishlist_page"))



