from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

app = Flask(__name__)

app.config['SECRET_KEY'] = "helsgddo"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_POOL_RECYCLE'] = 90

db = SQLAlchemy(app)

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

class Basket(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
	items = db.relationship('BasketItems', backref='basket', lazy=True)


class BasketItems(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	basket_id = db.Column(db.Integer, db.ForeignKey('basket.id'))
	product_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
	quantity = db.Column(db.Integer, nullable=False,default =1)

def clear_basket(UserID):
	 basket_items = BasketItems.query.filter_by(basket_id=UserID).all()
	 for item in basket_items:
			db.session.delete(item)
	 db.session.commit()

def clear_wishlist(UserID):
	 wishlist_items = WishListItems.query.filter_by(wishlist_id=UserID).all()
	 for item in wishlist_items:
			db.session.delete(item)
	 db.session.commit()

class wishlist(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
	items = db.relationship('WishListItems', backref='wishlist', lazy=True)


class WishListItems(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	wishlist_id = db.Column(db.Integer, db.ForeignKey('wishlist.id'))
	product_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False,unique=True)


db.create_all()

Item.query.delete()

db.session.add(Item(Type='computers',name='HP ProOne 440 G5 23.8" FHD Touchscreen AiO with i',description='Windows 10 Pro 64,Intel® Core™ i5-9500T with Intel® UHD Graphics 630,8 GB memory,60.45 cm (23.8) diagonal FHD IPS widescreen WLED-backlit touch screen',price='898.99',picfile='computer1.jpg'))
db.session.add(Item(Type='computers',name='Acer Nitro 50 i7 8GB 1TB SSD GTX1660 Super Gaming PC',description='Intel Core i710700 processor,Octa core processor,Processor speed 2.9GHz with a burst speed of 4.8GHz,8GB RAM DDR4,1TB SSD storage,NVIDIA GTX 1660 Super with 6GB memory GDDR6',price='1199.99',picfile='computer2.webp'))
db.session.add(Item(Type='computers',name='Vibox I-18 Gaming PC with a Free Game',description = 'Windows 10,Quad Core Ryzen Processor,Radeon Vega 8 Graphics,8GB RAM,1TB Hard Drive',price='614.95',picfile='computer3.jpg'))
db.session.add(Item(Type='computers',name='INFINITY X99 GT GAMING PC',description = 'Windows 10 Home (64-bit Edition) Perfect for most people all the core features of Windows 10.',price='1649',picfile='computer4.webp'))
db.session.add(Item(Type='computers',name='ULTRA R35 GAMING PC',description = 'Windows 10 Home (64-bit Edition) Perfect for most people with all the core features of Windows 10.',price='913',picfile='computer5.webp'))
db.session.add(Item(Type='laptops',name='Acer Nitro 5 17.3in i5 8GB 512GB GTX1650 Gaming Laptop',description = 'Intel Core i5 10300H processor,Quad core processor,2.5GHz processor speed with a burst speed of 4.5GHz,8GB RAM DDR4,512GB SSD storage,Microsoft Windows 10',price='799.99',picfile='laptop1.webp'))
db.session.add(Item(Type='laptops',name='Alienware m15 R3 Laptop',description = 'Intel Core 10th Generation i7-10750H Processor (6 Core, Up to 5.00GHz, 12MB Cache, 45W)Windows 10 Home16GB Memory. NVIDIA GeForce RTX 2070 SUPER 8GB GDDR6',price='1764',picfile='laptop2.webp'))
db.session.add(Item(Type='laptops',name='TURING PRO 3080 GAMING LAPTOP',description = 'Windows 10 Home (64-bit Edition) Perfect for most people with all the core features of Windows 10 including: automatic updates, Cortana and DirectX 12 graphics support (No Recovery Media).',price='1666',picfile='laptop3.webp'))
db.session.add(Item(Type='laptops',name='Lenovo Legion C7 82EH002BUK Core i9-10980HK 32GB 1TB SSD',description = 'Lenovo Legion C7 82EH002BUK Intel Core i9-10980HK (16MB Cache, 2.4GHz) 32GB DDR4-SDRAM.',price='2487.60',picfile='laptop4.jpg'))
db.session.add(Item(Type='laptops',name='Asus TUF Gaming Dash F15 Core i7-11370H 16GB 512GB SSD ',description = 'Processor - Intel Core i711370H - Screensize - 15.6 inch. Graphics card: Geforce RTX 3070 8gb. RAM-16GB.SSD:512GB.',price='1299.97',picfile='laptop5.jpg'))

db.session.commit()

