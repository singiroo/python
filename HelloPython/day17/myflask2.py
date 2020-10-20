from flask import Flask,render_template

app = Flask(__name__)
@app.route("/hello/<msg>")
def hello(msg):                           
    return render_template('helllo.html', msg=msg)

# 
# @app.route("/first/<username>")
# def get_first(username):
#     return "<h3>Hello " + username + "!</h3>"

if __name__ == "__main__":              
    app.run(host="0.0.0.0")