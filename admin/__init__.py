from flask_admin import Admin
from flask import session,render_template,redirect,url_for
from flask_admin.contrib.sqla import ModelView
from flask_login import login_user
from .accounts import register_page
from catalog.database import *

admin = Admin(app,name="Admin panel",template_mode='bootstrap4')

class AdminView(ModelView):
    def is_accessible(self):
        if "user" in session:
            User = get_userid(session.get("user",None))
            return User.is_admin

        return False

        
admin.add_view(AdminView(Users,db.session))
admin.add_view(AdminView(Item,db.session))
admin.add_view(AdminView(Basket,db.session))
admin.add_view(AdminView(BasketItems,db.session))
admin.add_view(AdminView(wishlist,db.session))
admin.add_view(AdminView(WishListItems,db.session))

