from flask import Flask, request, render_template
from math import *

app = Flask(__name__)


@app.route('/')
def calculate():
    expr = request.args.get('expr')
    if expr is None:
        result = 'Введите выражение для вычисления'
    else:
        try:
            result = eval(expr)
        except:
            result = 'Пожалуйста, проверьте правильность введенных данных'

    return render_template('base.html', result=result)


'''

Это реализация без шаблона. Значения аргументов вводятся через адресную строку, а не через шаблон.

@app.route('/<expr>')
def calculate(expr):
    try:
        result = f'Ответ: {eval(expr)}'
    except:
        result = 'Пожалуйста, проверьте правильность введенных данных'

    return result

'''

if __name__ == '__main__':
    app.run()
