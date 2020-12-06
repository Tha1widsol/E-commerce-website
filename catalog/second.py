from flask import Blueprint,render_template
import os

second = Blueprint("second",__name__,static_folder="static",template_folder="templates")


class Item():
     def __init__(self,Type,name,filename,description,price):
          self.Type=Type
          self.name=name
          self.filename=filename
          self.description=description
          self.price=price
      

   
          @second.route("/items")
          def add():
              item_images=[]
              item_images.append(os.path.join("static/images",self.filename))
              return render_template("items.html",Type=self.Type,item_images=item_images,name=self.name,description=self.description,price="Price:"+self.price,itemtab="active")
          
          @second.route("/purchased")         
          def button():
               return "<p> You bought this item </p>"



