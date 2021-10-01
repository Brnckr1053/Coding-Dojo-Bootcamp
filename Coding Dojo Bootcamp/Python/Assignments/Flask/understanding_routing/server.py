from flask import Flask

app = Flask(__name__)    
@app.route('/')          
def hello_world():
    return 'Hello World!'  

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/say/<name>')
def say(name):
    print(name)
    return "Hi " + name.capitalize() + "!"

@app.route('/repeat/<int:number>/<word>')
def repeat(number, word):
    str = ""
    for i in range(int(number)):
        str += word + " "
    return str

@app.errorhandler(404)
def no_page(e):
    return  "Sorry! No response. Try again.(404)"

if __name__=="__main__":  
    app.run(debug=True)