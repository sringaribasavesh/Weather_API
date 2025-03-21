import requests
from flask import Flask,render_template,request
localserver = True
app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
    if request.method == "POST":
        city = request.form["city"]
        country = request.form["country"]
        api_key = "dfbf70c1f92d6dc8542b15b8740f7490"
        
        we_url = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric")
        repon = we_url.json()
        
        temp = repon['main']['temp']
        humidity = repon['main']['humidity']
        wind_speed = repon['wind']['speed']
    
    
    
        return render_template("result.html",temp=temp,humidity=humidity,wind_speed=wind_speed,city=city)
    return render_template("index.html")


app.run(debug=True)