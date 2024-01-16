from flask import Flask, request, render_template, make_response

import json

app = Flask(__name__)

@app.route("/")
def helloword():
    return "Hello, World!"

@app.route("/name")
def hellobank():
    return "Hello, Bank!"

@app.route("/home", mthods={'POST','GET'})
def homefn():
    print('we are in home')
    #getting input with name = fname in HTML form
    namein = request.form.get('fname')
    agein = request.form.get('lname')
    print(namein)
    print(agein)
    return render_template("home.html", name=namein)



if __name__ =="__main__":
    app.run(host='0.0.0.0',debug=True,port=5001)#host='0.0.0.0", port=500
