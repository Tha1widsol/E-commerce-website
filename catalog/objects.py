import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="items"
    )
    

mycursor = db.cursor()

#mycursor.execute("CREATE DATABASE items")

#mycursor.execute("DROP TABLE IF EXISTS Item;")

#mycursor.execute("CREATE TABLE IF NOT EXISTS Item(itemID int PRIMARY KEY AUTO_INCREMENT,type VARCHAR(20),name VARCHAR(50),description TEXT(100),price FLOAT(10), picfile TEXT(20))")




mycursor.execute("""INSERT INTO Item(type,name,description,price,picfile) VALUES
('TV','Samsung Q355Q60R','Samsungs QLED is certified to deliver 100% colour volume.',749.99,'tv1.jpg'),
('TV','Hitachi 58 Inch Smart 4K UHD HDR LED Freeview TV','Bring the cinema to your living room with this 58 inch Hitachi Smart TV. Featuring 4K Ultra HD resolution, you can catch every little detail on your screen.',369.99,'tv2.webp'),
('TV','PHILIPS Ambilight 65" Smart 4K Ultra HD','With an OLED panel, every single pixel is controlled individually, giving deeper blacks, more vibrant colours and better contrast for an image that will look and feel stunningly lifelike.','2399','tv3.jpg'),
('TV','LG 43 Inch Smart Full HD Freeview TV','See a new level of Full-HD with Active HDR technology utilising Dynamic Colour and Virtual Surround Plus, experience film like never before.',279,'tv4.webp')

""")



