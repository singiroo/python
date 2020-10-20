from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello():                           
    return "hello"

@app.route("/info")
def get_profile(username):
    return 'info'
# 
# @app.route("/first/<username>")
# def get_first(username):
#     return "<h3>Hello " + username + "!</h3>"

if __name__ == "__main__":              
    app.run(host="0.0.0.0")