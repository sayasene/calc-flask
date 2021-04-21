from flask import Flask, request

import operations

app = Flask(__name__)


@app.route('/')
def landingPage():
    """returns a welcome message for the root page"""
    return """
        <html>
            <body>
                <h1>Welcome to the calculator!</h1>
            <body>
        </html>
        """


@app.route('/add')
def addition():
    """returns the sum of the two query string parameters"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"<h1> sum is {operations.add(a,b)}.</h1>"


@app.route('/sub')
def subtraction():
    """returns the difference of the two query string parameters"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"<h1> difference is {operations.sub(a,b)}.</h1>"


@app.route('/mult')
def multiplication():
    """returns the product of the two query string parameters"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"<h1> product is {operations.mult(a,b)}.</h1>"


@app.route('/div')
def division():
    """returns the quotient of the two query string parameters"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"<h1> quotient is {operations.div(a,b)}.</h1>"

