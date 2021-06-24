from flask import Flask,request
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return "<h1> THis is Flask APPLICATION </h1>"
if __name__ == '__main__':
    app.run()