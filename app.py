from flask import Flask, render_template

app = Flask(__name__)

menu = ['Home', 'About']


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html', menu=menu)


@app.route('/about')
def about():  # put application's code here
    return render_template('about.html', title='Про Flask', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
