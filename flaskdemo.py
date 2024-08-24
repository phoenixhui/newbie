from flask import Flask

app = Flask(__name__)


## Basic flask function: @app.route
## ('/testA/'): 
#  (1) Must use ' ', not " "
#  (2) Must use '/xxx/', not '/xxx'
@app.route('/testA/')
def hello_world():
    return"Hello A, World!"



app.run()