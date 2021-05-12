from flask import Flask
from catalog.items import *
from admin.accounts import *
from catalog.database import *
from catalog.database import app as application

application.register_blueprint(items,url_prefix="/") 
application.register_blueprint(accounts,url_prefix="/")

if __name__ =="__main__":
	application.run(debug=True)


		