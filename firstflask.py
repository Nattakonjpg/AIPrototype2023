from flask import Flask, request, render_template, make_response

import json

app = Flask(_name_)

@app.route("/")
def helloword():
    return "Hello, World!"

if __name__== "__main__"
    app.run(host='0.0.0.0',debug=True,port=50001)#host='0.0.0.0", port=500
