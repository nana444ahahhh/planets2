from flask import render_template
import flask
from flask import Flask
from flask import url_for
from flask import request

app = Flask(__name__)

i = 0


@app.route('/')
@app.route('/index')
def index1():
    param = {}
    param['username'] = "Ученик Яндекс.Лицея"
    param['title'] = 'Домашняя страница'
    return render_template('index.html', **param)


@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=2)


@app.route('/observerr')
def observe():
    return render_template('base.html', подстановка="киуаик")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
