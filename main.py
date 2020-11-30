from flask import Flask,render_template,redirect,url_for,request,session,flash
import os 
from catalog.second import second

app = Flask(__name__)
app.register_blueprint(second,url_prefix="/items") # We only go on second blueprint if we see "/admin"
#It finds "/" then adds "admin" = "/admin" 

@app.route("/")
@app.route("/home")
def home():
     return render_template("home.html")

class Item():
     def __init__(self,name,filename,description,price):
          self.name=name
          self.filename=filename
          self.description=description
          self.price=price
         
          @app.route("/items")
          def add():
              item_images = []
              item_images.append(os.path.join("static/images",self.filename))
              return render_template("items.html",item_images=item_images,name=self.name,description=self.description,price="Price:"+self.price)
          
     
vaccum1 = Item("Smart vaccum cleaner","vaccum1.jpg","It will suck your lungs out","£29.99")     


   
#Extra comment
if __name__ =="__main__":
    app.run()


        
