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
('computers','HP ProOne 440 G5 23.8" FHD Touchscreen AiO with i5','Windows 10 Pro 64,Intel® Core™ i5-9500T with Intel® UHD Graphics 630,8 GB memory,60.45 cm (23.8) diagonal FHD IPS widescreen WLED-backlit touch screen',898.99,'computer1.jpg'),
('computers','Acer Nitro 50 i7 8GB 1TB SSD GTX1660 Super Gaming PC','Intel Core i710700 processor,Octa core processor,Processor speed 2.9GHz with a burst speed of 4.8GHz,8GB RAM DDR4,1TB SSD storage,NVIDIA GTX 1660 Super with 6GB memory GDDR6',1199.99,'computer2.webp'),
('computers','Vibox I-18 Gaming PC with a Free Game','Windows 10,Quad Core Ryzen Processor,Radeon Vega 8 Graphics,8GB RAM,1TB Hard Drive',614.95,'computer3.jpg'),
('laptops','Acer Nitro 5 17.3in i5 8GB 512GB GTX1650 Gaming Laptop','Intel Core i5 10300H processor,Quad core processor,2.5GHz processor speed with a burst speed of 4.5GHz,8GB RAM DDR4,512GB SSD storage,Microsoft Windows 10',799.99,'computer4.webp'),
('laptops','Alienware m15 R3 Laptop','Intel Core 10th Generation i7-10750H Processor (6 Core, Up to 5.00GHz, 12MB Cache, 45W)Windows 10 Home16GB Memory. NVIDIA GeForce RTX 2070 SUPER 8GB GDDR6',1764.00,'computer5.webp')
""")


#mycursor.execute("CREATE TABLE BasketItems(ID int PRIMARY KEY AUTO_INCREMENT,UsersID int,productID int DEFAULT 0,quantity int DEFAULT 1)")

#mycursor.execute("ALTER TABLE BasketItems ADD FOREIGN KEY(productID) REFERENCES Item(itemID)")

#mycursor.execute("DROP TABLE IF EXISTS Item;")

#mycursor.execute("CREATE TABLE IF NOT EXISTS Users (ID int PRIMARY KEY AUTO_INCREMENT,email VARCHAR(100),username VARCHAR(1000),password VARCHAR(10000))")



#mycursor.execute("ALTER TABLE BasketItems ADD FOREIGN KEY(productID) REFERENCES Item(itemID)")
