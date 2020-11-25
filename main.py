from flask import Flask,render_template
from admin.second import second

app = Flask(__name__)
app.register_blueprint(second,url_prefix="/admin") # We only go on second blueprint if we see "/admin"
#It finds "/" then adds "admin" = "/admin" 

@app.route("/")
def test():
    return "<h1> Welcome to my first website </h1>"

 
if __name__ =="__main__":
    app.run()
