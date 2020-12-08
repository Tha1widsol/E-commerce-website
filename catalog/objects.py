import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="items"
    )
    

mycursor = db.cursor()

#mycursor.execute("CREATE DATABASE items")

mycursor.execute("DROP TABLE IF EXISTS Item;")

mycursor.execute("CREATE TABLE IF NOT EXISTS Item(itemID int PRIMARY KEY AUTO_INCREMENT,type VARCHAR(20),name VARCHAR(50),description TEXT(100),price FLOAT(10), picfile TEXT(20))")





mycursor.execute("INSERT INTO Item(type,name,description,price,picfile) VALUES ('TV','Samsung Q355Q60R','Samsungs QLED is certified to deliver 100% colour volume.',749.99,'tv1.jpg')")



