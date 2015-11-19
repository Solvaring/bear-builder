from flask import Flask
from flask import render_template
# from flask import request

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name="Solvaring"):
    # name = request.args.get('name', name) 
    return render_template("index.html", name=name)



@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
@app.route('/add/<int:num1>/<float:num2>')
def add(num1, num2):
    context = {'num1': num1, 'num2': num2}
    return render_template("add.html", **context)

if __name__ == "__main__":
    from os import environ
    if 'WINGDB_ACTIVE' not in environ:
        app.debug = True
    app.run(port=8000, host='192.168.1.114', use_reloader=True)    