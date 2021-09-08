from flask_admin import Admin
from flask import session
from flask_admin.contrib.sqla import ModelView
from catalog.database import *

admin = Admin(app,name="Admin panel",template_mode='bootstrap4')

class AdminView(ModelView):
    def is_accessible(self):
        if "user" in session:
            User = get_user(session.get("user",None))
            return User.is_admin

        return False

        
admin.add_view(AdminView(Users,db.session))
admin.add_view(AdminView(Item,db.session))
admin.add_view(AdminView(Basket,db.session))
admin.add_view(AdminView(BasketItems,db.session))
admin.add_view(AdminView(wishlist,db.session))
admin.add_view(AdminView(WishListItems,db.session))

