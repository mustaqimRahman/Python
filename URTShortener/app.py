from email import message
from re import U
from flask import Flask, redirect
from flask import render_template
from forms import UrlShortener
import random

from cryptography.fernet import Fernet

urls = [{'zWMqKI' : 'www.xyz.com'}]
 
app= Flask(__name__)

app.config["SECRET_KEY"] = "sdcfdsvfgdbhfvdsfs3243456y5"





@app.route('/', methods=["GET", "POST"])
def home():
    form = UrlShortener()
    if form.submit():
        print('Stored URL')
        key = Fernet.generate_key()
        key = ((str(key).replace('_','')).replace('=','')).replace('-','')
        key = key[2:8]
        url = form.url.data
        # urls[str(key)]= url
        urls.append({key:url})
        print(urls)
    return render_template("home.html", form = form, key = key )

@app.route('/<short_url>')
def url_redirect(short_url):
    # original_url = urls[short_url]
    short_url= str(short_url)
    for each in urls:
        if short_url in each.keys():
            original_url = each[short_url]
            print(original_url)    

    return redirect(original_url)



app.run(debug =True)


