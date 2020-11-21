from flask import Flask 
  
app = Flask(__name__) 
  
@app.route("/") 
def home_view(): 
        return "<h1>Flask on Ubuntu deployed to Heroku by Kudos Beluga!</h1>"