from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

app = Flask(__name__)

app.config['SECRET_KEY'] = "helsgddo"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_POOL_RECYCLE'] = 90

db = SQLAlchemy(app)
# mycursor.execute("CREATE TABLE BasketItems(ID int PRIMARY KEY AUTO_INCREMENT,UsersID int,productID int DEFAULT 0,quantity int DEFAULT 1)")
   # mycursor.execute("ALTER TABLE BasketItems ADD FOREIGN KEY(productID) REFERENCES Item(itemID)")
   # mycursor.execute("CREATE TABLE IF NOT EXISTS Users (ID int PRIMARY KEY AUTO_INCREMENT,email VARCHAR(100),username VARCHAR(1000),password VARCHAR(10000))")
   # mycursor.execute("ALTER TABLE BasketItems ADD FOREIGN KEY(UsersID) REFERENCES Users(ID)")

class Users(db.Model):
    id = db.Column("id",db.Integer,primary_key=True)
    email = db.Column(db.String(),unique=True)
    password = db.Column(db.String(),unique=True)
    
    def __init__(self,email,password):
        self.email = email 
        self.password = password

class Item(db.Model):
     id = db.Column("id",db.Integer,primary_key=True)
     Type = db.Column(db.String())
     name = db.Column(db.String(),unique=True)
     description = db.Column(db.Text,unique=True)
     price = db.Column(db.Float)
     picfile = db.Column(db.String(),unique=True)

     def __init__(self,Type,name,description,price,picfile):
        self.Type = Type
        self.name = name
        self.description = description
        self.price = price
        self.picfile = picfile

Item.query.delete()

db.session.add(Item(Type='computers',name='HP ProOne 440 G5 23.8" FHD Touchscreen AiO with i',description='indows 10 Pro 64,Intel® Core™ i5-9500T with Intel® UHD Graphics 630,8 GB memory,60.45 cm (23.8) diagonal FHD IPS widescreen WLED-backlit touch screen',price='898.99',picfile='computer1.jpg'))
db.session.commit()

#('computers','HP ProOne 440 G5 23.8" FHD Touchscreen AiO with i5','Windows 10 Pro 64,Intel® Core™ i5-9500T with Intel® UHD Graphics 630,8 GB memory,60.45 cm (23.8) diagonal FHD IPS widescreen WLED-backlit touch screen',898.99,'computer1.jpg'),
#('computers','Acer Nitro 50 i7 8GB 1TB SSD GTX1660 Super Gaming PC','Intel Core i710700 processor,Octa core processor,Processor speed 2.9GHz with a burst speed of 4.8GHz,8GB RAM DDR4,1TB SSD storage,NVIDIA GTX 1660 Super with 6GB memory GDDR6',1199.99,'computer2.webp'),
#('computers','Vibox I-18 Gaming PC with a Free Game','Windows 10,Quad Core Ryzen Processor,Radeon Vega 8 Graphics,8GB RAM,1TB Hard Drive',614.95,'computer3.jpg'),
#('computers','INFINITY X99 GT GAMING PC','Windows 10 Home (64-bit Edition) Perfect for most people with all the core features of Windows 10.',1649,'computer4.webp'),
#('computers','ULTRA R35 GAMING PC','Windows 10 Home (64-bit Edition) Perfect for most people with all the core features of Windows 10. ',913,'computer5.webp'),
#('laptops','Acer Nitro 5 17.3in i5 8GB 512GB GTX1650 Gaming Laptop','Intel Core i5 10300H processor,Quad core processor,2.5GHz processor speed with a burst speed of 4.5GHz,8GB RAM DDR4,512GB SSD storage,Microsoft Windows 10',799.99,'laptop1.webp'),
#('laptops','Alienware m15 R3 Laptop','Intel Core 10th Generation i7-10750H Processor (6 Core, Up to 5.00GHz, 12MB Cache, 45W)Windows 10 Home16GB Memory. NVIDIA GeForce RTX 2070 SUPER 8GB GDDR6',1764.00,'laptop2.webp'),
#('laptops','TURING PRO 3080 GAMING LAPTOP','Windows 10 Home (64-bit Edition) Perfect for most people with all the core features of Windows 10 including: automatic updates, Cortana and DirectX 12 graphics support (No Recovery Media).',1666,'laptop3.webp'),
#('laptops','Lenovo Legion C7 82EH002BUK Core i9-10980HK 32GB 1TB SSD','Lenovo Legion C7 82EH002BUK Intel Core i9-10980HK (16MB Cache, 2.4GHz) 32GB DDR4-SDRAM',2487.60,'laptop4.jpg'),
#('laptops','Asus TUF Gaming Dash F15 Core i7-11370H 16GB 512GB SSD ','Processor - Intel Core i711370H - Screensize - 15.6 inch. Graphics card: Geforce RTX 3070 8gb. RAM-16GB.SSD:512GB.',1299.97,'laptop5.jpg')
#""")

#mycursor.execute("CREATE TABLE BasketItems(ID int PRIMARY KEY AUTO_INCREMENT,UsersID int,productID int DEFAULT 0,quantity int DEFAULT 1)")

#mycursor.execute("ALTER TABLE BasketItems ADD FOREIGN KEY(productID) REFERENCES Item(itemID)")

#mycursor.execute("DROP TABLE IF EXISTS Item;")

#mycursor.execute("CREATE TABLE IF NOT EXISTS Users (ID int PRIMARY KEY AUTO_INCREMENT,email VARCHAR(100),username VARCHAR(1000),password VARCHAR(10000))")



#mycursor.execute("ALTER TABLE BasketItems ADD FOREIGN KEY(productID) REFERENCES Item(itemID)")


   

db.create_all()
#setup()