from flask import Flask, request, render_template, make_response

import json
import sys
app = Flask(__name__)

@app.route("/")
def helloword():
    return "Hello, World!"

@app.route("/name")
def hellobank():
    return "Hello, Bank!"

@app.route("/home", methods={'POST','GET'}) #add POST send message inbox and GET to get message from url
def homefn():
    if request.method == "GET":
       print('we are in home(GET)', file=sys.stdout)
       name = request.args.get('fname')
       print(name, file=sys.stdout)
       return render_template("home.html",name=name)
        #getting input with name = fname in HTML form
    elif request.method == "POST":
       print('we are in home(POST)', file=sys.stdout)
       namein = request.form.get('fname')
       lastnamein = request.form.get('lname')
       print(namein, file=sys.stdout)
       print(lastnamein, file=sys.stdout)
       return render_template("home.html",name=namein)


if __name__ =="__main__":
    app.run(host='0.0.0.0',debug=True,port=5001)#host='0.0.0.0", port=500

