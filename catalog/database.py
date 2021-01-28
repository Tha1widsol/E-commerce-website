import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="items"
    )
    
mycursor = db.cursor(buffered=True)

#mycursor.execute("CREATE DATABASE items")



#mycursor.execute("DROP TABLE IF EXISTS BasketItems;")

for _ in mycursor.execute("SET FOREIGN_KEY_CHECKS = 0; DROP TABLE IF EXISTS Item; SET FOREIGN_KEY_CHECKS = 1;",multi=True): pass
mycursor.execute("CREATE TABLE IF NOT EXISTS Item(itemID int PRIMARY KEY AUTO_INCREMENT,type VARCHAR(2000),name VARCHAR(2000),description TEXT(2000),price FLOAT(20), picfile TEXT(2000))")


mycursor.execute("""INSERT INTO Item(type,name,description,price,picfile) VALUES
('TV','Samsung Q355Q60R','Samsungs QLED is certified to deliver 100% colour volume.',749.99,'tv1.jpg'),
('TV','Hitachi 58 Inch Smart 4K UHD HDR LED Freeview TV','Bring the cinema to your living room with this 58 inch Hitachi Smart TV. Featuring 4K Ultra HD resolution, you can catch every little detail on your screen.',369.99,'tv2.webp'),
('TV','PHILIPS Ambilight 65" Smart 4K Ultra HD','With an OLED panel, every single pixel is controlled individually, giving deeper blacks, more vibrant colours and better contrast for an image that will look and feel stunningly lifelike.',2399.99,'tv3.jpg'),
('TV','LG 43 Inch Smart Full HD Freeview TV','See a new level of Full-HD with Active HDR technology utilising Dynamic Colour and Virtual Surround Plus, experience film like never before.',279,'tv4.webp'),
('Vaccumcleaners','Hetty HET 160-11 Bagged Cylinder Vacuum Cleaner',' Packed full of great features to make cleaning easy, including a huge capacity, versatile toolkit and super long-reach, trouble-free rewind cable. ',99.99,'vaccum1.webp'),
('Vaccumcleaners','Bush Cordless Handstick Vacuum Cleaner','Deal with dust and dander with the Bush cordless stick vacuum cleaner. Suitable for all floor surfaces, it is the perfect sidekick for cleaning your whole home in one go. ',79.99,'vaccum2.webp'),
('Vaccumcleaners','RoboVac 11S','Turn chore time into play time! RoboVac sweeps, vacuums, and recharges automatically.',189.99,'vaccum3.png'),
('Vaccumcleaners','Henry HVR 160-11 Bagged Cylinder Vacuum Cleaner','With over 10 million Henrys made, and most still in use today, he really is the vacuum you can trust.',139.99,'vaccum4.webp'),
('computers','HP ProOne 440 G5 23.8" FHD Touchscreen AiO with i5','Windows 10 Pro 64,Intel® Core™ i5-9500T with Intel® UHD Graphics 630,8 GB memory,60.45 cm (23.8) diagonal FHD IPS widescreen WLED-backlit touch screen',898.99,'computer1.jpg'),
('computers','Acer Nitro 50 i7 8GB 1TB SSD GTX1660 Super Gaming PC','Intel Core i710700 processor,Octa core processor,Processor speed 2.9GHz with a burst speed of 4.8GHz,8GB RAM DDR4,1TB SSD storage,NVIDIA GTX 1660 Super with 6GB memory GDDR6',1199.99,'computer2.webp'),
('computers','Vibox I-18 Gaming PC with a Free Game','Windows 10,Quad Core Ryzen Processor,Radeon Vega 8 Graphics,8GB RAM,1TB Hard Drive',614.95,'computer3.jpg'),
('computers','Acer Nitro 5 17.3in i5 8GB 512GB GTX1650 Gaming Laptop','Intel Core i5 10300H processor,Quad core processor,2.5GHz processor speed with a burst speed of 4.5GHz,8GB RAM DDR4,512GB SSD storage,Microsoft Windows 10',799.99,'computer4.webp'),
('TV','Samsung 50 TU8000 HDR Smart 4K TV with Tizen OS','Crystal Display: lose yourself in crystal clear colour',479.00,'tv5.jpg')
""")


#mycursor.execute("CREATE TABLE BasketItems(ID int PRIMARY KEY AUTO_INCREMENT,UsersID int,productID int DEFAULT 0,quantity int DEFAULT 1)")

#mycursor.execute("ALTER TABLE BasketItems ADD FOREIGN KEY(productID) REFERENCES Item(itemID)")

#mycursor.execute("DROP TABLE IF EXISTS Item;")

#mycursor.execute("CREATE TABLE IF NOT EXISTS Users (ID int PRIMARY KEY AUTO_INCREMENT,email VARCHAR(100),username VARCHAR(1000),password VARCHAR(10000))")



#mycursor.execute("ALTER TABLE BasketItems ADD FOREIGN KEY(productID) REFERENCES Item(itemID)")
