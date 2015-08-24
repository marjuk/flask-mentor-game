from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def homePage():
    return render_template('home.html')

@app.route('/page1')
def page1():
    return render_template('page1.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

if __name__=="__main__":
    app.run(debug=False,host="0.0.0.0")
