from flask import Flask
# from flask import request

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name="Solvaring"):
    return "Hello from {}".format(name)



@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
@app.route('/add/<int:num1>/<float:num2>')
def add(num1, num2):
    # name = request.args.get('name', name)
    return '{} + {} = {}'.format(num1, num2, num1+num2)

if __name__ == "__main__":
    from os import environ
    if 'WINGDB_ACTIVE' not in environ:
        app.debug = True
    app.run(port=8000, host='localhost', use_reloader=True)    